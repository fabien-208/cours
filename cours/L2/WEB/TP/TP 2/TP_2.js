function est_palindrome(mot) {
    let i = 0;
    let j = mot.lenght;
    while (i !== j) {
        if (mot[i] !== mot[j]) {
            return false;
        }
        i += 1;
        j -= 1;
    }
    return true;
}




function main() {
    console.log(est_palindrome("toto"));
    console.log(est_palindrome("SOS"));
    console.log(est_palindrome("radar"));

}

main();