from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Initialize the database connection
con = sqlite3.connect("garage.db", check_same_thread=False)
cur = con.cursor()

try:
    cur.execute("CREATE TABLE cars (car TEXT, model TEXT)") 
except sqlite3.OperationalError:
    print("Table already exists")

# Display index/form page (1)
@app.route('/',methods=['post', 'get'] )
def display():
    res = cur.execute("SELECT * FROM cars")
    return render_template('index.html', data=res.fetchall())

# Get data from index/form page and display on the page (2)
@app.route('/insert', methods=['post', 'get'])
def insert():
    if request.method == 'POST':
        try:
            car = request.form["namee"]
            model = request.form['model']
            cur.execute("INSERT INTO cars (car, model) VALUES (?, ?)", (car, model))
            con.commit()
        except Exception as e:
            print(e)

    res = cur.execute("SELECT * FROM cars")
    return render_template('index.html', data=res.fetchall())

if __name__ == "__main__":
    app.run(debug=True)


