import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import Carte;

public class Jeu {
    private List<Carte> jeuDeCartes;

    public Jeu() {
        jeuDeCartes = new ArrayList<>();
        String[] couleurs = {"Coeur", "Carreau", "Trèfle", "Pique"};
        String[] valeurs = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi", "As"};

        for (String couleur : Carte.COULEURS) {
            for (String valeur : Carte.VALEURS) {
                jeuDeCartes.add(new Carte(couleur, valeur));
            }
        }
        Collections.shuffle(jeuDeCartes);
    }

    public void afficheJeu() {
        for (Carte carte : jeuDeCartes) {
            System.out.println(carte);
        }
    }

    public static void main(String[] args) {
        Jeu jeu = new Jeu();
        jeu.afficheJeu();
    }
}

class Carte {
    private String couleur;
    private String valeur;

    public Carte(String couleur, String valeur) {
        this.couleur = couleur;
        this.valeur = valeur;
    }

    @Override
    public String toString() {
        return valeur + " de " + couleur;
    }
}