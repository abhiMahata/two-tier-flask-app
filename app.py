from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'mysql'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'devops'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    message = request.form.get('message')
    cur = mysql.connection.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS messages (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), message TEXT)")
    cur.execute("INSERT INTO messages (name, message) VALUES (%s, %s)", (name, message))
    mysql.connection.commit()
    cur.close()
    return f"<h2>Thanks, {name}! Message saved.</h2><a href='/'>Go back</a>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
