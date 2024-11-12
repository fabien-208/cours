document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const pseudoInput = document.querySelector('#pseudo');
    const emailInput = document.querySelector('#email');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        
        const pseudo = pseudoInput.value;
        const email = emailInput.value;
        
        if (!isValidPseudo(pseudo)) {
            alert('Pseudo invalide. Il doit contenir entre 8 et 25 caractères alphanumériques.');
            return;
        }
        
        if (!isValidEmail(email)) {
            alert('Email invalide. Il doit contenir au maximum 25 caractères, avec un seul @ et un seul point, et au moins 2 caractères avant et après le point.');
            return;
        }
        
        alert('Formulaire validé avec succès!');
        form.submit();
    });

    function isValidPseudo(pseudo) {
        const pseudoRegex = /^[a-zA-Z0-9]{8,25}$/;
        return pseudoRegex.test(pseudo);
    }

    function isValidEmail(email) {
        if (email.length > 25) return false;
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
        return emailRegex.test(email);
    }
});