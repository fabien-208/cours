
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
        res[i] = 0;
    }
    for (let num of tab) {
        if (num >= min && num < max) {
            res[num]++;
        }
    }
    
    return res;
}


function stats(tab, min, max) {
    let occ = occurences(tab, min, max);
    let total = tab.length;
    let res = {};
    for (let key in occ) {
        res[key] = occ[key] / total;
    }
    
    return res;
}





function excusotron(textArray) {
    return textArray.map(arr => arr[Math.floor(Math.random() * arr.length)]).join(' ');
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
    var pipoText1 = [["Ce matin,", "Tantôt,"], ["j'ai eu une panne"], ["de réveil.", "d'oreiller."]];
    console.log(excusotron(pipoText1));
    var pipoText2 = [ [ "Tôt dans la matinée,", "Vers 4h du matin,", "Hier soir,", "Tard dans la nuit,", "En pleine nuit," ], [ "alors que", "pendant que", "au moment où", "tandis que", "comme", "cependant que" ], [ "je dormais après avoir relu pour la 3ème fois la Comédie humaine de Balzac,", "je sommeillais en attendant de me lever pour mon footing quotidien de 5h du matin,", "je somnollais après avoir passé en revue une étude du Figaro Economique,", "je m'étais assoupi sur une des oeuvres passionnantes de Friedrich Wilheim Nietzsche,", "je me reposais après avoir pratiqué 2h intenses de Squash,", "je m'étais endormis sur un article fort intéressant du Herald Tribune,", "je faisais un somme après avoir fini de traduire Guerre & Paix en Mandarin,", "je m'étais assoupi sur la brillante émission 'Chasse et Pêche'," ], [ "mon chat", "mon chien", "ma vieille grand-mère", "mon perroquet", "mon sanglier domestique", "ma belle-mère", "mon iguane asthmatique" ], [ "a joué avec le fil électrique de", "s'est pris les pates dans le fil électrique de", "a appuyé par mégarde sur le bouton OFF de", "a effleuré par inadvertance le Snooze de", "a renversé du Coca sur", "a fait tomber dans la baignoire", "a rebooté" ], [ "mon radio-réveil qui n'a donc pas sonné, et ce n'est" ], [ "que lorsque les pompiers sont entrés en hurlant 'AU FEU!'", "qu'au moment où les huissiers (venus pour le voisin) ont enfoncé la porte", "qu'avec l'arrivée du SAMU, venu chercher ma grand-mère", "qu'après l'entrée fracassante de la SPA", "qu'au moment où les pompes-funèbres (venues chercher ma belle-mère) ont sonné à la porte", "que quand le plombier est venu réparer l'inondation", "qu'avec la visite d'un représentant du Téléthon venu me remercier pour mon généreux don de la veille" ], [ "que je me suis réveillé, trop en retard pour être à l'heure à la fac.", "que j'ai repris connaissance et me suis précipité tardivement à la fac.", "que j'ai réalisé qu'il était trop tard pour venir à la fac ce matin.", "que j'ai bondi hors de mon lit pour me ruer à la fac." ] ];
    console.log(excusotron(pipoText2));
}


main()




