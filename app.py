from flask import Flask, render_template

app = Flask(__name__)

Students = [{'Name': 'A', 'Rollno': 1, 'Age': 10, 'Gender': 'Male'},
            {'Name': 'B', 'Rollno': 2, 'Age': 9, 'Gender': 'Female'}]


@app.route("/")
def index():
    return render_template("index.html", len=len(Students), Students=Students)


@app.route("/insert/")
def accept(Name='C', Rollno=3, Age=8, Gender='Female'):
    Students.append({'Name': Name, 'Rollno': Rollno, 'Age': Age, 'Gender': Gender})
    return "Student added"


@app.route("/search/")
def search(rn=1):
    for student in Students:
        if student['Rollno'] == rn:
            return "Student found"
        else:
            return "Student not found"


@app.route("/delete/")
def delete(Rollno=1):
    for student in Students:
        if student['Rollno'] == 1:
            del student
            return "Student deleted"
        else:
            return "Invalid entry"


@app.route("/update/")
def update(Rollno=1, Age=11):
    for student in Students:
        if student['Rollno'] == 1:
            student['Age'] = 11
            return "Student updated"
        else:
            return "Invalid entry"


if __name__ == "__main__":
    app.run(debug=True)


