# app.py

from flask import Flask, render_template, request, redirect, url_for
from student import Student, students

app = Flask(__name__)

# Route pour afficher tous les étudiants
@app.route('/')
def index():
    return render_template('index.html', students=students)

# Route pour ajouter un nouvel étudiant
@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        student_id = request.form['student_id']
        name = request.form['name']
        age = request.form['age']
        new_student = Student(student_id, name, int(age))
        students.append(new_student)
        return redirect(url_for('index'))
    return render_template('add_student.html')

# Route pour afficher les détails d'un étudiant et ajouter une note
@app.route('/student/<student_id>', methods=['GET', 'POST'])
def student_detail(student_id):
    student = next((s for s in students if s.student_id == student_id), None)
    if request.method == 'POST':
        grade = float(request.form['grade'])
        student.add_grade(grade)
    return render_template('student_detail.html', student=student)

# Route pour modifier les informations d'un étudiant
@app.route('/edit/<student_id>', methods=['GET', 'POST'])
def edit_student(student_id):
    student = next((s for s in students if s.student_id == student_id), None)
    if request.method == 'POST':
        student.name = request.form['name']
        student.age = int(request.form['age'])
        return redirect(url_for('index'))
    return render_template('edit_student.html', student=student)

# Route pour supprimer un étudiant
@app.route('/delete/<student_id>')
def delete_student(student_id):
    global students
    students = [s for s in students if s.student_id != student_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
