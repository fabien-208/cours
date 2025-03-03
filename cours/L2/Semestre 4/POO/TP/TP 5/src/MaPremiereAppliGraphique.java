import javax.swing.*;
import java.awt.event.*;

public class MaPremiereAppliGraphique {
    // Tableau des images
    private static final String[] TABIMAGES = {
        "images/Bird.gif", "images/Bird2.gif", "images/Cat.gif",
        "images/Cat2.gif", "images/Dog.gif", "images/Rabbit.gif", "images/Pig.gif"
    };

    public static void main(String[] args) {
        // Création de la fenêtre
        JFrame fenetre = new JFrame("Les images");
        fenetre.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        fenetre.setSize(300, 300);

        // Création du bouton avec la première image
        JButton leBtn = new JButton(new ImageIcon(TABIMAGES[0]));

        // Ajout du gestionnaire d'événements
        leBtn.addActionListener(new GereClickBouton(leBtn));

        // Ajout du bouton à la fenêtre
        fenetre.add(leBtn);
        // Affichage de la fenêtre
        fenetre.setVisible(true);
    }
}

// Gestionnaire d'événements
class GereClickBouton implements ActionListener {
    private JButton btn;
    private int compteur = 0;
    private static final String[] TABIMAGES = {
        "images/Bird.gif", "images/Bird2.gif", "images/Cat.gif",
        "images/Cat2.gif", "images/Dog.gif", "images/Rabbit.gif", "images/Pig.gif"
    };

    public GereClickBouton(JButton btn) {
        this.btn = btn;
    }

    public void actionPerformed(ActionEvent e) {
        compteur = (compteur + 1) % TABIMAGES.length;
        btn.setIcon(new ImageIcon(TABIMAGES[compteur]));
    }
}
