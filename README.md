
## 🐍 **Automatização de Execução de Script Python no Windows**

Este projeto tem como objetivo automatizar a execução de um script Python diariamente usando o **Agendador de Tarefas do Windows (Task Scheduler)**. Ele facilita tarefas recorrentes como consultas a bancos de dados e geração de relatórios dos filiados que realizaram adesão no dia anterior.

---

### 🛠️ **Pré-requisitos**

Antes de começar, você precisa ter os seguintes itens instalados no seu sistema:

1. **Python** (versão 3.7 ou superior):  
   [Download Python](https://www.python.org/downloads/)

2. **Bibliotecas Python Necessárias**:

   Instale as dependências do projeto usando o seguinte comando:

   ```bash
   pip install -r requirements.txt
   ```

---

### ⚙️ **Configuração do Projeto**

1. **Configurar Variáveis de Ambiente**:

   Crie um arquivo `.env` na pasta raiz do projeto e adicione as configurações de conexão com o banco de dados:

   ```plaintext
   SERVER=nome_do_servidor
   DATABASE=nome_do_banco
   USERNAME=seu_usuario
   PASSWORD=sua_senha
   ```

2. **Criação do Arquivo .bat**:

   Crie um arquivo `.bat` para facilitar a execução do script pelo Agendador de Tarefas. Exemplo do conteúdo do arquivo `.bat`:

   ```plaintext
   @echo off
   cd C:\Users\14749431605\Downloads\DROGARAIA
   python consulta_filiados.py
   ```

   - **Salvar o arquivo**: Nomeie o arquivo como `rodar_script.bat` e salve-o na mesma pasta do projeto.

---

### 🗓️ **Agendando o Script com o Agendador de Tarefas do Windows**

Use o arquivo `.bat` criado para agendar a execução do script automaticamente.

1. **Abra o Agendador de Tarefas**:
   
   - Pressione `Win + R`, digite `taskschd.msc` e pressione **Enter**.

2. **Crie uma Nova Tarefa Básica**:

   - Clique em **"Criar Tarefa Básica..."**.

3. **Defina o Nome e a Descrição**:
   
   - **Nome**: `Executar Script Python Drogaraia`
   - **Descrição**: `Executa o script consulta_filiados.py diariamente.`

4. **Defina a Frequência**:
   
   - Escolha **"Diariamente"** e clique em **"Avançar"**.

5. **Defina o Horário de Execução**:
   
   - Escolha a hora desejada (por exemplo, `07:00`) e clique em **"Avançar"**.

6. **Selecione a Ação**:
   
   - Escolha **"Iniciar um Programa"** e clique em **"Avançar"**.

7. **Configurar o Programa a Ser Executado**:

   - **Programa/script**: Insira o caminho completo para o arquivo `.bat`. Exemplo:
     ```plaintext
     C:\Users\14749431605\Downloads\DROGARAIA\rodar_script.bat
     ```

8. **Concluir a Tarefa**:

   - Revise as configurações e clique em **"Concluir"**.

---

### ✅ **Testando a Automação**

1. No Agendador de Tarefas, clique com o botão direito na tarefa criada.
2. Selecione **"Executar"**.
3. Verifique se o arquivo CSV foi gerado corretamente na pasta especificada.

---

### 🛠️ **Configurações Avançadas**

- **Executar mesmo quando o usuário estiver desconectado**:
  - Abra as propriedades da tarefa, vá até a aba **"Segurança"** e marque **"Executar estando o usuário conectado ou não"**.
- **Executar com privilégios mais altos**:
  - Marque a opção **"Executar com privilégios mais altos"** na aba **"Geral"**.

---

### 📂 **Estrutura do Projeto**

```plaintext
AUTOMAÇÃO DROGARAIA/
│
├── consulta_filiados.py      # Script principal
├── .env                      # Variáveis de ambiente
├── rodar_script.bat          # Script para automatização
├── requirements.txt          # Dependências do projeto
└── README.md                 # Documentação
```

