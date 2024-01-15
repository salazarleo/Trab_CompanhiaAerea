document.addEventListener('DOMContentLoaded', function () {
    var backButton = document.querySelector('.back-button .back-btn');

    if (backButton) {
        backButton.addEventListener('click', function () {
            window.location.href = urlHome;
        });
    }
});


