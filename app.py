from flask import Flask, redirect, render_template, request

app = Flask(__name__)

tasks = ["x" , "y" , "z"]  # Lista de tarefas (inicialmente vazia)
task_status = ["", "", ""]  # Lista de status das tarefas

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks, task_status=task_status)

@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form['task']
    tasks.append(task)
    task_status.append("")
    return redirect('/')

@app.route('/update_task/<int:index>', methods=['POST'])
def update_task(index):
    task = request.form['task']
    tasks[index] = task
    return redirect('/')

@app.route('/complete_task/<int:index>', methods=['POST'])
def complete_task(index):
    task_status[index] = "completed"
    return redirect('/')

@app.route('/cancel_task/<int:index>', methods=['POST'])
def cancel_task(index):
    task_status[index] = "cancelled"
    return redirect('/')

@app.route('/delete_task/<int:index>', methods=['POST'])
def delete_task(index):
    del tasks[index]
    del task_status[index]
    return redirect('/')

if __name__ == '__main__':
    app.run()
