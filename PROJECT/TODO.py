from flask import Flask, render_template,request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'TODO'

mysql = MySQL(app)

@app.route('/data/create',methods=['GET','POST'])
def POST():
    if request.method == "POST":
        details = request.form
        data = details["dList"]
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Datas (dList)VALUES (\"%s\")", [data])   
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('insert.html')

# @app.route('/data/view' )
# def VIEW():
#     if request.method == "GET":
#         # details = request.form
#         # data = details["dList"]
#         cur = mysql.connection.cursor()
#         cur.execute("SELECT * FROM Datas")
#         view_data = cur.fetchall()
#         print(view_data)
#         mysql.connection.commit()
#         cur.close()
#         # return 'view is done'
#     return render_template('view.html', data=view_data)



if __name__ == "__main__":
    app.run(host='localhost',debug=True, port=5000)
