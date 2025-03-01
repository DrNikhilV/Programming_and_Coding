from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)
app.secret_key = 'dbmsInventorySystem'

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Ganesh@123'
app.config['MYSQL_DB'] = 'inventory_system'

mysql = MySQL(app)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
    account = cursor.fetchone()
    
    if account:
        return redirect(url_for('home'))
    else:
        flash('Invalid username or password')
        return redirect(url_for('login'))

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup_post():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    phone_number = request.form['phone_number']
    
    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO users (username, password, email, phone_number) VALUES (%s, %s, %s, %s)', 
                   (username, password, email, phone_number))
    mysql.connection.commit()
    return redirect(url_for('login'))

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/view_inventory')
def view_inventory():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM inventory')
    inventory = cursor.fetchall()
    return render_template('view_inventory.html', inventory=inventory)

@app.route('/add_sales')
def add_sales():
    return render_template('add_sales.html')

@app.route('/add_sales', methods=['POST'])
def add_sales_post():
    product_name = request.form['product_name']
    cost = request.form['cost']
    quantity = request.form['quantity']
    date = request.form['date']
    
    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO sales_history (product_name, cost, quantity, date_sold) VALUES (%s, %s, %s, %s)', 
                   (product_name, cost, quantity, date))
    mysql.connection.commit()
    
    cursor.execute('INSERT INTO inventory (product_name, cost, quantity, date_bought) VALUES (%s, %s, %s, %s)', 
                   (product_name, cost, quantity, date))
    mysql.connection.commit()
    
    return redirect(url_for('view_inventory'))

@app.route('/sales_history')
def sales_history():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM sales_history')
    sales = cursor.fetchall()
    return render_template('sales_history.html', sales=sales)

if __name__ == '__main__':
    app.run(debug=True)