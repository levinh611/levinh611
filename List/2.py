from flask import Flask, render_template, redirect,request
from flask_mysqldb import MySQL
import yaml
from model import app, mysql


db = yaml.load(open('db2.yaml'))
app.config['MYSQL_HOST'] = db['host']
app.config['MYSQL_USER'] = db['user']
app.config['MYSQL_PASSWORD'] = db['password']
app.config['MYSQL_DB'] = db['db']


@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    user = request.form
    name = user['name']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO user(name) VALUES (%s)", [name])
    mysql.connection.commit()
    cur.close()
    return redirect('/class3')
  return render_template('class2.html')




@app.route('/class3')


def show():
  cur = mysql.connection.cursor()
  h = cur.execute("SELECT * FROM class")
  if h >0:
    show = cur.fetchall()
    return render_template('class3.html', data=show)


if __name__=='__main__':
  app.run(debug=True)
