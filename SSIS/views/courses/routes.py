from flask import Flask, render_template, url_for, redirect, request, flash
from flask_mysqldb import MySQL
from SSIS.models.student import Student
from SSIS.models.course import Course
from SSIS.models.college import College
from . import courses



