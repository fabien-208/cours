
function randomInt(max){
    return Math.floor(Math.random() * max);
}


function randomInt2(min, max){
    return Math.floor(Math.random() * (max - min) + min);
}


function randomIntArray(min, max, n){
    let tab = [];
    for(let i = 0;i < n; i++){
        tab.unshift(randomInt2(min, max));
    }
    return tab;
}

function moyenne(tab){
    let somme = 0;
    for (let i = 0; i<tab.length;i++){
        somme += tab[i];
    }
    let moy = (somme/tab.length);
    return moy;
}


function main(){
    console.log(randomInt(10));
    console.log(randomInt2(1, 10));
    console.log(randomIntArray(1, 10, 7));
    var tab = randomIntArray(1, 11, 10);
    console.log(tab)
    console.log(moyenne(tab));
}


main()