import javax.swing.JFrame;
import javax.swing.JLabel;
import java.awt.Dimension;

class exo1 {
    public static void main(String[] args) {
        JFrame fenetre = new JFrame("fenetre");
        fenetre.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        Dimension dimEcran = fenetre.getToolkit().getScreenSize();
        JLabel label = new JLabel("Taille de l'ecran : " + dimEcran);
        fenetre.getContentPane().add(label);

        fenetre.pack();

        int fenetreWidth = fenetre.getWidth();
        int fenetreHeight = fenetre.getHeight();
        int locationX = (dimEcran.width - fenetreWidth) / 2;
        int locationY = (dimEcran.height - fenetreHeight) / 2;
        fenetre.setLocation(locationX, locationY);

        fenetre.setVisible(true);

        System.out.println("Screen width: " + dimEcran.width);
        System.out.println("Screen height: " + dimEcran.height);
    }
}
