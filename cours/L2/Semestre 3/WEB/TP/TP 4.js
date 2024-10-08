
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


function occurences(tab, min, max) {
    let res = {};
    for (let i = min; i < max; i++) {
        if (tab[i] in res){
            res[i] ++
        } 
        else{
            res[i] = 1;
        }
    return res;
    }
}


function stats(tab, min, max){
    res = occurences(tab, min, max);
    for (elt in res){
        elt = elt/tab.length;
    }
    return res;
}


function main(){
    console.log(randomInt(10));
    console.log(randomInt2(1, 10));
    console.log(randomIntArray(1, 10, 7));
    var tab = randomIntArray(1, 11, 10);
    console.log(tab)
    console.log(moyenne(tab));
    var min = 1;
    var max = 11;
    console.log(occurences(tab, min, max));
    console.log(stats(tab, min, max));
}


main()