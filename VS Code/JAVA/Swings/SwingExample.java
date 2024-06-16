import javax.swing.*;
import java.awt.event.*;

public class SwingExample extends JFrame {
    private JTextField jTextField1;
    private JTextField jTextField2;
    private JLabel jLabel3;
    private JButton calculateButton;
    private JButton clearButton;
    private JButton exitButton;

    public SwingExample() {
        initComponents();
    }

    private void initComponents() {
        jTextField1 = new JTextField();
        jTextField2 = new JTextField();
        jLabel3 = new JLabel();
        calculateButton = new JButton("Calculate");
        clearButton = new JButton("Clear");
        exitButton = new JButton("Exit");

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setTitle("Swing Example");

        calculateButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent evt) {
                calculateButtonActionPerformed(evt);
            }
        });

        clearButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent evt) {
                clearButtonActionPerformed(evt);
            }
        });

        exitButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent evt) {
                exitButtonActionPerformed(evt);
            }
        });

        GroupLayout layout = new GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(50, 50, 50)
                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING)
                            .addComponent(jLabel3)
                            .addGroup(layout.createSequentialGroup()
                                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING, false)
                                    .addComponent(jTextField1, GroupLayout.DEFAULT_SIZE, 100, Short.MAX_VALUE)
                                    .addComponent(jTextField2))
                                .addGap(18, 18, 18)
                                .addComponent(calculateButton)))
                        .addContainerGap(GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                    .addGroup(layout.createSequentialGroup()
                        .addComponent(clearButton)
                        .addPreferredGap(LayoutStyle.ComponentPlacement.RELATED, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addComponent(exitButton)
                        .addGap(56, 56, 56))))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(30, 30, 30)
                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(jTextField1, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
                    .addComponent(calculateButton))
                .addGap(18, 18, 18)
                .addComponent(jTextField2, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
                .addGap(18, 18, 18)
                .addComponent(jLabel3)
                .addGap(18, 18, 18)
                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(clearButton)
                    .addComponent(exitButton))
                .addContainerGap(30, Short.MAX_VALUE))
        );

        pack();
    }

    private void calculateButtonActionPerformed(ActionEvent evt) {
        int a = Integer.parseInt(jTextField1.getText());
        int b = Integer.parseInt(jTextField2.getText());
        int c = a + b;
        jLabel3.setText("The Sum is " + c);
    }

    private void clearButtonActionPerformed(ActionEvent evt) {
        jTextField1.setText(null);
        jTextField2.setText(null);
        jLabel3.setText("");
    }

    private void exitButtonActionPerformed(ActionEvent evt) {
        System.exit(0);
    }

    public static void main(String args[]) {
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new SwingExample().setVisible(true);
            }
        });
    }
}
