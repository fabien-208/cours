import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

class modeleMemory {
    private String[][] tab;
    private int nbLignes;
    private int nbColonnes;
    private int nbCartesRetournees;
    private int nbCartesTrouvees;
    private int nbCartes;
    private String [] liste;
    
    public modeleMemory(int nbLignes, int nbColonnes) {
        this.nbLignes = nbLignes;
        this.nbColonnes = nbColonnes;
        this.nbCartes = nbLignes * nbColonnes;
        this.nbCartesRetournees = 0;
        this.nbCartesTrouvees = 0;
        this.tab = new String[nbLignes][nbColonnes];
        this.liste = new String[]{"bin/images/Bird.gif", "bin/images/Bird2.gif", "bin/images/Cat.gif",
                                  "bin/images/Cat2.gif", "bin/images/Dog.gif", "bin/images/Dog2.gif", 
                                  "bin/images/Pig.gif", "bin/images/Rabbit.gif"};
        for (int i = 0; i < nbLignes; i++) {
            for (int j = 0; j < nbColonnes; j++) {
                this.tab[i][j] = liste[j];
            }
        }
    }
    
    public int getNbLignes() { return this.nbLignes; }
    public int getNbColonnes() { return this.nbColonnes; }
    public int getNbCartesRetournees() { return this.nbCartesRetournees; }
    public int getNbCartesTrouvees() { return this.nbCartesTrouvees; }
    public int getNbCartes() { return this.nbCartes; }
    public String getCarte(int i, int j) { return this.tab[i][j]; }
}

class MemoryGUI extends JFrame {
    private modeleMemory modele;
    private JButton[][] buttons;
    private JLabel statusLabel;
    private ImageIcon hiddenIcon;
    private int essais;
    
    public void main(int nbLignes, int nbColonnes) {
        this.modele = new modeleMemory(nbLignes, nbColonnes);
        this.buttons = new JButton[nbLignes][nbColonnes];
        this.setLayout(new BorderLayout());
        JPanel gridPanel = new JPanel(new GridLayout(nbLignes, nbColonnes));
        hiddenIcon = new ImageIcon("image.png"); // Load question mark image
        
        for (int i = 0; i < nbLignes; i++) {
            for (int j = 0; j < nbColonnes; j++) {
                buttons[i][j] = new JButton(hiddenIcon);
                buttons[i][j].addActionListener(new ButtonClickListener(i, j));
                gridPanel.add(buttons[i][j]);
            }
        }
        
        statusLabel = new JLabel("Nbre d'images gagnées : 0 | Nbre d'essais : 0");
        this.add(gridPanel, BorderLayout.CENTER);
        this.add(statusLabel, BorderLayout.SOUTH);
        
        this.setTitle("Memory");
        this.setSize(600, 600);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setVisible(true);
    }
    
    private class ButtonClickListener implements ActionListener {
        private int row, col;
        
        public ButtonClickListener(int row, int col) {
            this.row = row;
            this.col = col;
        }

        @Override
        public void actionPerformed(ActionEvent e) {
            essais++;
            buttons[row][col].setText(modele.getCarte(row, col));
            statusLabel.setText("Nbre d'images gagnées : 0 | Nbre d'essais : " + essais);
        }
    }
}
