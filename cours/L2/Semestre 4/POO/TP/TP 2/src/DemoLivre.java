public class DemoLivre {
    public static void main(String[] args) {
        // Création d'un objet Livre
        Livre livre1 = new Livre("Les Miserables", "Victor Hugo", "Gallimard", 10, "littérature française");
        
        // Test des getters
        System.out.println("Titre: " + livre1.getTitre());
        System.out.println("Auteur: " + livre1.getAuteur());
        System.out.println("Éditeur: " + livre1.getEditeur());
        System.out.println("Nombre d'exemplaires: " + livre1.getNombreExemplaires());
        System.out.println("Genre: " + livre1.getGenre());

        // Test de la méthode ajouterExemplaires
        System.out.println("\nAjout de 5 exemplaires...");
        livre1.ajouterExemplaires(5);
        System.out.println("Nombre d'exemplaires après ajout: " + livre1.getNombreExemplaires());

        // Test de la méthode supprimerExemplaires
        System.out.println("\nSuppression d'un exemplaire...");
        livre1.supprimerExemplaires(1);
        System.out.println("Nombre d'exemplaires après suppression: " + livre1.getNombreExemplaires());

        // Test de la méthode estPresent
        System.out.println("\nLe livre est-il présent ? " + (livre1.estPresent() ? "Oui" : "Non"));

        // Test de la méthode equals
        Livre livre2 = new Livre("Les Miserables", "Victor Hugo", "Gallimard", 5, "littérature française");
        System.out.println("\nLes livres sont-ils identiques ? " + (livre1.equals(livre2) ? "Oui" : "Non"));

        // Test de la méthode nouvelEditeur
        System.out.println("\nCréation d'un nouveau livre avec un éditeur différent...");
        Livre livre3 = livre1.nouvelEditeur("Folio");
        livre3.toString();

        // Affichage des informations du livre
        System.out.println("\nInformations sur le livre original :");
        livre1.toString();
    }
}
