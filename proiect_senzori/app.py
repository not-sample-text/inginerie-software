import os
import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
from flask import Flask, render_template, request, jsonify, send_from_directory

#! PART 1: API CALLS - Data Fetching Layer

def fetch_solar_data(region_code, start=None, end=None):
    """
    Fetches solar generation data from the PV Live API for a specific region.
    
    Args:
        region_code: NUTS code for the region
        start: Start date in YYYY-MM-DD format
        end: End date in YYYY-MM-DD format
        
    Returns:
        Raw JSON data from the API or None if request failed
    """
    url = f"https://api.pvlive.uk/pvlive_eu/api/v5/nuts/{region_code}"
    params = {k: v for k, v in {'start': start, 'end': end}.items() if v}
    
    try:
        print(f"Fetching data for region: {region_code}...")
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json().get('data', [])
    except requests.exceptions.RequestException as e:
        print(f"API request failed for {region_code}: {e}")
        return None

#! PART 2: DATA PROCESSING - Data Processing Layer

# Directory to save plots
SAVE_DIR = "static/img"

def ensure_directory(path):
    # ! Ensures the existence of the directory for saving files.
    os.makedirs(path, exist_ok=True)

def remove_files(path, clear_existing=False):
    # ? Removes all files in the directory if clear_existing is True.
    if clear_existing and os.path.exists(path):
        for file in os.listdir(path):
            os.remove(os.path.join(path, file))

class SolarData:
    # ? Handles processing and visualization of solar generation data.
    
    def __init__(self, region_code, raw_data=None):
        self.region_code = region_code
        self.data = None
        self.plot_files = []
        if raw_data:
            self.process_data(raw_data)
    
    def process_data(self, raw_data):
        # ? Processes raw data into a DataFrame.
        if not raw_data:
            return False
            
        self.data = pd.DataFrame(raw_data, columns=['region', 'timestamp', 'generation_mw'])
        if not self.data.empty:
            # * Convert timestamp to datetime without timezone
            self.data['datetime'] = pd.to_datetime(self.data['timestamp']).dt.tz_localize(None)
            print(f"Processed {len(self.data)} data points for {self.region_code}.")
            return True
        return False
    
    def generate_plots(self, clear_existing=False):
        # ? Generates and saves plots for the region data.
        if self.data is None or self.data.empty:
            print(f"No data available to plot for {self.region_code}.")
            return []
        
        # * Clear existing plots if requested
        if clear_existing:
            self._clear_region_plots()
        
        self.plot_files = []
        date_str = self.data['datetime'].iloc[0].strftime("%Y-%m-%d")
        
        # * Plot settings for light and dark mode
        plot_settings = {
            False: {'suffix': '', 'bg': '#e7e5e4', 'text': '#292524', 'line': '#6366f1'},
            True: {'suffix': '_dark', 'bg': '#292524', 'text': '#e7e5e4', 'line': '#818cf8'}
        }
        
        for dark_mode, settings in plot_settings.items():
            plt.figure(figsize=(16, 9), dpi=300)
            ax = plt.gca()
            ax.set_facecolor(settings['bg'])
            plt.gcf().patch.set_facecolor(settings['bg'])

            plt.plot(self.data['datetime'], self.data['generation_mw'],
                        color=settings['line'], label=f"Region {self.region_code}")
            plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
            plt.xlabel('Time', color=settings['text'])
            plt.ylabel('Generation (MW)', color=settings['text'])
            plt.title(f'Solar Generation for {self.region_code} on {date_str}',
                        color=settings['text'], fontsize=24)
            plt.legend()
            plt.grid(True, color='gray', alpha=0.3)
            ax.tick_params(axis='x', colors=settings['text'])
            ax.tick_params(axis='y', colors=settings['text'])
            plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)

            filename = f"{self.region_code}_plot{settings['suffix']}.svg"
            full_path = os.path.join(SAVE_DIR, filename)
            plt.savefig(full_path)
            plt.close()
            self.plot_files.append(filename)
            print(f"Plot saved: {full_path}")
            
        return self.plot_files
    
    def _clear_region_plots(self):
        # ? Removes existing plots for this region.
        if os.path.exists(SAVE_DIR):
            for file in os.listdir(SAVE_DIR):
                if file.startswith(f"{self.region_code}_plot") and file.endswith('.svg'):
                    os.remove(os.path.join(SAVE_DIR, file))
    
    def __str__(self):
        return f"Region {self.region_code} with {len(self.data) if self.data is not None else 0} data points."

def process_region(region_code, start=None, end=None):
    # ? Complete workflow to fetch, process and plot data for a region.
    # ? Returns:
    # ?    SolarData object with processed data and generated plots
    
    raw_data = fetch_solar_data(region_code, start, end)
    solar_data = SolarData(region_code)
    if solar_data.process_data(raw_data):
        solar_data.generate_plots()
    return solar_data

def get_default_regions():
    # ? Returns a list of default region codes to process.
    return ['BE1', 'BE3']

def initialize_data(clear_existing=True):
    # ? Generate initial dataset if not already present.
    if clear_existing:
        remove_files(SAVE_DIR, clear_existing=True)
    
    results = {}
    for region_code in get_default_regions():
        # * Use default date range (1 month back from today)
        today = datetime.now()
        end_date = today.strftime('%Y-%m-%d')
        start_date = (today - timedelta(days=30)).strftime('%Y-%m-%d')
        
        solar_data = process_region(region_code, start_date, end_date)
        if solar_data.plot_files:
            results[region_code] = solar_data.plot_files
    
    return results

#! PART 3: WEB APP - Flask Application Layer

app = Flask(__name__)

# ? Ensure the image directory exists
ensure_directory(SAVE_DIR)

@app.route('/')
def home():
    # ? Render the home page with available regions.
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_plots():
    # ? API endpoint to generate plots based on form data.
    try:
        # Get form data
        region_code = request.form.get('region_code', 'BE1')
        
        # Calculate default dates if not provided
        today = datetime.now()
        default_end = today.strftime('%Y-%m-%d')
        default_start = (today - timedelta(days=30)).strftime('%Y-%m-%d')
        
        start_date = request.form.get('start_date', default_start)
        end_date = request.form.get('end_date', default_end)
        
        # Process the region data
        solar_data = process_region(region_code, start_date, end_date)
        
        if solar_data.plot_files:
            return jsonify({'success': True, 'plots': solar_data.plot_files})
        else:
            return jsonify({'success': False, 'error': 'No data available for the selected region and dates'})
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/graph')
def graph():
    # ? Display the graph page with available SVGs.
    # ? Get region code from query parameter, default to showing all
    region_code = request.args.get('region', None)
    dark_mode = request.args.get('dark', 'false').lower() == 'true'
    
    # ? List SVG files in the static/img directory
    svg_files = []
    if os.path.exists(SAVE_DIR):
        all_files = os.listdir(SAVE_DIR)
        # * Filter by region if specified
        if region_code:
            svg_files = [f for f in all_files if f.startswith(region_code) and f.endswith('.svg')]
        else:
            svg_files = [f for f in all_files if f.endswith('.svg')]  # Show all graphs by default
        
        # * Further filter by theme if needed
        if dark_mode:
            svg_files = [f for f in svg_files if '_dark' in f]
        else:
            svg_files = [f for f in svg_files if '_dark' not in f]
    
    # ? Get all unique region codes from filenames
    regions = set()
    for file in svg_files:
        if '_plot' in file:
            region = file.split('_plot')[0]
            regions.add(region)
    
    return render_template('graph.html', 
                            svg_files=svg_files, 
                            regions=sorted(regions),
                            selected_region=region_code,
                            dark_mode=dark_mode)

@app.route('/api/regions')
def list_regions():
    # ? API endpoint to list available regions with data.
    svg_files = []
    if os.path.exists(SAVE_DIR):
        svg_files = [f for f in os.listdir(SAVE_DIR) if f.endswith('.svg')]
    
    # ? Get unique region codes from filenames
    regions = set()
    for file in svg_files:
        if '_plot' in file:
            region = file.split('_plot')[0]
            regions.add(region)
    
    return jsonify(list(sorted(regions)))

@app.route('/static/img/<filename>')
def serve_svg(filename):
    # ? Serve SVG files from the static/img directory.
    return send_from_directory(SAVE_DIR, filename)

@app.route('/initialize')
def init_data_endpoint():
    # ? Generate initial data plots if none exist.
    svg_files = []
    if os.path.exists(SAVE_DIR):
        svg_files = [f for f in os.listdir(SAVE_DIR) if f.endswith('.svg')]
    
    # ? If no plots exist, generate default ones
    if not svg_files:
        results = initialize_data()
        return jsonify({'success': True, 'message': 'Default plots generated', 'plots': results})
    
    return jsonify({'success': True, 'message': 'Plots already exist'})

def before_first_request():
    # ? Initialize data before the first request.
    svg_files = []
    if os.path.exists(SAVE_DIR):
        svg_files = [f for f in os.listdir(SAVE_DIR) if f.endswith('.svg')]
    
    # ? If no plots exist, generate default ones
    if not svg_files:
        initialize_data()

if __name__ == "__main__":
    # ! Initialize data on startup
    before_first_request()
    
    # ? Run the Flask application
    app.run(debug=True)
