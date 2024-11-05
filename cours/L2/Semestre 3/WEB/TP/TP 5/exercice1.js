
// Exercice 1

function infoPopup() {
    var nom_navigateur = navigator.appName;
    var version_navigateur = navigator.appVersion;
    var platforme = navigator.platform;
    var user_Agent = navigator.userAgent;

    alert("Nom du navigateur: " + nom_navigateur + "\n" +
          "Version du navigateur: " + version_navigateur + "\n" +
          "Plateforme: " + platforme + "\n" +
          "User Agent: " + user_Agent);
    }




function main() {
    console.log("Exercice 1");
    infoPopup();
}


main();