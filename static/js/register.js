document.addEventListener('DOMContentLoaded', () => {
    const password = document.getElementById('password');
    const confirmPassword = document.getElementById('confirm_password');
    const passwordHints = document.getElementById('password-hints');
    const uppercaseHint = document.getElementById('uppercase');
    const lowercaseHint = document.getElementById('lowercase');
    const numberHint = document.getElementById('number');
    const specialHint = document.getElementById('special');

    const validatePassword = () => {
        const value = password.value;
        passwordHints.style.display = value.length > 0 ? 'block' : 'none'; // Show hints when typing

        // Check each condition
        uppercaseHint.classList.toggle('valid', /[A-Z]/.test(value));
        lowercaseHint.classList.toggle('valid', /[a-z]/.test(value));
        numberHint.classList.toggle('valid', /\d/.test(value));
        specialHint.classList.toggle('valid', /[!@#$%^&*()\-_=+]/.test(value));
    };

    password.addEventListener('input', validatePassword);

    document.getElementById('register-form').addEventListener('submit', (e) => {
        if (password.value !== confirmPassword.value) {
            e.preventDefault();
            alert('Passwords do not match!');
        }
    });
});
