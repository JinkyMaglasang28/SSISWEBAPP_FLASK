from flask import Flask, render_template, url_for, redirect, request, flash
from SSIS import mysql
from . import colleges

@colleges.route('/college')
def college():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM college_list")
    data = cur.fetchall()
    cur.close()

    return render_template('college.html', college_list = data)

@colleges.route('/add_college', methods = ['POST'])
def add_college():
    if request.method == "POST":
        flash("Data Inserted Successfully")
    if request.method == "POST":
        college_code = request.form['college_code']
        college_name = request.form['college_name']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO college_list (college_code, college_name) VALUES (%s, %s)",
                        (college_code, college_name))
        mysql.connection.commit()
        return redirect(url_for('college.college'))

@colleges.route('/update_college', methods = ['POST', 'GET'])
def update_college():
    if request.method == 'POST':
        college_code = request.form['college_code']
        college_name = request.form['college_name']
        cur = mysql.connection.cursor()
        cur.execute(
            """UPDATE college_list SET college_name=%s WHERE college_code=%s""",
            (college_name, college_code))
        flash("Data updated successfully")
        mysql.connection.commit()
        return redirect(url_for('college.college'))

@colleges.route('/delete/college/<string:college_code>', methods = ['GET'])
def delete_college(college_code):
    flash("Record has been deleted successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM college_list WHERE college_code=%s", (college_code,))
    mysql.connection.commit()
    return redirect(url_for('college.college'))

@colleges.route('/searchcollege', methods=['GET', 'POST'])
def searchstudent():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM college_list")
    colleges = cur.fetchall()
    user_input = request.form['tableSearch']
    keyword = user_input.upper()
    result = []

    for college in colleges:    
            student_allcaps = [str(info).upper() for info in college]
            if keyword in student_allcaps:
                result.append(college)
            result
   
    if not user_input:
        flash("Input All fields", "Error")

    if len(result) !=0:
        return render_template('college.html', college_list=result)
    else:
        return redirect(url_for('college.college'))