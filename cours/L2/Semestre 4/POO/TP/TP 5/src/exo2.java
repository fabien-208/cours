import javax.swing.*;
import java.awt.*;
import java.awt.event.*;


class exo2 {   
    public static void main(String[] args) {
        JFrame fenetre = new JFrame("Nombre mystérieux");
        fenetre.setSize(400, 300);
        fenetre.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        fenetre.setLayout(new FlowLayout());

        JButton btnFin = new JButton("Fin");
        JButton btnCommencer = new JButton("Commencer");

        JLabel lblResultat = new JLabel("Trouvez un nbre entre 0 et 99", SwingConstants.CENTER);
        JLabel lblNbCoups = new JLabel("Nombre de coups: 0", SwingConstants.CENTER);

        JTextField txtSaisie = new JTextField(5);

        fenetre.add(lblResultat);
        fenetre.add(lblNbCoups);
        fenetre.add(txtSaisie);
        fenetre.add(btnCommencer);
        fenetre.add(btnFin);



        LiaisonMystIG.setBtnFin(btnFin);
        LiaisonMystIG.setBtnCommencer(btnCommencer);
        LiaisonMystIG.setLblResultat(lblResultat);
        LiaisonMystIG.setLblNbCoups(lblNbCoups);
        LiaisonMystIG.setZoneSaisie(txtSaisie);

        fenetre.setVisible(true);
    }
}