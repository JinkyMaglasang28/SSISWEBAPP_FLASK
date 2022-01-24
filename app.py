from flask import Flask, render_template, url_for, redirect, request, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "flash message"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'database'

mysql = MySQL(app)

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

@app.route('/delete/student/<string:stud_id>')
def delete(stud_id):
    flash("Record has been deleted successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM student_list WHERE stud_id=%s", (stud_id,))
    mysql.connection.commit()
    return redirect(url_for('Index'))

@app.route('/update', methods = ['POST', 'GET'])
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
        cur.execute("""UPDATE student_list SET fname=%s, lname=%s, course=%s, year_lvl=%s, gender=%s WHERE stud_id=%s""",
                    (fname, lname, course, year_lvl, gender, stud_id))
        flash("Data updated successfully")
        mysql.connection.commit()
        return redirect(url_for('Index'))


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
            """UPDATE course_list SET course_name=%s, college=%s WHERE course_code=%s""",
            (course_name, college, course_code))
        flash("Data updated successfully")
        mysql.connection.commit()
        return redirect(url_for('course'))

@app.route('/delete/course/<string:course_code>', methods = ['GET'])
def delete_course(course_code):
    flash("Record has been deleted successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM course_list WHERE course_code=%s", (course_code,))
    mysql.connection.commit()
    return redirect(url_for('course'))



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
        cur.execute("INSERT INTO college_list (college_code, college_name) VALUES (%s, %s)",
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
            """UPDATE college_list SET college_name=%s WHERE college_code=%s""",
            (college_name, college_code))
        flash("Data updated successfully")
        mysql.connection.commit()
        return redirect(url_for('college'))

@app.route('/delete/college/<string:college_code>', methods = ['GET'])
def delete_college(college_code):
    flash("Record has been deleted successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM college_list WHERE college_code=%s", (college_code,))
    mysql.connection.commit()
    return redirect(url_for('Index'))


'''def search(self,searchInput):
		cur = mysql.connection.cursor()
		cur.execute("SET @search=%s",(searchInput,))

		cur.execute("""SELECT * FROM(SELECT department.departmentNo,department.departmentName,college.collegeCode
					   FROM department,college
					   WHERE department.college=college.collegeNo) AS department
					   WHERE departmentNo  LIKE CONCAT('%',@search,'%') or departmentName LIKE CONCAT('%',@search,'%')  or 
					   		 collegeCode LIKE CONCAT('%',@search,'%')""")
		data = cur.fetchall()

		return data'''

if __name__=="__main__":
    app.run(debug=True)