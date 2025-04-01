// Set default date values (current month)
document.addEventListener("DOMContentLoaded", function () {
	const today = new Date();
	const endDate = today.toISOString().split("T")[0];
	document.getElementById("end_date").value = endDate;

	// Set start date to 30 days ago
	const startDate = new Date();
	startDate.setDate(today.getDate() - 30);
	document.getElementById("start_date").value = startDate
		.toISOString()
		.split("T")[0];

	// Load available regions
	loadRegions();
});

// Form submission
document
	.getElementById("generate-form")
	.addEventListener("submit", function (e) {
		e.preventDefault();
		const formData = new FormData(this);
		const loadingDiv = document.getElementById("loading");
		const messageDiv = document.getElementById("message");

		loadingDiv.style.display = "block";
		messageDiv.style.display = "none";

		fetch("/generate", {
			method: "POST",
			body: formData
		})
			.then((response) => response.json())
			.then((data) => {
				loadingDiv.style.display = "none";
				messageDiv.style.display = "block";

				if (data.success) {
					messageDiv.className = "message success";
					messageDiv.textContent = "Plots generated successfully!";

					// Add view links
					const region = document.getElementById("region_code").value;
					const viewLink = document.createElement("p");
					viewLink.innerHTML = `<a href="/graph?region=${region}" class="view-button">View ${region} Graphs</a>`;
					messageDiv.appendChild(viewLink);

					// Refresh regions list
					loadRegions();
				} else {
					messageDiv.className = "message error";
					messageDiv.textContent =
						data.error || "An error occurred while generating plots.";
				}
			})
			.catch((error) => {
				loadingDiv.style.display = "none";
				messageDiv.style.display = "block";
				messageDiv.className = "message error";
				messageDiv.textContent =
					"An error occurred while communicating with the server.";
				console.error("Error:", error);
			});
	});

// Initialize default data
document.getElementById("init-data").addEventListener("click", function (e) {
	e.preventDefault();
	const loadingDiv = document.getElementById("loading");
	const messageDiv = document.getElementById("message");

	loadingDiv.style.display = "block";
	messageDiv.style.display = "none";

	fetch("/initialize")
		.then((response) => response.json())
		.then((data) => {
			loadingDiv.style.display = "none";
			messageDiv.style.display = "block";

			if (data.success) {
				messageDiv.className = "message success";
				messageDiv.textContent = data.message;

				const viewLink = document.createElement("p");
				viewLink.innerHTML = `<a href="/graph" class="view-button">View All Graphs</a>`;
				messageDiv.appendChild(viewLink);

				// Refresh regions list
				loadRegions();
			} else {
				messageDiv.className = "message error";
				messageDiv.textContent = data.error || "An error occurred.";
			}
		})
		.catch((error) => {
			loadingDiv.style.display = "none";
			messageDiv.style.display = "block";
			messageDiv.className = "message error";
			messageDiv.textContent =
				"An error occurred while communicating with the server.";
			console.error("Error:", error);
		});
});

// Load available regions
function loadRegions() {
	const regionsContainer = document.getElementById("regions-container");
	regionsContainer.textContent = "Loading...";

	const isDarkMode = window.matchMedia("(prefers-color-scheme: dark)").matches;

	fetch("/api/regions")
		.then((response) => response.json())
		.then((regions) => {
			if (regions.length === 0) {
				regionsContainer.innerHTML =
					"<p>No regions available. Generate some data first.</p>";
				return;
			}

			let html = '<div style="display: flex; flex-wrap: wrap; gap: 10px;">';

			regions.forEach((region) => {
				const graphMode = isDarkMode ? "dark" : "light";
				html += `
                        <div style="background: var(--border-color); padding: 15px; border-radius: 8px; min-width: 150px;">
                            <h3>${region}</h3>
                            <p>
                                <a href="/graph?region=${region}&mode=${graphMode}" class="view-button">View Graphs</a>
                            </p>
                        </div>
                    `;
			});

			html += "</div>";
			regionsContainer.innerHTML = html;
		})
		.catch((error) => {
			regionsContainer.innerHTML = "<p>Error loading regions.</p>";
			console.error("Error:", error);
		});
}
