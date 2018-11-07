const collapseFilterButton = document.getElementById('filter-collapse');
const collapseFilterButtonLabel = document.getElementById('filter-collapse-label');
const tableFilterContent =  document.getElementById('table-filters');
const clearFilterButton = document.getElementById('clear-filters');
const tableFilterForm = document.getElementById('table-filter-form');

collapseFilterButton.addEventListener('click', function() {
	var isCollapsed = !tableFilterContent.classList.contains('show');

	collapseFilterButtonLabel.innerText = isCollapsed ? 'Show' : 'Hide';
});


clearFilterButton.addEventListener('click', function() {
	tableFilterForm.querySelector('input').forEach(input => {
		input.value = '';
	});

	tableFilterForm.submit();
});
