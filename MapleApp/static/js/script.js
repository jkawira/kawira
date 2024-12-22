document.addEventListener('DOMContentLoaded', function () {
    // Get CSRF token from cookies
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    const csrftoken = getCookie('csrftoken');

    // Handle Admin Login
    const adminLoginForm = document.querySelector('form[name="login"]');
    if (adminLoginForm) {
        adminLoginForm.addEventListener('submit', function (event) {
            event.preventDefault();
            const formData = new FormData(adminLoginForm);

            fetch(adminLoginForm.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': csrftoken
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

            fetch(studentLoginForm.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': csrftoken
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    window.location.href = data.redirect_url;  // Redirect to the index page
                } else {
                    alert(data.message);  // Show pop-up alert for error messages
                    if (data.errors) {
                        const errorMessages = JSON.parse(data.errors);
                        for (const field in errorMessages) {
                            errorMessages[field].forEach(error => {
                                alert(`${field}: ${error.message}`);  // Show pop-up alert for each error message
                            });
                        }
                    }
                }
            })
            .catch(error => {
                alert('Something went wrong. Please try again.');  // Show pop-up alert for fetch error
                console.error('Fetch error:', error);
            });
        });
    }

    // Handle Registration
    const registrationForm = document.querySelector('form[name="registration"]');
    if (registrationForm) {
        registrationForm.addEventListener('submit', function (event) {
            event.preventDefault();
            const formData = new FormData(registrationForm);

            fetch(registrationForm.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': csrftoken
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    window.location.href = data.redirect_url;  // Redirect to the confirmation page
                } else {
                    alert(data.message);  // Show pop-up alert for error messages
                    if (data.errors) {
                        const errorMessages = JSON.parse(data.errors);
                        for (const field in errorMessages) {
                            errorMessages[field].forEach(error => {
                                alert(`${field}: ${error.message}`);  // Show pop-up alert for each error message
                            });
                        }
                    }
                }
            })
            .catch(error => {
                alert('Something went wrong. Please try again.');  // Show pop-up alert for fetch error
                console.error('Fetch error:', error);
            });
        });
    }

    // Handle Feedback Submission
    const feedbackForm = document.querySelector('form[name="feedback"]');
    if (feedbackForm) {
        feedbackForm.addEventListener('submit', function (event) {
            event.preventDefault();
            const formData = new FormData(feedbackForm);

            fetch(feedbackForm.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': csrftoken
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
});
