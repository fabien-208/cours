public enum Couleur {
    PIQUE("\u2660"),
    COEUR("\u2665"),
    CARREAU("\u2666"),
    TREFLE("\u2663");

    private final String symbole;

    Couleur(String symbole) {
        this.symbole = symbole;
    }

    @Override
    public String toString() {
        return this.symbole;
    }
}
public enum Hauteur {
    DEUX(2, 2),
    TROIS(3, 3),
    QUATRE(4, 4),
    CINQ(5, 5),
    SIX(6, 6),
    SEPT(7, 7),
    HUIT(8, 8),
    NEUF(9, 9),
    DIX(10, 10),
    VALET(11, 11),
    DAME(12, 12),
    ROI(13, 13),
    AS(14, 14);

    private final int rang;
    private final int points;

    Hauteur(int rang, int points) {
        this.rang = rang;
        this.points = points;
    }

    public int getRang() {
        return this.rang;
    }

    @Override
    public String toString() {
        return this.name() + " (" + this.points + " points)";
    }
}

public class Carte {
    private final Hauteur hauteur;
    private final Couleur couleur;

    public Carte(Hauteur hauteur, Couleur couleur) {
        this.hauteur = hauteur;
        this.couleur = couleur;
    }

    public Hauteur getHauteur() {
        return hauteur;
    }

    public Couleur getCouleur() {
        return couleur;
    }

    @Override
    public String toString() {
        return hauteur.name() + couleur.toString();
    }
}