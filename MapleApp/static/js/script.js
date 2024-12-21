document.addEventListener('DOMContentLoaded', function () {
    // Handle Admin Login
    const adminLoginForm = document.querySelector('form[name="login"]');
    if (adminLoginForm) {
        adminLoginForm.addEventListener('submit', function (event) {
            event.preventDefault();
            const formData = new FormData(adminLoginForm);
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            fetch(adminLoginForm.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': csrfToken
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    window.location.href = data.redirect_url;
                } else {
                    alert(data.message);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Something went wrong. Please try again.');
            });
        });
    }

    // Handle Student Login
    const studentLoginForm = document.querySelector('form[name="login"]');
    if (studentLoginForm) {
        studentLoginForm.addEventListener('submit', function (event) {
            event.preventDefault();
            const formData = new FormData(studentLoginForm);
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            fetch(studentLoginForm.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': csrfToken
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    window.location.href = data.redirect_url;
                } else {
                    alert(data.message);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Something went wrong. Please try again.');
            });
        });
    }

    // Handle Feedback Submission
    const feedbackForm = document.querySelector('form[name="feedback"]');
    if (feedbackForm) {
        feedbackForm.addEventListener('submit', function (event) {
            event.preventDefault();
            const formData = new FormData(feedbackForm);
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            fetch(feedbackForm.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': csrfToken
                }
            })
            .then(response => response.json())
            .then(data => {
                alert(data.message);
                if (data.success) {
                    feedbackForm.reset();
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Something went wrong. Please try again.');
            });
        });
    }

    // Handle Registration
    const registrationForm = document.querySelector('form[name="registration"]');
    if (registrationForm) {
        registrationForm.addEventListener('submit', function (event) {
            event.preventDefault();
            const formData = new FormData(registrationForm);
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            fetch(registrationForm.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': csrfToken
                }
            })
            .then(response => response.json())
            .then(data => {
                alert(data.message);
                if (data.success) {
                    window.location.href = data.redirect_url;
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Something went wrong. Please try again.');
            });
        });
    }
});
