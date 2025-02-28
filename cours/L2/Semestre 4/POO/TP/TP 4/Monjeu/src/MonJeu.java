import guilines.IJeuDesBilles;
import java.awt.Point;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Set;
import java.util.HashSet;


public class MonJeu implements IJeuDesBilles {
    
    private int[][] grille; // Grille de jeu
    private static final int TAILLE = 9; // Taille du plateau (9x9)
    private static final int NB_COULEURS = 8; // Nombre de couleurs utilisées
    private static final int VIDE = -1; // Valeur pour une case vide
    private int score = 0; // initialise le score
    private Random random; // Générateur de nombres aléatoires
    private List<Integer> nouvellesCouleurs; // Liste des couleurs des prochaines billes

    public MonJeu() {
        grille = new int[TAILLE][TAILLE]; // Création de la grille
        random = new Random(); // Initialisation du générateur de nombres aléatoires
        nouvellesCouleurs = new ArrayList<>(); // Initialisation de la liste des couleurs
        initialiserGrille(); // Initialisation de la grille
    }

    public int getNbLignes() { // renvoie le nombre de lignes
        return TAILLE;
    }

    public int getNbColonnes() { // renvoie le nombre de colonnes
        return TAILLE;
    }

    public int getCouleur(int x, int y) { // renvoie la couleur de la bille
        return grille[x][y];
    }

    public int getScore() { // renvoie le score
        return score;
    }

    public int getNbCouleurs() { // renvoie le nombre de couleurs
        return NB_COULEURS;
    }

    public boolean partieFinie() { // renvoie si la partie est finie
        for (int i = 0; i < TAILLE; i++) {
            for (int j = 0; j < TAILLE; j++) {
                if (grille[i][j] == VIDE) {
                    return false;
                }
            }
        }
        return true;
    }

    public int getNbBillesAjoutees() { // renvoie le nombre de billes ajoutées
        return nouvellesCouleurs.size();
    }

    public void reinit() { // réinitialise le jeu
        score = 0;
        initialiserGrille();
    }

    private void initialiserGrille() { // initialise la grille
        for (int i = 0; i < TAILLE; i++) {
            for (int j = 0; j < TAILLE; j++) {
                grille[i][j] = VIDE;
            }
        }
        for (int i = 0; i < 3; i++) {
            nouvellesCouleurs.add(random.nextInt(NB_COULEURS));
        }
        genererBilles(5); // ajoute 5 billes au début
    }

    private List<Point> genererBilles(int nombre) { // pose des billes sur la grille
        List<Point> nouvellesBilles = new ArrayList<>();
        for (int i = 0; i < nombre; i++) {
            int x, y;
            if (partieFinie()) {
                System.out.println("Partie finie");
                break;
            } else {
                do {
                    x = random.nextInt(TAILLE);
                    y = random.nextInt(TAILLE);
                } while (grille[x][y] != VIDE); // Trouver une case vide
            }
            int couleur = nouvellesCouleurs.remove(0); // Prendre la première couleur de la liste
            grille[x][y] = couleur; // Pose la bille
            nouvellesCouleurs.add(random.nextInt(NB_COULEURS)); // Ajouter une nouvelle couleur
            nouvellesBilles.add(new Point(x, y)); // Ajouter la position de la nouvelle bille
            check_point(); // Vérification des alignements
        }
        return nouvellesBilles;
    }
    
    public List<Point> deplace(int x1, int y1, int x2, int y2) { // déplace une bille
        List<Point> modifications = new ArrayList<>();
    
        if (grille[x1][y1] != VIDE && grille[x2][y2] == VIDE) {
            // Déplacement de la bille
            grille[x2][y2] = grille[x1][y1];
            grille[x1][y1] = VIDE;
            modifications.add(new Point(x1, y1));
            modifications.add(new Point(x2, y2));
            if (check_point()){ // Vérification et suppression des alignements
                List<Point> nouvellesBilles = genererBilles(3); // Génération de 3 nouvelles billes
                modifications.addAll(nouvellesBilles); // Ajouter les nouvelles billes à la liste des modifications
            }
        }
        return modifications;
    }
    
    public List<Point> getDernieresModifications() { // renvoie les dernières modifications
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

    public int[] getNouvellesCouleurs() { // renvoie les nouvelles couleurs
        return nouvellesCouleurs.stream().mapToInt(i -> i).toArray();
    }

    public boolean check_point() { // Vérifie les alignements et supprime les billes
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
        // Si aucune bille à supprimer, retourner true
        if (aSupprimer.isEmpty()) {
            return true;
        }    
    
        score += aSupprimer.size() * 5; // Ajoute 5 points par bille supprimée
        //afficherGrille();
        // Supprimer les billes de la grille
        for (Point p : aSupprimer) {
            System.out.println("Suppression : " + p); // Vérification
            grille[p.x][p.y] = VIDE; // Suppression effective
        }
        //afficherGrille();

        // Retourner false pour indiquer qu'un alignement a été supprimé
        return false;
    }
    
    private void ajouterBillesASupprimer(Set<Point> liste, int x, int y, int dx, int dy) { // ajoute les billes à supprimer
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
    

/*
    private void afficherGrille() {
        for (int i = 0; i < TAILLE; i++) {
            for (int j = 0; j < TAILLE; j++) {
                System.out.print(grille[i][j] + "\t");
            }
            System.out.println();
        }
        System.out.println("--------------------------------------------");
    }
*/
    
}
    