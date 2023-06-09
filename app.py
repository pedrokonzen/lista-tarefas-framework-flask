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

    # Lógica para adicionar a tarefa ao banco de dados ou à lista de tarefas existente
    return redirect('/')

@app.route('/update_task/<int:task_id>', methods=['POST'])
def update_task(task_id):
    task = request.form['task']
    tasks[task_id] = task

    # Lógica para atualizar a tarefa no banco de dados ou na lista de tarefas existente
    return redirect('/')

@app.route('/delete_task/<int:task_id>', methods=['GET', 'POST'])
def delete_task(task_id):
    del tasks[task_id]
    return redirect('/')


if __name__ == '__main__':
    app.run()