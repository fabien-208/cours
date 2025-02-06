import java.util.ArrayList;
import java.util.List;

public class Bibliobus {
    private String nom;
    private Livre[] catalogue;
    private int nombreLivres;

    public Bibliobus(String nom, int capaciteMax) {
        this.nom = nom;
        this.catalogue = new Livre[capaciteMax];
        this.nombreLivres = 0;
    }

    public String getNom() {
        return nom;
    }

    public Livre getLivreById(int id) {
        if (id >= 0 && id < nombreLivres) {
            return catalogue[id];
        }
        return null;
    }

    public void afficherLivreById(int id) {
        Livre livre = getLivreById(id);
        if (livre != null) {
            System.out.println(livre);
        } else {
            System.out.println("Livre non trouvé.");
        }
    }

    public void afficherCatalogue() {
        for (int i = 0; i < nombreLivres; i++) {
            System.out.println(catalogue[i] + "\n");
        }
    }

    public void afficherLivresPresents() {
        for (int i = 0; i < nombreLivres; i++) {
            if (catalogue[i].estPresent()) {
                System.out.println(catalogue[i] + "\n");
            }
        }
    }

    public void afficherLivresParGenre(String genre) {
        for (int i = 0; i < nombreLivres; i++) {
            if (catalogue[i].getGenre().equalsIgnoreCase(genre)) {
                System.out.println(catalogue[i]);
            }
        }
    }

    public boolean estLivreConnu(int id) {
        return id >= 0 && id < nombreLivres;
    }

    public boolean estLivrePresent(int id) {
        Livre livre = getLivreById(id);
        return livre != null && livre.estPresent();
    }

    public int nombreExemplaires(int id) {
        Livre livre = getLivreById(id);
        return livre != null ? livre.getNombreExemplaires() : 0;
    }

    public void retirerLivre(int id) {
        if (id >= 0 && id < nombreLivres) {
            catalogue[id] = catalogue[nombreLivres - 1];
            catalogue[nombreLivres - 1] = null;
            nombreLivres--;
        }
    }

    public boolean ajouterLivre(Livre livre) {
        if (nombreLivres < catalogue.length) {
            catalogue[nombreLivres] = livre;
            nombreLivres++;
            return true;
        }
        return false;
    }
}

