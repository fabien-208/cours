import guilines.IJeuDesBilles;
import java.awt.Point;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class MonJeu implements IJeuDesBilles {
    private int[][] grille;
    private static final int TAILLE = 9; // Taille du plateau (9x9)
    private static final int NB_COULEURS = 3; // Nombre de couleurs utilisées (simplifié)
    private static final int VIDE = -1;
    private Random random;
    private List<Integer> nouvellesCouleurs; // Stocke les nouvelles couleurs après un déplacement

    public MonJeu() {
        grille = new int[TAILLE][TAILLE];
        random = new Random();
        nouvellesCouleurs = new ArrayList<>();
        initialiserGrille();
    }

    private void initialiserGrille() {
        for (int i = 0; i < TAILLE; i++) {
            for (int j = 0; j < TAILLE; j++) {
                grille[i][j] = VIDE;
            }
        }
        genererBilles(5); // Générer 5 billes au début
    }

    private void genererBilles(int nombre) {
        nouvellesCouleurs.clear();
        for (int i = 0; i < nombre; i++) {
            int x, y;
            do {
                x = random.nextInt(TAILLE);
                y = random.nextInt(TAILLE);
            } while (grille[x][y] != VIDE);
            int couleur = random.nextInt(NB_COULEURS);
            grille[x][y] = couleur;
            nouvellesCouleurs.add(couleur);
        }
    }

    public boolean deplace(int x1, int y1, int x2, int y2) {
        if (grille[x1][y1] != VIDE && grille[x2][y2] == VIDE) {
            grille[x2][y2] = grille[x1][y1];
            grille[x1][y1] = VIDE;
            genererBilles(3); // Ajouter 3 nouvelles billes après déplacement
            return true;
        }
        return false;
    }

    public List<Point> getDernieresModifications() {
        List<Point> modifications = new ArrayList<>();
        for (int i = 0; i < TAILLE; i++) {
            for (int j = 0; j < TAILLE; j++) {
                modifications.add(new Point(i, j));
            }
        }
        return modifications;
    }

    public List<Integer> getNouvellesCouleurs() {
        return nouvellesCouleurs;
    }
}
