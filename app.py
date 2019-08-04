from flask import Flask, render_template, request
import sqlite3

app= Flask(__name__)

DATABASE = 'app.db'

def connectDB():
    return sqlite3.connect(DATABASE)

@app.route('/')
@app.route("/home")
def index():
    return render_template('index.html')

@app.route('/pictures')
def pictures():
    return render_template('pictures.html')

@app.route('/choosing')
def choosing():
    return render_template('choosing.html')

@app.route('/addinfo')
def addinfo():
    firstName = request.args.get('firstName')
    lastName = request.args.get('lastName')
    firstChoice = request.args.get('firstChoice')
    scndChoice = request.args.get('scndChoice')
    thirdChoice = request.args.get('thirdChoice')
    db = connectDB()
    sql = "insert into travelDestination (firstName, lastName, firstChoice, scndChoice, thirdChoice) values (?,?,?,?,?)"
    db.execute(sql, [firstName, lastName, firstChoice, scndChoice, thirdChoice])
    db.commit()
    db.close()
    return render_template('choosing.html', firstName=firstName, lastName=lastName, firstChoice=firstChoice, scndChoice=scndChoice, thirdChoice=thirdChoice)

@app.route('/list')
def list():
    db = connectDB()
    cur = db.execute("select id, firstName, lastName, firstChoice, scndChoice, thirdChoice from travelDestination")
    entries = [dict(id=row[0], firstName=row[1], lastName=row[2], firstChoice=row[3], scndChoice=row[4], thirdChoice=row[5]) for row in cur.fetchall()]
    print(entries)
    db.close()
    return render_template('list.html', entries=entries)

@app.route('/update')
def update():
    id = request.args.get('id')
    firstName = request.args.get('firstName')
    lastName = request.args.get('lastName')
    firstChoice = request.args.get('firstChoice')
    scndChoice = request.args.get('scndChoice')
    thirdChoice = request.args.get('thirdChoice')
    db = connectDB()
    sql = "update travelDestination set firstName=?, lastName=?, firstChoice=?, scndChoice=?, thirdChoice=? where id=?"
    db.execute(sql, [firstName, lastName, firstChoice, scndChoice, thirdChoice, id])
    db.commit()
    db.close()
    return list()

@app.route('/edit')
def edit():
    id = request.args.get('id')
    db = connectDB()
    cur = db.execute("select id, firstName, lastName, firstChoice, scndChoice, thirdChoice from travelDestination where id=?", [id])
    rv = cur.fetchall()
    cur.close()
    travelInfo = rv[0]
    print(rv[0])
    db.close()
    return render_template('listUpdate.html', travelInfo=travelInfo)

@app.route('/delete')
def delete():
    id = request.args.get('id')
    db = connectDB()
    sql = "delete from travelDestination where id=?"
    db.execute(sql, [id])
    db.commit()
    db.close()
    return render_template('list.html')

if __name__ =="__main__":
    app.run(debug=True)