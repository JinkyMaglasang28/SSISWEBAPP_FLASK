import app
from flask_mysqldb import mysql
from flask import Flask, render_template, url_for, redirect, request, flash
from flask_mysqldb import MySQL
from SSIS.models.student import Student
from SSIS.models.course import Course
from SSIS.models.college import College
from . import colleges



@app.route('/college')
def college():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM college_list")
    data = cur.fetchall()
    cur.close()

    return render_template('college.html', college_list = data)

@app.route('/add_college', methods = ['POST'])
def add_college():
    if request.method == "POST":
        flash("Data Inserted Successfully")
    if request.method == "POST":
        college_code = request.form['college_code']
        college_name = request.form['college_name']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO college_list (college_name, college_code) VALUES (%s, %s)",
                        (college_code, college_name))
        mysql.connection.commit()
        return redirect(url_for('college'))

@app.route('/update_college', methods = ['POST', 'GET'])
def update_college():
    if request.method == 'POST':
        college_code = request.form['college_code']
        college_name = request.form['college_name']
        cur = mysql.connection.cursor()
        cur.execute(
            """UPDATE college_list SET college_code=%s, college_name=%s, WHERE college_code=%s""",
            (college_name, college_code))
        flash("Data updated successfully")
        mysql.connection.commit()
        return redirect(url_for('college'))

@app.route('/delete/<string:college_name>', methods = ['GET'])
def delete_college(college_code):
    flash("Record has been deleted successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM college_code WHERE college_code=%s", (college_code,))
    mysql.connection.commit()
    return redirect(url_for('Index'))
