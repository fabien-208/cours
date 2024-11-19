
// exercice 1

function maxi(n, m) {

    if (n > m) {
        return n;
    }
    return m;
}

// exercice 2


function abs(n) {

    if (n <= 0) {
        return n * (-1);
    }
    return n;
}

// exercice 3
// question 1

function harm(n) {

    let somme = 0;
    let i = 1;
    while (i < n) {
        if (i === 1) {
            somme += 1;
        } else {
            somme += (1 / i);
        }
        i += 1;
    }
    return somme;
}

// quesion 2

function harmAlt(n) {

    let somme = -1;
    let i = 2;
    while (i < n) {
        if (i === 1) {
            somme -= 1;
        } else {
            if (i % 2 === 0) {
                somme += (1 / i);
            } else {
                somme -= (1 / i);
            }
        }
        i += 1;
    }
    return somme;
}

//question 3

function nblterHarmAlt(epsilon) {

    let somme = -1;
    let i = 1;
    let ln = Math.log(2);
    while ((abs(ln + somme)) < epsilon) {
    
        if (i % 2 === 0) {
            somme += (1 / i);
        } else {
            somme -= (1 / i);
        }
        i += 1;
    }
    return i;
}


// exerice 4

function celsiusToFahreinheit(n, m) {
    let i = 0;
    while (i < n) {
        let far = (9 * i) / 5 + 32;
        console.log(i + " Degrés Celsius = " + far + " Degrés Fahreinheit");
        i += m;
    }

}



function main() {

    console.log(maxi(2, 3));
    console.log(maxi(2, 2));
    console.log(maxi(2, -2));
    console.log(abs(-4));
    console.log(abs(-0));
    console.log(abs(3.14));
    console.log(harm(0));
    console.log(harm(1));
    console.log(harm(100));
    console.log(harm(1000));
    console.log(harmAlt(0));
    console.log(harmAlt(1));
    console.log(harmAlt(1000));
    console.log(harmAlt(100000));
    console.log(nblterHarmAlt(1));
    console.log(nblterHarmAlt(0.1));
    console.log(nblterHarmAlt(0.001));
    console.log(nblterHarmAlt(0.00001));
    celsiusToFahreinheit(20, 1);
}

main();