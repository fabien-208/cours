import java.util.Arrays;
import java.util.Objects;

public class Livre {
    private final String titre;
    private final String auteur;
    private final String editeur;
    private int nombreExemplaires;
    private String genre;

    public static final String[] GENRES = {
        "littérature française", "littérature jeunesse", "littérature étrangère", 
        "policier", "politique", "sciences", "sciences humaines", "non spécifié"
    };

    public Livre(String titre, String auteur, String editeur, int nombreExemplaires, String genre) {
        if (!estGenreValide(genre)) {
            throw new IllegalArgumentException("Genre invalide. Veuillez choisir parmi : " + Arrays.toString(GENRES));
        }
        this.titre = titre;
        this.auteur = auteur;
        this.editeur = editeur;
        this.nombreExemplaires = nombreExemplaires;
        this.genre = genre;
    }

    private static boolean estGenreValide(String genre) {
        for (String g : GENRES) {
            if (g.equalsIgnoreCase(genre)) {
                return true;
            }
        }
        return false;
    }

    public String getTitre() {
        return titre;
    }

    public String getAuteur() {
        return auteur;
    }

    public String getEditeur() {
        return editeur;
    }

    public int getNombreExemplaires() {
        return nombreExemplaires;
    }

    public String getGenre() {
        return genre;
    }

    public void ajouterExemplaires(int nombre) {
        if (nombre < 0) {
            throw new IllegalArgumentException("Le nombre d'exemplaires à ajouter ne peut pas être négatif");
        }
        this.nombreExemplaires += nombre;
    }

    public void supprimerExemplaires(int nombre) {
        if (nombre < 0) {
            throw new IllegalArgumentException("Le nombre d'exemplaires à supprimer ne peut pas être négatif");
        }
        this.nombreExemplaires = Math.max(0, this.nombreExemplaires - nombre);
    }

    public boolean estPresent() {
        return this.nombreExemplaires > 0;
    }

    @Override
    public String toString() {
        return "Titre: " + this.titre + "\n" +
               "Auteur: " + this.auteur + "\n" +
               "Éditeur: " + this.editeur + "\n" +
               "Nombre d'exemplaires: " + this.nombreExemplaires + "\n" +
               "Genre: " + this.genre;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Livre autreLivre = (Livre) obj;
        return this.titre.equals(autreLivre.titre) && 
               this.auteur.equals(autreLivre.auteur) && 
               this.editeur.equals(autreLivre.editeur);
    }

    @Override
    public int hashCode() {
        return Objects.hash(titre, auteur, editeur);
    }

    public Livre nouvelEditeur(String nouvelEditeur) {
        return new Livre(this.titre, this.auteur, nouvelEditeur, 1, this.genre);
    }
}
