import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class Resume extends JFrame implements ActionListener {
    public static void main(String args[]) {
        new Resume();
    }

    JButton sub, clr;
    JTextField nm, bd, fn, nas, ph, em;
    JRadioButton m, f;
    JComboBox<String> q;
    JTextArea ta;

    public Resume() {
        setTitle("Resume builder");
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLayout(new GridLayout(10, 2));

        add(new JLabel("Student's Name"));
        nm = new JTextField(25);
        add(nm);

        add(new JLabel("Father's Name"));
        fn = new JTextField(25);
        add(fn);

        add(new JLabel("Birthday"));
        bd = new JTextField(10);
        add(bd);

        add(new JLabel("Nationality"));
        nas = new JTextField(25);
        add(nas);

        add(new JLabel("Phone"));
        ph = new JTextField(25);
        add(ph);

        add(new JLabel("E-Mail"));
        em = new JTextField(10);
        add(em);

        m = new JRadioButton("Male");
        f = new JRadioButton("Female");
        ButtonGroup bg = new ButtonGroup();
        bg.add(m);
        bg.add(f);
        add(m);
        add(f);

        add(new JLabel("Qualification"));
        q = new JComboBox<>();
        q.addItem("A");
        q.addItem("B");
        q.addItem("C");
        add(q);

        sub = new JButton("Submit");
        sub.addActionListener(this);
        add(sub);

        clr = new JButton("Clear");
        clr.addActionListener(this);
        add(clr);

        ta = new JTextArea();
        JScrollPane sp = new JScrollPane(ta, JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED, JScrollPane.HORIZONTAL_SCROLLBAR_AS_NEEDED);
        add(sp);

        pack();
        setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == sub) {
            StringBuffer b = new StringBuffer();
            b.append(nm.getText() + '\n');
            b.append(fn.getText() + '\n');
            b.append(bd.getText() + '\n');
            b.append(nas.getText() + '\n');
            b.append(ph.getText() + '\n');
            b.append(em.getText() + '\n');
            b.append(bd.getText() + '\n');
            b.append(q.getSelectedItem() + "\n");
            ta.setText(b.toString());
        } else {
            nm.setText("");
            fn.setText("");
            bd.setText("");
            nas.setText("");
            ph.setText("");
            em.setText("");
            bd.setText("");
        }
    }
}
