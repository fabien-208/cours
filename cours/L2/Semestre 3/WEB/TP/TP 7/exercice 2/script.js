document.addEventListener('DOMContentLoaded', () => {
    const submitButton = document.getElementById('submitButton');
    submitButton.addEventListener('click', (event) => {
        calcul();
    });
});

function calcul() {
    let basePrice = 16400;
    let totalPrice = basePrice;

    let options = document.querySelectorAll('input[type="checkbox"]:checked');

    options.forEach(option => {
        let optionValue = parseFloat(option.value);
        if (!isNaN(optionValue)) {
            totalPrice += optionValue;
        }
    });
    document.getElementById('totalPrice').textContent = `Total Price: $${totalPrice}`;
}