// author : moi :)
// Date: 18.03.2020

import java.lang.classfile.AnnotationValue.OfEnum;

public interface Aliment {
    public String getNom();
    public int getPoids();
    public int getCalories();
}


public class chocolat implements Aliment {
    public final static String nom = "Chocolat";
    public final static int nb_cal_par_gr = 5;
    private int poids;
    private int calories;

    chocolat (int poids) {
        this.poids = poids;
        this.calories = poids * nb_cal_par_gr;
    }
    public int getCalories() {
        return calories;
    }

    public int getPoids() {
        return poids;
    }

    public String geString() {
        return nom;
    }

    public String StringtoString() {
        return (getNom() + "- Poids : " +getPoids() + "gr. - Calories : " + getCalories() + "cal.");
    }
}


public class Beurre implements Aliment {
    public final static String nom = "Beurre";
    public final static int nb_cal_par_gr = 7;
    private int poids ;
    private int calories;
    private boolean demi_sel;

    Beurre(int poids, boolean demi_sel) {
        this.poids = poids;
        this.calories = poids * nb_cal_par_gr;
        this.demi_sel = demi_sel;
    }

    public int getCalories() {
        return calories;
    }

    public String getNom() {
        return nom;
    }

    public int getPoids() {
        return poids;
    }

    public String StringtoString() {
        if (demi_sel) {
            return (getNom() + " demi-sel - Poids : " +getPoids() + "gr. - Calories : " + getCalories() + "cal.");
        } else {
            return (getNom() + " doux - Poids : " +getPoids() + "gr. - Calories : " + getCalories() + "cal.");
        }
    }
}


public class oeuf {
    
    public static final String nom = "Oeuf";
    public static final int nb_cal_par_gr = 87;
    public static final int poids_par_oeuf = 60;
    private int poids;
    private int calories;
    private int quantité;
    

    Oeuf (int quantité) {
        this.poids = quantité * poids_par_oeuf;
        this.quantité = quantité;
        this.calories = quantité * nb_cal_par_gr;
    }

    public String getnom() {
        return nom;
    }

    public int getPoids() {
        return poids;
    }

    public int getCalories() {
        return calories;
    }

    public getquantité() {
        return quantité;
    }

    public String StringtoString() {
        return (getNom() + " - Quantité : " + getquantité() + " - Calories : " + getCalories() + "cal.");
    }
}
