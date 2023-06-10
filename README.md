Lista de Tarefas com Flask. 

A aplicação "Lista de Tarefas com Flask" é um projeto web simples que permite aos usuários 
criar, atualizar, concluir e excluir tarefas em uma lista. A aplicação foi construída utilizando 
o framework Flask, que é um framework leve e flexível em Python para desenvolvimento web.

Funcionalidades Principais
- Adicionar tarefas: Os usuários podem digitar o nome de uma tarefa em um campo de entrada e clicar no botão "Adicionar" para adicioná-la à lista de tarefas.
- Atualizar tarefas: Ao lado de cada tarefa, há um botão de edição. Ao clicar nesse botão, a tarefa se torna editável e o usuário pode fazer alterações no seu conteúdo.
- Concluir tarefas: Cada tarefa possui um botão de conclusão (representado por um ícone de certo). Ao clicar nesse botão, a tarefa é marcada como concluída e seu texto é exibido em verde.
- Cancelar tarefas: As tarefas concluídas podem ser revertidas para o estado não concluído clicando no botão de cancelamento (representado por um ícone de errado). Ao clicar nesse botão, seu texto é exibido em vermelho.
- Excluir tarefas: Ao lado de cada tarefa, há um botão de exclusão (representado por um ícone de lixeira). Ao clicar nesse botão, a tarefa é removida permanentemente da lista.

Execução do Projeto
Para executar o projeto, siga os seguintes passos:

- Python: Certifique-se de ter o Python instalado no seu sistema. O projeto foi desenvolvido em Python 3.
- Ambiente Virtual (opcional): É recomendado, mas não obrigatório, criar um ambiente virtual para isolar as dependências do projeto. Você pode usar ferramentas como o venv ou o virtualenv para criar um ambiente virtual.
- Dependências: Instale as dependências necessárias do projeto. Você pode fazer isso utilizando o arquivo requirements.txt fornecido. Execute o seguinte comando para instalar as dependências:

pip install -r requirements.txt

- Executar o aplicativo: Para rodar o projeto, execute o arquivo app.py com o seguinte comando:

python app.py

- Acesso à aplicação: Após executar o aplicativo, abra um navegador da web e acesse o endereço http://localhost:5000. A página da lista de tarefas será exibida, e você poderá interagir com as funcionalidades fornecidas.
