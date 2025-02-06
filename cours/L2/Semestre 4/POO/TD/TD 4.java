// author : moi :)
// Date: 18.03.2020

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
