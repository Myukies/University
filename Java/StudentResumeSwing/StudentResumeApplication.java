import javax.swing.*;
import java.awt.*;

public class StudentResumeApplication extends JFrame {
    private JTextField nameField, emailField;
    private JTextArea educationArea, experienceArea;
    private JButton submitButton;

    public StudentResumeApplication() {
        setTitle("Student Resume Application");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(new GridLayout(5, 1));

        JLabel nameLabel = new JLabel("Name:");
        nameField = new JTextField();

        JLabel emailLabel = new JLabel("Email:");
        emailField = new JTextField();

        JLabel educationLabel = new JLabel("Education:");
        educationArea = new JTextArea();

        JLabel experienceLabel = new JLabel("Experience:");
        experienceArea = new JTextArea();

        submitButton = new JButton("Submit");
        submitButton.addActionListener(e -> submitResume());

        add(nameLabel);
        add(nameField);
        add(emailLabel);
        add(emailField);
        add(educationLabel);
        add(new JScrollPane(educationArea));
        add(experienceLabel);
        add(new JScrollPane(experienceArea));
        add(submitButton);

        setVisible(true);
    }

    private void submitResume() {
        String name = nameField.getText();
        String email = emailField.getText();
        String education = educationArea.getText();
        String experience = experienceArea.getText();

        JOptionPane.showMessageDialog(this, "Resume submitted successfully!",
                "Success", JOptionPane.INFORMATION_MESSAGE);

        nameField.setText("");
        emailField.setText("");
        educationArea.setText("");
        experienceArea.setText("");
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(StudentResumeApplication::new);
    }
}
