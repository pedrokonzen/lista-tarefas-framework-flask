from flask import Flask, redirect, render_template, request

app = Flask(__name__)

tasks = []  # Lista de tarefas (inicialmente vazia)
    
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form['task']
    tasks.append(task)


if __name__ == '__main__':
    app.run()