public class DemoBibliobus {
    public static void main(String[] args) {
        // Création du bibliobus avec une capacité de 5 livres
        Bibliobus bibliobus = new Bibliobus("Bibliobus Mobile", 5);

        // Création de quelques livres
        Livre livre1 = new Livre("1984", "George Orwell", "Secker & Warburg", 3, "littérature étrangère");
        Livre livre2 = new Livre("Le Petit Prince", "Antoine de Saint-Exupéry", "Gallimard", 5, "littérature jeunesse");
        Livre livre3 = new Livre("Sherlock Holmes", "Arthur Conan Doyle", "Penguin Books", 2, "policier");

        // Ajout des livres au bibliobus
        bibliobus.ajouterLivre(livre1);
        bibliobus.ajouterLivre(livre2);
        bibliobus.ajouterLivre(livre3);

        // Affichage du catalogue complet
        System.out.println("Catalogue du Bibliobus:");
        bibliobus.afficherCatalogue();

        // Test de l'affichage d'un livre par ID
        System.out.println("\nAffichage du livre avec ID 1:");
        bibliobus.afficherLivreById(1);

        // Test de l'affichage des livres présents
        System.out.println("\nLivres actuellement disponibles:");
        bibliobus.afficherLivresPresents();

        // Test de l'affichage par genre
        System.out.println("\nLivres du genre 'policier':");
        bibliobus.afficherLivresParGenre("policier");

        // Vérification si un livre est présent
        System.out.println("\nLe livre avec ID 1 est-il disponible? " + bibliobus.estLivrePresent(1));

        // Retrait d'un livre et vérification après suppression
        System.out.println("\nRetrait du livre avec ID 1.");
        bibliobus.retirerLivre(1);

        // Vérification si un livre est présent
        System.out.println("\nLe livre avec ID 1 est-il disponible? " + bibliobus.estLivrePresent(1));

        // Affichage du catalogue après suppression
        System.out.println("\nCatalogue après retrait:");
        bibliobus.afficherCatalogue();
    }
}
