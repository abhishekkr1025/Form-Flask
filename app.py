from flask import Flask, render_template,request
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect('database.db')
conn.execute('CREATE TABLE IF NOT EXISTS PARTICIPANTS (name TEXT,email TEXT,\
	     city TEXT,country TEXT,phone TEXT)')

@app.route("/")
def index():
	return render_template("index.html")
@app.route("/<name>")
def welcome(name):
	return render_template("welcome.html", name=name)
@app.route("/home")
def home():
	return render_template("home.html")
@app.route("/about")
def about():
	sites = ["Twitter","Facebook","Instagram","Whatsapp"]
	return render_template("about.html",sites=sites)
@app.route("/contact/<role>")
def contact(role):
	return render_template("contact.html", person=role)


connect = sqlite3.connect('database.db')
connect.execute(
    'CREATE TABLE IF NOT EXISTS PARTICIPANTS (name TEXT, \
    email TEXT, city TEXT, country TEXT, phone TEXT)')
  
  
@app.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        city = request.form['city']
        country = request.form['country']
        phone = request.form['phone']
  
        with sqlite3.connect("database.db") as users:
            cursor = users.cursor()
            cursor.execute("INSERT INTO PARTICIPANTS \
            (name,email,city,country,phone) VALUES (?,?,?,?,?)",
                           (name, email, city, country, phone))
            users.commit()
        return render_template("form.html")
    else:
        return render_template('join.html')
    

    
@app.route('/participants')
def participants():
    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM PARTICIPANTS')
  
    data = cursor.fetchall()
    return render_template("participants.html", data=data)
	


         


if __name__ == "__main__":
	app.run()
