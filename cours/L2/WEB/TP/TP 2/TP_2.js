function est_palindrome(mot) {
    let i = 0;
    let j = mot.length - 1;
    while (i <= j) {
        if (mot[i] !== mot[j]) {
            return false;
        }
        i += 1;
        j -= 1;
    }
    return true;
}

function est_palindrome2 (phrase) {
    let i = 0;
    let j = phrase.length - 1;
    let not_car = ['.', ',', '?', ':', ';', '!'];
    while (i <= j) {
        if (phrase[i] in not_car) {
            i++;
        }
        if (phrase[j] in not_car) {
            j--;
        }
        if (phrase[i] !== phrase[j]) {
            return false;
        }
        i += 1;
        j -= 1;
    }
    return true;

}


function compteMots (phrase) {
    let i = 0;
    let nb_mot = 0;
    while( i < phrase.length -1 ) {
        if (phrase[i] === ' ' && phrase[i+1] !== ' ') {
            nb_mot ++;
        } 
        i++;
    }
    if (phrase[-1] !== ' ') {
        nb_mot ++
}
    return nb_mot
}


function compteMots2 (phrase) {
    let i = 0;
    let nb_mot = 0;
    while(phrase[i] === ' ') {
        i++
    }
    while( i < phrase.length -1 ) {
        if (phrase[i] === ' ' && phrase[i+1] !== ' ') {
            nb_mot ++;
        } 
        i++;
    }
    if (phrase[-1] !== ' ') {
        nb_mot ++
    }
    return nb_mot
}


function compteMots3 (phrase) {
    let i = 0;
    let nb_mot = 0;
    let not_car = ['.', ',', '?', ':', ';', '!', "'"];
    while(phrase[i] === ' ') {
        i++
    }
    while( i < phrase.length -1 ) {
        if (phrase[i] in not_car){
            i++;
    }
        if (phrase[i] === ' ' && phrase[i+1] !== ' ') {
            nb_mot ++;
        } 
        i++;
    }
    if (phrase[-1] !== ' '){
        nb_mot ++;
    }
    if (phrase[-1] in not_car){
        nb_mot --;
    }
    return nb_mot;
}

function main() {
    console.log(est_palindrome("toto")); // false
    console.log(est_palindrome("SOS")); // true
    console.log(est_palindrome("radar")); // true 
    console.log(est_palindrome2('esope reste elu par cette crapule et se repose')); // true
    console.log(est_palindrome2('Eh ca va la vache ?')); //true
    console.log(compteMots('la maman de Colette et de Daniel')); // 7
    console.log(compteMots2(' la maman    de Colette et de   Daniel  ')); // 7
    console.log(compteMots2('Ceci, mais oui, est une phrase !', ' !,')); // 6

}

main();