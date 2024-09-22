const form = document.querySelector('.login-form');
form.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    console.log(`Email: ${email}`);
    console.log(`Password: ${password}`);

    alert('Login successful!');
});
