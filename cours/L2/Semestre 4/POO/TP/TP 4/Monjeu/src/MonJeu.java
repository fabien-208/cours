import guilines.IJeuDesBilles;
import java.awt.Point;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Set;
import java.util.HashSet;

public class MonJeu implements IJeuDesBilles {
    
    private int[][] grille;
    private static final int TAILLE = 9; // Taille du plateau (9x9)
    private static final int NB_COULEURS = 8; // Nombre de couleurs utilisées
    private static final int VIDE = -1;
    private int score = 0;
    private Random random;
    private List<Integer> nouvellesCouleurs; // Stocke les nouvelles couleurs après un déplacement

    public MonJeu() {
        grille = new int[TAILLE][TAILLE];
        random = new Random();
        nouvellesCouleurs = new ArrayList<>();
        initialiserGrille();
    }

    public int getNbLignes() {
        return TAILLE;
    }

    public int getNbColonnes() {
        return TAILLE;
    }

    public int getCouleur(int x, int y) {
        return grille[x][y];
    }

    public int getScore() {
        return score;
    }

    public int getNbCouleurs() {
        return NB_COULEURS;
    }

    public boolean partieFinie() {
        for (int i = 0; i < TAILLE; i++) {
            for (int j = 0; j < TAILLE; j++) {
                if (grille[i][j] != VIDE) {
                    return false;
                }
            }
        }
        return true;
    }

    public int getNbBillesAjoutees() {
        return nouvellesCouleurs.size();
    }

    public void reinit() {
        score = 0;
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

    private List<Point> genererBilles(int nombre) {
        nouvellesCouleurs.clear();
        List<Point> nouvellesBilles = new ArrayList<>();
    
        for (int i = 0; i < nombre; i++) {
            int x, y;
            do {
                x = random.nextInt(TAILLE);
                y = random.nextInt(TAILLE);
            } while (grille[x][y] != VIDE); // Trouver une case vide
    
            int couleur = random.nextInt(NB_COULEURS);
            grille[x][y] = couleur;
            nouvellesCouleurs.add(couleur);
            nouvellesBilles.add(new Point(x, y)); // Ajouter la position de la nouvelle bille
        }
        return nouvellesBilles;
    }
    

    public List<Point> deplace(int x1, int y1, int x2, int y2) {
        List<Point> modifications = new ArrayList<>();
    
        if (grille[x1][y1] != VIDE && grille[x2][y2] == VIDE) {
            // Déplacement de la bille
            grille[x2][y2] = grille[x1][y1];
            grille[x1][y1] = VIDE;
            modifications.add(new Point(x1, y1));
            modifications.add(new Point(x2, y2));
    
            // Vérification et suppression des alignements
            check_point();
    
            // Génération de 3 nouvelles billes
            List<Point> nouvellesBilles = genererBilles(3);
            modifications.addAll(nouvellesBilles); // Ajouter les nouvelles billes à la liste des modifications
        }
        return modifications;
    }
    
    

    public List<Point> getDernieresModifications() {
        List<Point> modifications = new ArrayList<>();
        for (int i = 0; i < TAILLE; i++) {
            for (int j = 0; j < TAILLE; j++) {
                if (grille[i][j] != VIDE) {
                    modifications.add(new Point(i, j));
                }
            }
        }
        return modifications;
    }


    public int[] getNouvellesCouleurs() {
        return nouvellesCouleurs.stream().mapToInt(i -> i).toArray();
    }


    public boolean check_point() {
        Set<Point> aSupprimer = new HashSet<>();
    
        // Vérification horizontale (→)
        for (int i = 0; i < TAILLE; i++) {
            for (int j = 0; j <= TAILLE - 5; j++) {
                if (grille[i][j] != VIDE) {
                    ajouterBillesASupprimer(aSupprimer, i, j, 0, 1);
                }
            }
        }
    
        // Vérification verticale (↓)
        for (int i = 0; i <= TAILLE - 5; i++) {
            for (int j = 0; j < TAILLE; j++) {
                if (grille[i][j] != VIDE) {
                    ajouterBillesASupprimer(aSupprimer, i, j, 1, 0);
                }
            }
        }
    
    
        // Si aucune bille à supprimer, retourner false
        if (aSupprimer.isEmpty()) {
            return false;
        }    
        // Augmenter le score en fonction du nombre de billes supprimées
        score += aSupprimer.size() * 5; // 5 points par bille supprimée
        // Ajouter les points supprimés aux modifications
        for (Point p : aSupprimer) {
            System.out.println("Suppression : " + p); // Vérification
            grille[p.x][p.y] = VIDE; // Suppression effective
        }
    
        return true;
    }
    
    private void ajouterBillesASupprimer(Set<Point> liste, int x, int y, int dx, int dy) {
        int couleur = grille[x][y];
        List<Point> tempList = new ArrayList<>();
    
        for (int k = 0; k < 5; k++) {
            int nx = x + k * dx;
            int ny = y + k * dy;
            if (nx < 0 || ny < 0 || nx >= TAILLE || ny >= TAILLE || grille[nx][ny] != couleur) {
                return;  
            }
            tempList.add(new Point(nx, ny));
        }
        liste.addAll(tempList); // Ajouter toutes les billes détectées à la liste

    }
}
    