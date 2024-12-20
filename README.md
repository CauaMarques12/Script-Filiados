# AUTOMAÇÃO DROGARAIA
 Script para automatizar os filiados para importação no sistema drogaraia


## 🐍 **Automatização de Execução de Script Python no Windows**

Este projeto tem como objetivo automatizar a execução de um script Python diariamente usando o **Agendador de Tarefas do Windows (Task Scheduler)**. Ideal para tarefas recorrentes como consultas a bancos de dados e geração de relatórios.


---

### 🛠️ **Pré-requisitos**

Antes de começar, você precisa ter os seguintes itens instalados no seu sistema:

1. **Python** (versão 3.7 ou superior):  
   [Download Python](https://www.python.org/downloads/)

2. **Bibliotecas Python Necessárias**:

   Instale as dependências do projeto usando `pip`:

   ```
   pip install pyodbc pandas python-dotenv SQLAlchemy schedule
   ```

---

### ⚙️ **Configurar Variáveis de Ambiente**

Crie um arquivo `.env` na pasta raiz do projeto e adicione as configurações de conexão com o banco de dados:

```plaintext
SERVER=
DATABASE=
USERNAME=seu_usuario
PASSWORD=sua_senha
```


---

### 🗓️ **Agendando o Script com o Agendador de Tarefas do Windows**

Siga os passos abaixo para agendar a execução automática do script.

1. **Abra o Agendador de Tarefas**:
   
   - Pressione `Win + R`, digite `taskschd.msc` e pressione **Enter**.

2. **Crie uma Nova Tarefa Básica**:

   - Clique em **"Criar Tarefa Básica..."**.

3. **Defina o Nome e a Descrição**:
   
   - **Nome**: `Executar Script Python`
   - **Descrição**: `Executa o script consulta_filiados.py diariamente.`

4. **Defina a Frequência**:
   
   - Escolha **"Diariamente"** e clique em **"Avançar"**.

5. **Defina o Horário de Execução**:
   
   - Escolha a hora desejada (por exemplo, `07:00`) e clique em **"Avançar"**.

6. **Selecione a Ação**:
   
   - Escolha **"Iniciar um Programa"** e clique em **"Avançar"**.

7. **Configurar o Programa a Ser Executado**:

   - **Programa/script**: Insira o caminho completo para o `python.exe`. Exemplo:
     ```plaintext
     C:\Python39\python.exe
     ```

   - **Adicionar argumentos**: Insira o caminho completo para o script. Exemplo:
     ```plaintext
     C:\Users\14749431605\Downloads\DROGARAIA\consulta_filiados.py
     ```

   - **Iniciar em (opcional)**: Pasta onde o script está localizado:
     ```plaintext
     C:\Users\14749431605\Downloads\DROGARAIA
     ```

8. **Concluir a Tarefa**:

   - Revise as configurações e clique em **"Concluir"**.

---

### ✅ **Testando a Tarefa**

1. No Agendador de Tarefas, clique com o botão direito na tarefa criada.
2. Selecione **"Executar"**.
3. Verifique se o arquivo CSV é gerado corretamente na pasta especificada.

---

### 🛠️ **Configurações Adicionais**

- **Executar mesmo quando o usuário estiver desconectado**:
  - Abra as propriedades da tarefa, vá até a aba **"Segurança"** e marque **"Executar estando o usuário conectado ou não"**.
- **Executar com privilégios mais altos** (se necessário).

