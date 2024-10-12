function codeCesar(msg, key) {
    const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    let resultat = '';
    for (let i = 0; i < msg.length; i++) {
        let caractere = msg[i].toUpperCase();
        if (alphabet.includes(caractere)) {
            let index = alphabet.indexOf(caractere);
            let nouveauIndex = (index + key) % 26;
            if (nouveauIndex < 0) {
                nouveauIndex += 26;
            }
            resultat += alphabet[nouveauIndex];
        }
    }

    return resultat;
}


function decodeCesar(msg, key) {
    const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    let resultat = '';
    for (let i = 0; i < msg.length; i++) {
        let caractere = msg[i].toUpperCase();
        if (alphabet.includes(caractere)) {
            let index = alphabet.indexOf(caractere);
            let nouveauIndex = (index - key) % 26;
            if (nouveauIndex < 0) {
                nouveauIndex += 26;
            }

            resultat += alphabet[nouveauIndex];
        }
    }
    return resultat;
}

function codeCesar2(msg, key) {
    const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    let resultat = '';
    for (let i = 0; i < msg.length; i++) {
        let caractere = msg[i].toUpperCase();
        if (alphabet.includes(caractere)) {
            let index = alphabet.indexOf(caractere);
            let nouveauIndex = (index + key) % 26;
            if (nouveauIndex < 0) {
                nouveauIndex += 26;
            }

            resultat += alphabet[nouveauIndex];
        } else {
            resultat += caractere;
        }
    }

    return resultat;
}


function decodeCesar2(msg, key) {
    const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    let resultat = '';
    for (let i = 0; i < msg.length; i++) {
        let caractere = msg[i].toUpperCase();
        if (alphabet.includes(caractere)) {
            let index = alphabet.indexOf(caractere);
            let nouveauIndex = (index - key) % 26;
            if (nouveauIndex < 0) {
                nouveauIndex += 26;
            }

            resultat += alphabet[nouveauIndex];
        } else {
            resultat += caractere;
        }
    }
    return resultat;
}




function codeCesar3(msg, key) {
    const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    let resultat = '';
    for (let i = 0; i < msg.length; i++) {
        let caractere = msg[i].toUpperCase();
        if (alphabet.includes(caractere)) {
            let index = alphabet.indexOf(caractere);
            let nouveauIndex = (index + key) % 26;
            if (nouveauIndex < 0) {
                nouveauIndex += 26;
            }

            resultat += alphabet[nouveauIndex];
        } else {
            resultat += caractere;
        }
    }

    return resultat;
}


function decodeCesar3(msg, key) {
    const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    let resultat = '';
    for (let i = 0; i < msg.length; i++) {
        let caractere = msg[i].toUpperCase();
        if (alphabet.includes(caractere)) {
            let index = alphabet.indexOf(caractere);
            let nouveauIndex = (index - key) % 26;
            if (nouveauIndex < 0) {
                nouveauIndex += 26;
            }

            resultat += alphabet[nouveauIndex];
        } else {
            resultat += caractere;
        }
    }
    return resultat;
}



function codeSubstitution(msg, key) {
    const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    let resultat = '';
    for (let i = 0; i < msg.length; i++) {
        let caractere = msg[i];

        if (alphabet.includes(caractere)) {
            let index = alphabet.indexOf(caractere);
            resultat += key[index];
        } else {
            resultat += caractere;
        }
    }

    return resultat;
}






function decodeSubstitution(msg, key) {
    const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    let resultat = '';
    for (let i = 0; i < msg.length; i++) {
        let caractere = msg[i];

        if (key.includes(caractere)) {
            let index = key.indexOf(caractere);
            resultat += alphabet[index];
        } else {
            resultat += caractere;
        }
    }

    return resultat;
}





function main(){
    console.log(codeCesar("COUCOU", 3)); // FRXFRX
    console.log(codeCesar('ZORRO', 3));    // 'CRUUR'
    console.log(decodeCesar('CRUUR', 3)); // 'ZORRO')
    console.log(codeCesar('COUCOU TOUT LE MONDE', 3)); // 'FRXFRX WRXW OH PRQGH'
    console.log(decodeCesar2('FRXFRX WRXW OH PRQGH', 3)); // 'COUCOU TOUT LE MONDE'
    console.log(codeCesar3('COUCOU, TOUT LE MONDE !', 3, ', !')); // 'FRXFRX, WRXW OH PRQGH !'
    console.log(decodeCesar3('FRXFRX, WRXW OH PRQGH !', 3, ', !')); // 'COUCOU, TOUT LE MONDE !'
    console.log(codeSubstitution('CECI EST UN TEST', 'AZERTYUIOPQSDFGHJKLMWXCVBN')); // ETEO TLM WF MTLM
    console.log(decodeSubstitution('&"&! "¨ù `_ @`ù^" ù"¨ù', '@#&é"(§è!çà)-_$*€^¨ù`£=+:/')); // 'CECI EST UN AUTRE TEST'
}



main()