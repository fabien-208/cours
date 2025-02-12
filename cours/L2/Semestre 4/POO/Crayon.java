
public class Crayon {
    public final int quantité_base = 100;
    private String marque;
    private String couleur;
    private float prix;
    private int qte = quantité_base;
    private static final int quantité_max_base = 1000;   

    public Crayon (String marque, String couleur, float prix) {
        this.marque = marque;
        this.couleur = couleur;
        this.prix = (prix > 0 ? prix : -prix);
    }

    public Crayon (String marque, String couleur, float prix, int quantité) {
        this(marque, couleur, prix);
        if (quantité >= 0 && quantité <= quantité_max_base) {
            this.qte = quantité;
        }
    }

    public String get_marque() {
        return marque;
    }

    public float get_prix() {
        return prix;
    }

    public String get_couleur() {
        return couleur;
    }

    public int get_quantité() {
        return qte;
    }

    public float prix_du_lot() {
        return qte * prix;
    }


    public String toString() {
        return "Marque : " + marque + " Couleur : " + couleur + " Prix : " + prix + " quantité : " + qte;
    }
}

public class Commande {
    public static final int MAX_ACHATS = 100;
    private static int nbCommande = 0;

    private int numeroCommande;
    private Client papeterie;
    private String laDate;
    private Crayon[] achats = new Crayon[MAX_ACHATS];
    private int nbAchats;


    public Commande(Client client, String date) {
        this.papeterie = client;
        this.laDate = date;
        this.numeroCommande = ++nbCommande;
    }

    public Boolean ajouteNouveaucrayon( String couleur, String marque, float prix, int qte) {
        if (nbAchats < achats.length) {
            Crayon c = new Crayon(marque, couleur, qte, prix);
            achats[nbAchats++] = c;
            return True;
        }
        return False;
    }

    public Crayon getAchatCrayon( int indice) {
        if ((indice >= 0) && (indice < nbAchats)) {
            return achats[indice];
        }
        return null;
    }


    public boolean modifieAchat ( int indice, int qte) {
        if ((indice >= 0) && (indice <nbAchats) && (qte >= 0)){
            return achats[indice].setQte(qte);
        }
        return False;
    }

    public float coutTotal() {
        float cout = 0;
        for(int i = 0; i < nbAchats; i++) {
            cout += achats[i].get_prix()
        }
    }
}