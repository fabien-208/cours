document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('form').addEventListener('submit', function(event) {
        var pseudo = document.getElementById('pseudo').value;
        var email = document.getElementById('email').value;
        var pseudoRegex = /^[a-zA-Z0-9]{8,25}$/;
        var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
        var isValid = true;

        if (!pseudoRegex.test(pseudo)) {
            document.getElementById('pseudo').classList.add('error');
            isValid = false;
            alert('Le pseudo doit contenir entre 8 et 25 caractères alphanumériques.');
            event.preventDefault();
        } else {
            document.getElementById('pseudo').classList.remove('error');
        }

        if (!emailRegex.test(email) || email.length > 25) {
            document.getElementById('email').classList.add('error');
            isValid = false;
            alert('L\'email doit contenir au maximum 25 caractères, un seul @ et un seul point avec au moins 2 caractères avant et après le point.'); 
            event.preventDefault();
        } else {
            document.getElementById('email').classList.remove('error');
        }

        if (isValid) {
            alert('Compte enregistré');
        }
    });
});
/*
document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('form').addEventListener('submit', function(event) {
    var pseudo = document.getElementById('pseudo').value;
    var email = document.getElementById('email').value;
    var pseudoRegex = /^[a-zA-Z0-9]{8,25}$/;
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
    var isValid = true;


    if (!pseudoRegex.test(pseudo)) {
        document.getElementById('pseudo').style.borderColor = 'red';
        isValid = false;
        event.preventDefault();
    } else if (!emailRegex.test(email) || email.length > 25) {
        document.getElementById('email').style.borderColor = 'red';
        isValid = false;
        event.preventDefault();
    };
    if (isValid) {
        alert('Compte enregistré');
    }
})});
*/