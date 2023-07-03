from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'  # Replace with your MySQL host
app.config['MYSQL_USER'] = 'username'  # Replace with your MySQL username
app.config['MYSQL_PASSWORD'] = 'password'  # Replace with your MySQL password
app.config['MYSQL_DB'] = 'database_name'  # Replace with your MySQL database name

# Initialize the MySQL extension
mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get form data
    name = request.form['name']
    email = request.form['email']
    
    # Create a cursor to execute queries
    cur = mysql.connection.cursor()
    
    # Execute an SQL query to insert data into the 'users' table
    cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    
    # Commit the changes to the database
    mysql.connection.commit()
    
    # Close the cursor
    cur.close()
    
    return 'Data submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
