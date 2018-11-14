const collapseFilterButton = document.getElementById('filter-collapse');
const collapseFilterButtonLabel = document.getElementById('filter-collapse-label');
const tableFilterContent =  document.getElementById('table-filters');
const clearFilterButton = document.getElementById('clear-filters');
const tableFilterForm = document.getElementById('table-filter-form');

collapseFilterButton.addEventListener('click', function() {
	var hasShow = !tableFilterContent.classList.contains('show');

	collapseFilterButtonLabel.innerText = hasShow ? 'Hide' : 'Show';
});


clearFilterButton.addEventListener('click', function() {
	tableFilterForm.querySelectorAll('input').forEach(input => {
		input.value = '';
	});

	tableFilterForm.submit();
});
