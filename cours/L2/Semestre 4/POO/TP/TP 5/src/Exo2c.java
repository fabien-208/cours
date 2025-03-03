import javax.swing.*;
import java.awt.*;

public class Exo2c {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Exo2c");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 200);

        JPanel panel = new JPanel();
        panel.setLayout(new BoxLayout(panel, BoxLayout.Y_AXIS));

        JButton btnFin = new JButton("Fin");
        JButton btnCommencer = new JButton("Commencer");

        JLabel lblResultat = new JLabel("Trouvez un nbre entre 0 et 99", SwingConstants.CENTER);
        JLabel lblNbCoups = new JLabel("Nombre de coups: 0", SwingConstants.CENTER);

        JTextField txtSaisie = new JTextField(5);

        panel.add(lblResultat);
        panel.add(lblNbCoups);
        panel.add(txtSaisie);
        panel.add(btnCommencer);
        panel.add(btnFin);
        frame.add(panel);
        frame.setVisible(true);
    }
}