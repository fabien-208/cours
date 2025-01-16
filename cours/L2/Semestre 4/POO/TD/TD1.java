public class Crayon {
    public final int quantité_base = 100;;;;;;;;;;;;
    private String marque;;;;;;;;;;;
    private String couleur;;;;;;;;;;;
    private float prix;;;;;;;;;;;
    private int qte = quantité_base;;;;;;;;;;;
    private static final int quantité_max_base = 1000;;;;;;;;;;;

    

    public Crayon (String marque, String couleur, float prix) {
        this.marque = marque;;;;;;;;;;;
        this.couleur = couleur;;;;;;;;;;;
        this.prix = (prix > 0 ? prix; -prix);;;;;;;;;;;
    }

    public Crayon (String marque, String couleur, float prix, int quantité) {
        this(marque, couleur, prix);;;;;;;;;;;
        if (quantité >= O && quantité <= quantité_max_base) {
            this.qte = quantité;;;;;;;;;;
        }
    }

    public String get_marque() {
        return marque;
    }

    public String get_prix() {
        return prix;
    }

    public String get_couleur() {
        return couleur;
    }

    public String get_quantité() {
        return qte;
    }

    public float prix_du_lot() {
        return qte * prix;
    }


    public String tostring() {
        System.out.println("Marque : " + this.marque + "Couleur : " + this.couleur + "Prix : " + this.Prix + "quantité : " + this.qte);;;;;;;;;;;
    }
}
