import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

class ColorDemo implements ItemListener {
    JComboBox<Integer> r, g, b;
    JFrame jfrm;

    ColorDemo() {
        jfrm = new JFrame("Color changer");
        jfrm.setSize(275, 100);
        jfrm.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        jfrm.setLayout(new FlowLayout());

        r = new JComboBox<>();
        g = new JComboBox<>();
        b = new JComboBox<>();

        jfrm.add(r);
        jfrm.add(g);
        jfrm.add(b);

        for (int i = 0; i < 256; i++) {
            r.addItem(i);
            g.addItem(i);
            b.addItem(i);
        }

        r.addItemListener(this);
        g.addItemListener(this);
        b.addItemListener(this);

        jfrm.setVisible(true);
    }

    public static void main(String args[]) {
        new ColorDemo();
    }

    @Override
    public void itemStateChanged(ItemEvent e) {
        int rc = r.getSelectedIndex();
        int gc = g.getSelectedIndex();
        int bc = b.getSelectedIndex();
        System.out.println(rc + " " + gc);
        Color c = new Color(rc, gc, bc);
        jfrm.getContentPane().setBackground(c);
    }
}
