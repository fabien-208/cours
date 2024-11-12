function calcul() {
    let basePrice = 16400;
    let totalPrice = basePrice;

    let options = document.querySelectorAll('input[type="checkbox"]:checked');

    options.forEach(option => {
        totalPrice += parseFloat(option.value);
    });
    document.getElementById('totalPrice').textContent = `Total Price: $${totalPrice.toFixed(2)}`;
}