import app
from flask_mysqldb import mysql
from flask import Flask, render_template, url_for, redirect, request, flash
from flask_mysqldb import MySQL
from SSIS.models.student import Student
from SSIS.models.course import Course
from SSIS.models.college import College
from . import courses


@app.route('/course')
def course():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM course_list")
    data = cur.fetchall()
    cur.close()
    return render_template('course.html', course_list = data)

@app.route('/add_course', methods = ['POST'])
def add_course():
    if request.method == "POST":
        flash("Data Inserted Successfully")
    if request.method == "POST":
        course_code = request.form['course_code']
        course_name = request.form['course_name']
        college = request.form['college']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO course_list (course_code, course_name, college) VALUES (%s, %s, %s)", (course_code, course_name, college))
        mysql.connection.commit()
        return redirect(url_for('course'))

@app.route('/update_course', methods = ['POST', 'GET'])
def update_course():
    if request.method == 'POST':
        course_code = request.form['course_code']
        course_name = request.form['course_name']
        college = request.form['college']
        cur = mysql.connection.cursor()
        cur.execute(
            """UPDATE course_list SET course_name=%s, college=%s, WHERE course_code=%s""",
            (course_name, college, course_code))
        flash("Data updated successfully")
        mysql.connection.commit()
        return redirect(url_for('course'))

@app.route('/delete/<string:course_code>', methods = ['GET'])
def delete_course(course_code):
    flash("Record has been deleted successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM course_list WHERE course_code=%s", (course_code,))
    mysql.connection.commit()
    return redirect(url_for('Index'))




