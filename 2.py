from flask import Flask, render_template, redirect,request
from flask_mysqldb import MySQL
import redis



app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'vnexpress'

mysql = MySQL(app)
peewee


@app.route('/', methods=['GET', 'POST'])
def hi():
  if request.method == 'POST':
    user = request.form
    name = user['name']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO user(name) VALUES (%s)",[name])
    mysql.connection.commit()
    cur.close()
    return redirect('/class3')
  return render_template('class2.html')




@app.route('/class3')


def hello():
  cur = mysql.connection.cursor()
  h = cur.execute("SELECT * FROM class")
  if h >0:
    show = cur.fetchall()
    return render_template('class3.html', data=show)


if __name__=='__main__':
  app.run(debug=True)