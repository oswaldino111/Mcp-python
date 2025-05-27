Bem-vindo ao projeto MCP
Este é um exemplo de servidor MCP com integração ao Open AI usando SQLite para busca de carros.
Como usar
1. Criar ambiente virtual
python -m venv .carros

2. Ativar ambiente virtual

No Windows:

.carros\Scripts\activate


No macOS/Linux:

source .venv/bin/activate

3. Instale as dependências
pip install -r requirements.txt  # instalar no ambiente virtual

4. Gere os dados de exemplo
python main_carga_dados.py

5. Substitua no .env sua key do ChatGpt

6. Inicie o servidor MCP
python server.py

7. Em outro terminal, inicie o cliente
python main.py

8. Para encerrar
Pressione as teclas: Ctrl + C

9. Para testes
Na raiz do projeto, execute:
python -m testes.main

Estrutura do Banco de Dados

id: Integer
marca: String
ano: Integer
modelo: String
cor: String
quilometragem: Integer
quantidade_portas: Integer
chassi: String
propulsao: String
lugares: Integer
cambio: String

