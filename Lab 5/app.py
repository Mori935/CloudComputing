from flask import Flask
from flask import request
from flask_mysqldb import MySQL
from flask_cors import CORS
import json
mysql = MySQL()
app = Flask(__name__)
CORS(app)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'student'
app.config['MYSQL_HOST'] = 'localhost'
mysql.init_app(app)


@app.route("/add")
def add():
    name = request.args.get('name')
    email = request.args.get('email')
    cur = mysql.connection.cursor()
    s='''INSERT INTO students(studentName, email) VALUES('{}','{}');'''.format(name,email)
    cur.execute(s)
    mysql.connection.commit()

    return '{"Result":"success"}'

@app.route("/")
def read():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * From students''')
    rv = cur.fetchall()
    Results=[]
    for row in rv:
        Result={}
        Result['Name']=row[0].replace('\n',' ')
        Result['Email']=row[1]
        Result['ID']=row[2]
        Results.append(Result)
    
    response={'Results':Results, 'count':len(Results)}
    ret=app.response_class(
        response=json.dumps(response),
        status=200,
        mimetype='application/json'
    )
    return ret
if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080')
