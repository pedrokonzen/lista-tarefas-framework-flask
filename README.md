Lista de Tarefas com Flask. 

A aplicação "Lista de Tarefas com Flask" é um projeto web simples que permite aos usuários 
criar, atualizar, concluir e excluir tarefas em uma lista. A aplicação foi construída utilizando 
o framework Flask, que é um framework leve e flexível em Python para desenvolvimento web, juntamente com um página html simples sobre Frameworks em geral.

Funcionalidades Principais
- Adicionar tarefas: Os usuários podem digitar o nome de uma tarefa em um campo de entrada e clicar no botão "Adicionar" para adicioná-la à lista de tarefas.
- Atualizar tarefas: Ao lado de cada tarefa, há um botão de edição. Ao clicar nesse botão, a tarefa se torna editável e o usuário pode fazer alterações no seu conteúdo.
- Concluir tarefas: Cada tarefa possui um botão de conclusão (representado por um ícone de certo). Ao clicar nesse botão, a tarefa é marcada como concluída e seu texto é exibido em verde.
- Cancelar tarefas: As tarefas concluídas podem ser revertidas para o estado não concluído clicando no botão de cancelamento (representado por um ícone de errado). Ao clicar nesse botão, seu texto é exibido em vermelho.
- Excluir tarefas: Ao lado de cada tarefa, há um botão de exclusão (representado por um ícone de lixeira). Ao clicar nesse botão, a tarefa é removida permanentemente da lista.

- Ao seguir o link "Clique aqui para ver o relatório sobre Frameworks", segue para a página destinada ao Relatório sobre Frameworks.



Execução do Projeto
Para executar o projeto, siga os seguintes passos:

- Python: Certifique-se de ter o Python instalado no seu sistema. O projeto foi desenvolvido em Python 3.
- Ambiente Virtual (opcional): É recomendado, mas não obrigatório, criar um ambiente virtual para isolar as dependências do projeto. Você pode usar ferramentas como o venv ou o virtualenv para criar um ambiente virtual.

python3 -m venv venv

- Dependências: Instale as dependências necessárias do projeto. Execute o seguinte comando para instalar o flask:

pip install flask

- Executar o aplicativo: Para rodar o projeto, no terminal execute o seguinte comando:

flask run

- Acesso à aplicação: Após executar o aplicativo, abra um navegador da web e acesse o endereço http://localhost:5000. A página da lista de tarefas será exibida, e você poderá interagir com as funcionalidades fornecidas.
