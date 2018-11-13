const emailInput = document.getElementById('id_email');
const usernameInput = document.getElementById('id_username');

emailInput.addEventListener('change', (e) => {
	let parts = emailInput.value.split('@');
	if (parts.length == 1) {
		return;
	}

	usernameInput.value = parts[0];
});
