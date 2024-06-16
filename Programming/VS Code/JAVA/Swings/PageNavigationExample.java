import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class PageNavigationExample extends JFrame {
    private JPanel mainPanel;
    private JButton nextPageButton;
    private JButton previousPageButton;

    public PageNavigationExample() {
        setTitle("Page Navigation Example");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(400, 300);
        setLocationRelativeTo(null);

        mainPanel = new JPanel();
        mainPanel.setLayout(new BorderLayout());

        // Create buttons
        nextPageButton = new JButton("Next Page");
        previousPageButton = new JButton("Previous Page");

        // Add action listeners to the buttons
        nextPageButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                showNextPage();
            }
        });

        previousPageButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                showPreviousPage();
            }
        });

        // Add buttons to the panel
        mainPanel.add(nextPageButton, BorderLayout.CENTER);
        mainPanel.add(previousPageButton, BorderLayout.NORTH);

        // Set the main panel as the content pane
        setContentPane(mainPanel);
    }

    private void showNextPage() {
        // Create a new JFrame for the next page
        JFrame nextPage = new JFrame();
        nextPage.setTitle("Next Page");
        nextPage.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        nextPage.setSize(400, 300);
        nextPage.setLocationRelativeTo(this);
        nextPage.setVisible(true);
    }

    private void showPreviousPage() {
        // Create a new JFrame for the previous page
        JFrame previousPage = new JFrame();
        previousPage.setTitle("Previous Page");
        previousPage.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        previousPage.setSize(400, 300);
        previousPage.setLocationRelativeTo(this);
        previousPage.setVisible(true);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                PageNavigationExample example = new PageNavigationExample();
                example.setVisible(true);
            }
        });
    }
}
