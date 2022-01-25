from flask import Flask, render_template, url_for, redirect, request, flash
from SSIS import mysql
from flask import Blueprint

student = Blueprint('app', url_prefix='/app')
courses  = Blueprint('app', url_prefix='/app')
colleges = Blueprint('app', url_prefix='/app')










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
