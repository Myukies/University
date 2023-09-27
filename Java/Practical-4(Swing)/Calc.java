import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class Calc extends JFrame implements ActionListener {

    public static void main(String args[]) {
        new Calc();
    }

    JButton add, sub, pro, div, clr;
    JTextField t1, t2;
    JLabel res;

    public Calc() {
        setTitle(" Calculator ");
        add = new JButton(" + ");
        sub = new JButton(" - ");
        pro = new JButton(" * ");
        div = new JButton(" / ");
        clr = new JButton(" clear ");
        t1 = new JTextField(20);
        t2 = new JTextField(20);
        res = new JLabel();

        JPanel top = new JPanel();
        top.setBackground(Color.yellow);

        JPanel bot = new JPanel();
        bot.setBackground(Color.blue);
        bot.setLayout(new FlowLayout());
        bot.add(add);
        bot.add(sub);
        bot.add(pro);
        bot.add(div);
        bot.add(clr);
        bot.add(res);

        top.setLayout(new GridLayout(2, 2));
        top.add(new JLabel("Number1:"));
        top.add(t1);
        top.add(new JLabel("Number2:"));
        top.add(t2);

        setLayout(new GridLayout(2, 1));
        add(top);
        add(bot);
        setSize(400, 150);
        setVisible(true);

        add.addActionListener(this);
        sub.addActionListener(this);
        pro.addActionListener(this);
        div.addActionListener(this);
        clr.addActionListener(this);

        setDefaultCloseOperation(EXIT_ON_CLOSE);
    }

    public void actionPerformed(ActionEvent e) {
        int n1 = Integer.parseInt(t1.getText());
        int n2 = Integer.parseInt(t2.getText());
        int r = 0;

        if (e.getSource() == add) {
            r = n1 + n2;
            res.setText(r + "");
        } else if (e.getSource() == sub) {
            r = n1 - n2;
            res.setText(r + "");
        } else if (e.getSource() == pro) {
            r = n1 * n2;
            res.setText(r + "");
        } else if (e.getSource() == div) {
            r = n1 / n2;
            res.setText(r + "");
        } else {
            t1.setText("");
            t2.setText("");
            res.setText("");
        }
    }
}
