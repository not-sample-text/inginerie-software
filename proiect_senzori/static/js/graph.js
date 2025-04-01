// Region filter functionality
document.getElementById("apply-filter").addEventListener("click", function () {
	const regionSelect = document.getElementById("region-select");
	const selectedRegion = regionSelect.value;

	let url = "/graph";
	if (selectedRegion) {
		url += `?region=${selectedRegion}`;
	}

	window.location.href = url;
});
