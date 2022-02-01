from flask import Flask, render_template, url_for, redirect, request, flash
from SSIS import mysql
from . import student
from cloudinary.uploader import upload, destroy

@student.route('/')
def Index():
    cur = mysql.connection.cursor()
    cursor = mysql.connection.cursor()
    cur.execute("SELECT * FROM student_list")
    cursor.execute("SELECT * FROM course_list")
    course= cursor.fetchall()
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', student_list = data, course=course)

@student.route('/insert', methods = ['POST'])
def insert():
    stud_id = (request.form['stud_id']).strip()
    file = request.files.get('file')
    fname = request.form['fname']
    lname = request.form['lname']
    course = request.form['course']
    year_lvl = request.form['year_lvl']
    gender = request.form['gender']
    if request.method == "POST":
        flash("Data Inserted Successfully")
        sample="ssis/{}".format(stud_id)
        upload(file.read(), public_id="ssis/{}".format(stud_id))

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO student_list (stud_id, fname, lname, course, year_lvl, gender) VALUES (%s, %s, %s, %s, %s, %s)",
                    (stud_id, fname, lname, course, year_lvl, gender))
        mysql.connection.commit()
        return redirect(url_for('student.Index'))

@student.route('/delete/student/<string:stud_id>')
def delete(stud_id):
    destroy(public_id="ssis/{}".format(stud_id))
    flash("Record has been deleted successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM student_list WHERE stud_id=%s", (stud_id,))
    mysql.connection.commit()
    return redirect(url_for('student.Index'))

@student.route('/update', methods = ['POST', 'GET'])
def update():
    if request.method == 'POST':
        # stud_id = request.form['stud_id']
        stud_id = request.form.get('stud_id')
        fname = request.form['fname']
        lname = request.form['lname']
        course = request.form['course']
        year_lvl = request.form['year_lvl']
        gender = request.form['gender']
        cur = mysql.connection.cursor()
        file = request.files.get('file')
        if file:
            file_name = 'ssis/' + stud_id
            destroy(file_name)
            upload(file.read(), public_id="ssis/{}".format(stud_id.strip()))
        cur.execute("""UPDATE student_list SET fname=%s, lname=%s, course=%s, year_lvl=%s, gender=%s WHERE stud_id=%s""",
                    (fname, lname, course, year_lvl, gender, stud_id))
        flash("Data updated successfully")
        mysql.connection.commit()
        return redirect(url_for('student.Index'))

@student.route('/searchstudent', methods=['GET', 'POST'])
def searchstudent():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM student_list")
    students = cur.fetchall()
    user_input = request.form['tableSearch']
    keyword = user_input.upper()
    result = []

    for student in students:    
            student_allcaps = [str(info).upper() for info in student]
            if keyword in student_allcaps:
                result.append(student)
            result
   
    if not user_input:
        flash("Input All fields", "Error")

    if len(result) !=0:
        return render_template('index.html', student_list=result)
    else:
        return redirect(url_for('student.Index'))