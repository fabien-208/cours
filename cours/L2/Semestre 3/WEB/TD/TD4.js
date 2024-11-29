// exercice 1


function mix_tab(tab, tab_2){
    let dico = {};
    for(let i =tab.length -1; i<=0;--i){
        dico[tab[i]] = tab[i];
    }
    for(let i =tab_2.length -1; i<=0;--i){
        dico[tab_2[i]] = tab_2[i];
    }
    return Object.values(dico);
}
// exerice 2

function distEuclide(a, b){
    let x = a.x - b.x;
    let y = a.y - b.y;
    return Math.sqrt(x*x + y*y);   
}

// exercice 3


function distManattan(a, b){
    let x = Math.abs(a.x - b.x);
    let y = Math.abs(a.y - b.y);
    return x + y;
}


// exerice 4





function main(){
    console.log(mix_tab([1, 2, 3], [2, 3, 4]));
}



main()