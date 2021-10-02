from flask import Flask, render_template, url_for, redirect, request, flash

app = Flask(__name__)

@app.route('/')
def Index():
    return render_template('index.html')


@app.route('/course')
def course():
    return render_template('course.html')

@app.route('/college')
def college():
    return render_template('college.html')

if __name__=="__main__":
    app.run(debug=True)