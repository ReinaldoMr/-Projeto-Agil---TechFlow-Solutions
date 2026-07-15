from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tarefas = []

#retorna a intex para exporta
@app.route('/')
def home():
    return render_template('index.html', tarefas=tarefas)

#rota para adicionar tarefa
@app.route('/adicionar', methods=['POST'])
def adicionar():

    titulo = request.form['titulo']
    descricao = request.form['descricao']

    tarefas.append({
        'id': len(tarefas),
        'titulo': titulo,
        'descricao': descricao,
        'status': 'Pendente'
    })

    return redirect('/')

#rota para editar tarefa
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):

    for tarefa in tarefas:
        if tarefa['id'] == id:

            if request.method == 'POST':
                tarefa['titulo'] = request.form['titulo']
                tarefa['descricao'] = request.form['descricao']

                return redirect('/')

            return f'''
            <h1>Editar Tarefa</h1>

            <form method="POST">
                <input type="text" name="titulo" value="{tarefa['titulo']}" required>
                <br><br>

                <textarea name="descricao">{tarefa['descricao']}</textarea>
                <br><br>

                <button type="submit">Salvar Alterações</button>
            </form>
            ''' 
            
#rota para Excluir uma tarefa            
@app.route('/excluir/<int:id>')
def excluir(id):
    global tarefas

    tarefas = [tarefa for tarefa in tarefas if tarefa['id'] != id]

    return redirect('/')


#rota para concluir uma tarefa 
@app.route('/concluir/<int:id>')
def concluir(id):

    for tarefa in tarefas:
        if tarefa['id'] == id:
            tarefa['status'] = 'Concluída'

    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)