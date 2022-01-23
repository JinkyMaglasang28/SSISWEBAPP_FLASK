from flask import Flask, render_template, url_for, redirect, request, flash
from flask_mysqldb import MySQL
from flask_mysqldb import mysql
import app
from . import students 
from SSIS.models.student import student
from SSIS.models.course import course
from SSIS.models.college import college


@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM student_list")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', student_list = data)

@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
        flash("Data Inserted Successfully")
    if request.method == "POST":
        stud_id = request.form['stud_id']
        fname = request.form['fname']
        lname = request.form['lname']
        course = request.form['course']
        year_lvl = request.form['year_lvl']
        gender = request.form['gender']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO student_list (stud_id, fname, lname, course, year_lvl, gender) VALUES (%s, %s, %s, %s, %s, %s)",
                    (stud_id, fname, lname, course, year_lvl, gender))
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/delete/<string:stud_id>', methods = ['GET'])
def delete(stud_id):
    flash("Record has been deleted successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM student_list WHERE stud_id=%s", (stud_id,))
    mysql.connection.commit()
    return redirect(url_for('Index'))

@app.route('/update', methods = ['POST', 'GET'])
def update():
    if request.method == 'POST':
        stud_id = request.form['stud_id']
        fname = request.form['fname']
        lname = request.form['lname']
        course = request.form['course']
        year_lvl = request.form['year_lvl']
        gender = request.form['gender']
        cur = mysql.connection.cursor()
        cur.execute("""UPDATE student_list SET fname=%s, lname=%s, course=%s, year_lvl=%s, gender=%s WHERE stud_id=%s""",
                    (fname, lname, course, year_lvl, gender, stud_id))
        flash("Data updated successfully")
        mysql.connection.commit()
        return redirect(url_for('Index'))