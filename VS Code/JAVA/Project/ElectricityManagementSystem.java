import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.HashMap;
import java.util.Map;

public class ElectricityManagementSystem extends JFrame {
    private JTextField userIdField;
    private JPasswordField passwordField;
    private JLabel nameLabel;
    private JLabel mobileNumberLabel;
    private JLabel emailLabel;
    private JLabel customerIdLabel;
    private JLabel previousDuesLabel;
    private JLabel currentDuesLabel;

    private Map<String, String> userCredentials;
    private String loggedInUserId;
    private boolean hasCurrentDues;

    public ElectricityManagementSystem() {
        setTitle("Electricity Management System - Login");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(400, 250);
        setLocationRelativeTo(null);

        userCredentials = new HashMap<>();
        userCredentials.put("One", "1");
        userCredentials.put("Two", "2");
        userCredentials.put("Three", "3");
        userCredentials.put("Four", "4");

        JPanel mainPanel = new JPanel();
        mainPanel.setLayout(new GridLayout(4, 2));

        JLabel userIdLabel = new JLabel("User ID:");
        userIdField = new JTextField();

        JLabel passwordLabel = new JLabel("Password:");
        passwordField = new JPasswordField();

        JButton loginButton = new JButton("Login");
        loginButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String userId = userIdField.getText();
                String password = new String(passwordField.getPassword());

                if (authenticateUser(userId, password)) {
                    loggedInUserId = userId;
                    showHomePage();
                } else {
                    JOptionPane.showMessageDialog(ElectricityManagementSystem.this,
                            "Invalid user ID or password. Please try again.",
                            "Login Error",
                            JOptionPane.ERROR_MESSAGE);
                }
            }
        });

        JButton createNewUserButton = new JButton("Create New User");
        createNewUserButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                showCreateUserPage();
            }
        });

        mainPanel.add(userIdLabel);
        mainPanel.add(userIdField);
        mainPanel.add(passwordLabel);
        mainPanel.add(passwordField);
        mainPanel.add(loginButton);
        mainPanel.add(createNewUserButton);

        setContentPane(mainPanel);
    }

    private boolean authenticateUser(String userId, String password) {
        String storedPassword = userCredentials.get(userId);
        return storedPassword != null && storedPassword.equals(password);
    }

private String name;
private String mobileNumber;
private String email;
private String customerId;
private String previousDues;
private String currentDues;

private void updateCustomerDetails() {
    customerId = generateCustomerId();
    previousDues = hasCurrentDues ? "N/A" : "0";
    currentDues = hasCurrentDues ? "100" : "0";

    if (loggedInUserId.equals("One")) {
        name = "John Doe";
        mobileNumber = "1234567890";
        email = "john@example.com";
    } else if (loggedInUserId.equals("Two")) {
        name = "Jane Smith";
        mobileNumber = "9876543210";
        email = "jane@example.com";
        hasCurrentDues = true;
        currentDues = "200";
    } else if (loggedInUserId.equals("Three")) {
        name = "Alice Johnson";
        mobileNumber = "5555555555";
        email = "alice@example.com";
        hasCurrentDues = true;
        currentDues = "180";
    } else if (loggedInUserId.equals("Four")) {
        name = "Bob Wilson";
        mobileNumber = "9999999999";
        email = "bob@example.com";
    }
}

    private void showHomePage() {
        JFrame homePage = new JFrame();
        homePage.setTitle("Electricity Management System - Home");
        homePage.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        homePage.setSize(400, 300);
        homePage.setLocationRelativeTo(this);
    
        JPanel homePanel = new JPanel();
        homePanel.setLayout(new BorderLayout());
    
        JPanel buttonPanel = new JPanel();
        buttonPanel.setLayout(new FlowLayout(FlowLayout.CENTER));
    
        JLabel welcomeLabel = new JLabel("Welcome to our online electricity bill management system!");
    
        nameLabel = new JLabel();
        mobileNumberLabel = new JLabel();
        emailLabel = new JLabel();
        customerIdLabel = new JLabel();
        previousDuesLabel = new JLabel();
        currentDuesLabel = new JLabel();
    
        String meterNumber = generateMeterNumber();
        JLabel meterNumberLabel = new JLabel("Meter Number: " + meterNumber);


        updateCustomerDetails();    
    nameLabel.setText("Name: " + name);
    mobileNumberLabel.setText("Mobile Number: " + mobileNumber);
    emailLabel.setText("Email: " + email);
    customerIdLabel.setText("Customer ID: " + customerId);
    previousDuesLabel.setText("Previous Dues: " + previousDues);
    currentDuesLabel.setText("Current Dues: " + currentDues);

        JButton viewDetailsButton = new JButton("View Customer Details");
        viewDetailsButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                showCustomerDetailsPage();
            }
        });
    
        JButton payNowButton = new JButton("Pay Now");
        payNowButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                showPaymentPage();
            }
        });
    
        JButton logoutButton = new JButton("Logout");
        logoutButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                loggedInUserId = null;
                showLoginPage();
                homePage.dispose();
            }
        });
    
        JButton calculateBillButton = new JButton("Calculate Bill");
        calculateBillButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                showBillCalculationPage();
            }
        });
    
        buttonPanel.add(viewDetailsButton);
        buttonPanel.add(payNowButton);
        buttonPanel.add(calculateBillButton);
        buttonPanel.add(logoutButton);
    
        homePanel.add(welcomeLabel, BorderLayout.NORTH);
        homePanel.add(nameLabel, BorderLayout.CENTER);
        homePanel.add(mobileNumberLabel, BorderLayout.CENTER);
        homePanel.add(emailLabel, BorderLayout.CENTER);
        homePanel.add(customerIdLabel, BorderLayout.CENTER);
        homePanel.add(previousDuesLabel, BorderLayout.CENTER);
        homePanel.add(currentDuesLabel, BorderLayout.CENTER);
        homePanel.add(buttonPanel, BorderLayout.SOUTH);
        homePanel.add(meterNumberLabel, BorderLayout.CENTER);
    
        homePage.setContentPane(homePanel);
        homePage.setVisible(true);
    
        updateCustomerDetails();
    }

    private String generateMeterNumber() {
        int min = 10000000;
        int max = 99999999;
        int randomNum = min + (int) (Math.random() * (max - min + 1));
        return String.valueOf(randomNum);
    }

    private String generateCustomerId() {
        return String.valueOf((int) (Math.random() * 100000));
    }

    private void showPaymentPage() {
        JFrame paymentPage = new JFrame();
        paymentPage.setTitle("Electricity Management System - Payment");
        paymentPage.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        paymentPage.setSize(400, 250);
        paymentPage.setLocationRelativeTo(this);
    
        JPanel paymentPanel = new JPanel();
        paymentPanel.setLayout(new GridLayout(5, 2));
    
        JLabel paymentLabel = new JLabel("Enter payment details:");
        JLabel nameLabel = new JLabel("Name on Card:");
        JTextField nameField = new JTextField();
    
        JLabel cardNumberLabel = new JLabel("Card Number:");
        JTextField cardNumberField = new JTextField();
    
        JLabel expiryDateLabel = new JLabel("Expiry Date (MM/YY):");
        JTextField expiryDateField = new JTextField();
    
        JLabel cardTypeLabel = new JLabel("Card Type:");
        JCheckBox visaCheckbox = new JCheckBox("Visa");
        JCheckBox mastercardCheckbox = new JCheckBox("Mastercard");
        JCheckBox expressCheckbox = new JCheckBox("Express");
        JCheckBox debitCheckbox = new JCheckBox("Debit");
        JCheckBox creditCheckbox = new JCheckBox("Credit");
    
        JButton submitButton = new JButton("Submit");
    
        submitButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String name = nameField.getText();
                String cardNumber = cardNumberField.getText();
                String expiryDate = expiryDateField.getText();
                String cardType = "";
    
                if (visaCheckbox.isSelected()) {
                    cardType = "Visa";
                } else if (mastercardCheckbox.isSelected()) {
                    cardType = "Mastercard";
                } else if (expressCheckbox.isSelected()) {
                    cardType = "Express";
                } else if (debitCheckbox.isSelected()) {
                    cardType = "Debit";
                } else if (creditCheckbox.isSelected()) {
                    cardType = "Credit";
                }
    
                if (name.isEmpty() || cardNumber.isEmpty() || expiryDate.isEmpty() || cardType.isEmpty()) {
                    JOptionPane.showMessageDialog(paymentPage,
                            "Please enter all the payment details.",
                            "Error",
                            JOptionPane.ERROR_MESSAGE);
                } else {
                    JOptionPane.showMessageDialog(paymentPage,
                            "Payment completed successfully!",
                            "Success",
                            JOptionPane.INFORMATION_MESSAGE);
                    hasCurrentDues = false;
                    updateCustomerDetails();
                    paymentPage.dispose();
                }
            }
        });
    
        paymentPanel.add(paymentLabel);
        paymentPanel.add(new JLabel());
        paymentPanel.add(nameLabel);
        paymentPanel.add(nameField);
        paymentPanel.add(cardNumberLabel);
        paymentPanel.add(cardNumberField);
        paymentPanel.add(expiryDateLabel);
        paymentPanel.add(expiryDateField);
        paymentPanel.add(cardTypeLabel);
        paymentPanel.add(new JPanel());
        paymentPanel.add(visaCheckbox);
        paymentPanel.add(mastercardCheckbox);
        paymentPanel.add(expressCheckbox);
        paymentPanel.add(debitCheckbox);
        paymentPanel.add(creditCheckbox);
        paymentPanel.add(submitButton);
    
        paymentPage.setContentPane(paymentPanel);
        paymentPage.setVisible(true);
    }
    
    private void showCreateUserPage() {
        JFrame createUserPage = new JFrame();
        createUserPage.setTitle("Create New User");
        createUserPage.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        createUserPage.setSize(400, 300);
        createUserPage.setLocationRelativeTo(this);

        JPanel createUserPanel = new JPanel();
        createUserPanel.setLayout(new GridLayout(7, 2));

        JLabel nameLabel = new JLabel("Name:");
        JTextField nameField = new JTextField();

        JLabel ageLabel = new JLabel("Age:");
        JTextField ageField = new JTextField();

        JLabel locationLabel = new JLabel("Location:");
        JTextField locationField = new JTextField();

        JLabel userIdLabel = new JLabel("User ID:");
        JTextField newUserIdField = new JTextField();

        JLabel passwordLabel = new JLabel("Password:");
        JPasswordField newPasswordField = new JPasswordField();

        JButton submitButton = new JButton("Submit");
        submitButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String name = nameField.getText();
                String age = ageField.getText();
                String location = locationField.getText();
                String newUserId = newUserIdField.getText();
                String newPassword = new String(newPasswordField.getPassword());

                if (newUserId.isEmpty() || newPassword.isEmpty()) {
                    JOptionPane.showMessageDialog(createUserPage,
                            "Please enter a user ID and password.",
                            "Error",
                            JOptionPane.ERROR_MESSAGE);
                } else {
                    userCredentials.put(newUserId, newPassword);
                    JOptionPane.showMessageDialog(createUserPage,
                            "User created successfully!",
                            "Success",
                            JOptionPane.INFORMATION_MESSAGE);
                    createUserPage.dispose();
                }
            }
        });

        createUserPanel.add(nameLabel);
        createUserPanel.add(nameField);
        createUserPanel.add(ageLabel);
        createUserPanel.add(ageField);
        createUserPanel.add(locationLabel);
        createUserPanel.add(locationField);
        createUserPanel.add(userIdLabel);
        createUserPanel.add(newUserIdField);
        createUserPanel.add(passwordLabel);
        createUserPanel.add(newPasswordField);
        createUserPanel.add(new JLabel());
        createUserPanel.add(submitButton);

        createUserPage.setContentPane(createUserPanel);
        createUserPage.setVisible(true);
    }

    private void showCustomerDetailsPage() {
        JFrame customerDetailsPage = new JFrame();
        customerDetailsPage.setTitle("Electricity Management System - Customer Details");
        customerDetailsPage.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        customerDetailsPage.setSize(400, 300);
        customerDetailsPage.setLocationRelativeTo(this);
    
        JPanel customerDetailsPanel = new JPanel();
        customerDetailsPanel.setLayout(new GridLayout(7, 2));
    
        JLabel nameLabel = new JLabel("Name: " + name);
        JLabel mobileNumberLabel = new JLabel("Mobile Number: " + mobileNumber);
        JLabel emailLabel = new JLabel("Email: " + email);
        JLabel customerIdLabel = new JLabel("Customer ID: " + customerId);
        JLabel previousDuesLabel = new JLabel("Previous Dues: " + previousDues);
        JLabel currentDuesLabel = new JLabel("Current Dues: " + currentDues);
    
        JButton editButton = new JButton("Edit Customer Details");
        editButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                showEditCustomerDetailsPage();
                customerDetailsPage.dispose();
            }
        });
    
        customerDetailsPanel.add(nameLabel);
        customerDetailsPanel.add(new JLabel());
        customerDetailsPanel.add(mobileNumberLabel);
        customerDetailsPanel.add(new JLabel());
        customerDetailsPanel.add(emailLabel);
        customerDetailsPanel.add(new JLabel());
        customerDetailsPanel.add(customerIdLabel);
        customerDetailsPanel.add(new JLabel());
        customerDetailsPanel.add(previousDuesLabel);
        customerDetailsPanel.add(new JLabel());
        customerDetailsPanel.add(currentDuesLabel);
        customerDetailsPanel.add(new JLabel());
        customerDetailsPanel.add(editButton);
    
        customerDetailsPage.setContentPane(customerDetailsPanel);
        customerDetailsPage.setVisible(true);
    }

    private void showEditCustomerDetailsPage() {
        JFrame editCustomerDetailsPage = new JFrame();
        editCustomerDetailsPage.setTitle("Electricity Management System - Edit Customer Details");
        editCustomerDetailsPage.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        editCustomerDetailsPage.setSize(400, 300);
        editCustomerDetailsPage.setLocationRelativeTo(this);

        JPanel editCustomerDetailsPanel = new JPanel();
        editCustomerDetailsPanel.setLayout(new GridLayout(6, 2));

        JLabel nameLabel = new JLabel("Name:");
        JTextField nameField = new JTextField();
        nameField.setText(nameLabel.getText().replace("Name: ", ""));

        JLabel mobileNumberLabel = new JLabel("Mobile Number:");
        JTextField mobileNumberField = new JTextField();
        mobileNumberField.setText(mobileNumberLabel.getText().replace("Mobile Number: ", ""));

        JLabel emailLabel = new JLabel("Email:");
        JTextField emailField = new JTextField();
        emailField.setText(emailLabel.getText().replace("Email: ", ""));

        JButton submitButton = new JButton("Submit");
        submitButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String name = nameField.getText();
                String mobileNumber = mobileNumberField.getText();
                String email = emailField.getText();

                if (name.isEmpty() || mobileNumber.isEmpty() || email.isEmpty()) {
                    JOptionPane.showMessageDialog(editCustomerDetailsPage,
                            "Please enter all the details.",
                            "Error",
                            JOptionPane.ERROR_MESSAGE);
                } else {
                    nameLabel.setText("Name: " + name);
                    mobileNumberLabel.setText("Mobile Number: " + mobileNumber);
                    emailLabel.setText("Email: " + email);

                    JOptionPane.showMessageDialog(editCustomerDetailsPage,
                            "Customer details updated successfully!",
                            "Success",
                            JOptionPane.INFORMATION_MESSAGE);
                    editCustomerDetailsPage.dispose();
                }
            }
        });

        editCustomerDetailsPanel.add(nameLabel);
        editCustomerDetailsPanel.add(nameField);
        editCustomerDetailsPanel.add(mobileNumberLabel);
        editCustomerDetailsPanel.add(mobileNumberField);
        editCustomerDetailsPanel.add(emailLabel);
        editCustomerDetailsPanel.add(emailField);
        editCustomerDetailsPanel.add(new JLabel());
        editCustomerDetailsPanel.add(submitButton);

        editCustomerDetailsPage.setContentPane(editCustomerDetailsPanel);
        editCustomerDetailsPage.setVisible(true);
    }

    private void showLoginPage() {
        userIdField.setText("");
        passwordField.setText("");
        setVisible(true);
    }

    private void showBillCalculationPage() {
        JFrame billCalculationPage = new JFrame();
        billCalculationPage.setTitle("Electricity Management System - Bill Calculation");
        billCalculationPage.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        billCalculationPage.setSize(400, 250);
        billCalculationPage.setLocationRelativeTo(this);
    
        JPanel billCalculationPanel = new JPanel();
        billCalculationPanel.setLayout(new GridLayout(4, 2));
    
        JLabel lastMonthUnitsLabel = new JLabel("Last Month Units:");
        JTextField lastMonthUnitsField = new JTextField();
    
        JLabel thisMonthUnitsLabel = new JLabel("This Month Units:");
        JTextField thisMonthUnitsField = new JTextField();
    
        JButton calculateButton = new JButton("Calculate");
        calculateButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    int lastMonthUnits = Integer.parseInt(lastMonthUnitsField.getText());
                    int thisMonthUnits = Integer.parseInt(thisMonthUnitsField.getText());
    
                    if (lastMonthUnits < 0 || thisMonthUnits < 0) {
                        JOptionPane.showMessageDialog(billCalculationPage,
                                "Invalid units. Units must be a positive integer.",
                                "Error",
                                JOptionPane.ERROR_MESSAGE);
                    } else {
                        int unitsUsed = Math.abs(thisMonthUnits - lastMonthUnits);
                        int cost = calculateBillCost(unitsUsed);
    
                        JOptionPane.showMessageDialog(billCalculationPage,
                                "Units Used: " + unitsUsed + "\n" +
                                "Bill Amount: Rs. " + cost,
                                "Bill Calculation Result",
                                JOptionPane.INFORMATION_MESSAGE);
                    }
                } catch (NumberFormatException ex) {
                    JOptionPane.showMessageDialog(billCalculationPage,
                            "Invalid units. Please enter valid integers.",
                            "Error",
                            JOptionPane.ERROR_MESSAGE);
                }
            }
        });
    
        billCalculationPanel.add(lastMonthUnitsLabel);
        billCalculationPanel.add(lastMonthUnitsField);
        billCalculationPanel.add(thisMonthUnitsLabel);
        billCalculationPanel.add(thisMonthUnitsField);
        billCalculationPanel.add(new JLabel());
        billCalculationPanel.add(calculateButton);
    
        billCalculationPage.setContentPane(billCalculationPanel);
        billCalculationPage.setVisible(true);
    }
    
    private int calculateBillCost(int unitsUsed) {
        if (unitsUsed <= 100) {
            return Math.abs(unitsUsed * 2);
        } else if (unitsUsed <= 200) {
            return Math.abs(100 * 2 + (unitsUsed - 100) * 4);
        } else if (unitsUsed <= 300) {
            return Math.abs(100 * 2 + 100 * 4 + (unitsUsed - 200) * 6);
        } else {
            return Math.abs(100 * 2 + 100 * 4 + 100 * 6 + (unitsUsed - 300) * 8);
        }
    }

    
    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                ElectricityManagementSystem ems = new ElectricityManagementSystem();
                ems.setVisible(true);
            }
        });
    }
}