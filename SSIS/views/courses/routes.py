from flask import Flask, render_template, url_for, redirect, request, flash
from SSIS import mysql
from . import courses


@courses.route('/course')
def course():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM course_list")
    data = cur.fetchall()
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM college_list")
    college = cursor.fetchall()
    cur.close()
    return render_template('course.html', course_list = data, college=college)

@courses.route('/add_course', methods = ['POST'])
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
        return redirect(url_for('course.course'))

@courses.route('/update_course', methods = ['POST', 'GET'])
def update_course():
    if request.method == 'POST':
        course_code = request.form['course_code']
        course_name = request.form['course_name']
        college = request.form['college']
        cur = mysql.connection.cursor()
        cur.execute(
            """UPDATE course_list SET course_name=%s, college=%s WHERE course_code=%s""",
            (course_name, college, course_code))
        flash("Data updated successfully")
        mysql.connection.commit()
        return redirect(url_for('course.course'))

@courses.route('/delete/course/<string:course_code>', methods = ['GET'])
def delete_course(course_code):
    flash("Record has been deleted successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM course_list WHERE course_code=%s", (course_code,))
    mysql.connection.commit()
    return redirect(url_for('course.course'))

@courses.route('/searchcourse', methods=['GET', 'POST'])
def searchstudent():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM course_list")
    courses = cur.fetchall()
    user_input = request.form['tableSearch']
    keyword = user_input.upper()
    result = []

    for course in courses:    
            student_allcaps = [str(info).upper() for info in course]
            if keyword in student_allcaps:
                result.append(course)
            result
   
    if not user_input:
        flash("Input All fields", "Error")

    if len(result) !=0:
        return render_template('course.html', course_list=result)
    else:
        return redirect(url_for('course.course'))