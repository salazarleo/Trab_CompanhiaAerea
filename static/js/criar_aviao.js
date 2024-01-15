document.addEventListener('DOMContentLoaded', function () {
    var backButton = document.querySelector('.back-button .btn-voltar');

    if (backButton) {
        backButton.addEventListener('click', function () {
            console.log(urlHome); // Verifique o valor no console
            window.location.href = urlHome;
        });
    }
});
