# Problema 1

Para resolver o teste proposto pela EDS, estarei utilizando o banco de dados SQLITE, na extensão do VSCODE.
Essa decisão foi tomada já que a base (SQLITE) é ideal para projetos pequenos, além de preferência pessoal.

Primeiramente, criarei várias tabelas de dados dos três hospitais, já que o SQLITE não suporta a criação de schemas.

```sql
-- Cada tabela é criada na mesma estrutura de um schema, com a adaptação necessária ao final

CREATE TABLE stg_hospital_a_pacientes(
-- PRIMARY KEY garante que cada id será único (sem repetição)

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    dt_nascimento DATE NOT NULL,
    cpf INTEGER NOT NULL,
    nome_mae TEXT, 
    dt_atualizacao TIMESTAMP
-- TIMESTAMP foi usado ao invés de DATE, pois deve suportar data/hora
);

CREATE TABLE stg_hospital_b_pacientes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    dt_nascimento DATE NOT NULL,
    cpf INTEGER NOT NULL,
    nome_mae TEXT, 
    dt_atualizacao TIMESTAMP
);

CREATE TABLE stg_hospital_c_pacientes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    dt_nascimento DATE NOT NULL,
    cpf INTEGER NOT NULL,
    nome_mae TEXT, 
    dt_atualizacao TIMESTAMP

);
```

Após a criação das tabelas de dados de cada hospital, basta criar a tabela stg_prontuario, que abrigará dados de todos os pacientes

```sql
-- Terá, obviamente, a mesma estrutura de dados das tabelas dos hospitais.

CREATE TABLE stg_prontuario_PACIENTE(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    dt_nascimento DATE NOT NULL,
    cpf INTEGER NOT NULL,
    nome_mae TEXT, 
    dt_atualizacao TIMESTAMP

)
```
Com as tabelas criadas, devemos criar dados para cada uma delas. Não há necessidade de especificar o id na inserção dos mesmos
Para facilitar, usei o chatGPT para gerar os dados.

```sql

INSERT INTO stg_hospital_a(nome,dt_nascimento,cpf,nome_mae,dt_atualizacao)
VALUES("Lucas Pereira", "2000-01-01", 12345678912, "Gertrudes", "2025-01-07 13:59:55"),
      ("Mariana Silva", "1995-07-12", 23456789012, "Bruna", "2025-01-02 09:30:45"),
      ("João Oliveira", "1988-03-25", 56789123456, "Fernanda", "2025-01-03 15:45:03"),
      ("Mari Silv", "1995-07-12", 23456789012, "Bruna", "2025-01-05 04:35:30"),
      ("Lucas P", "2000-01-01", 12345678912, "Gertrudes", "2025-01-01 02:00:23");

INSERT INTO stg_hospital_b(nome,dt_nascimento,cpf,nome_mae,dt_atualizacao)
VALUES("Aline Costa", "1999-11-23", 35178264019, "Roberta", "2025-01-06 04:05:50"),
  ("Bruno Rocha", "1990-07-30", 60481329754, "Helena", "2025-01-09 18:15:05"),
  ("A Costa", "1999-11-23", 35178264019, "Roberta", "2025-05-06 03:45:40"),
  ("Rafael Mendes", "1996-03-18", 18230745961, "Simone", "2025-01-05 00:11:29");

INSERT INTO stg_hospital_c(nome,dt_nascimento,cpf,nome_mae,dt_atualizacao)
VALUES("Fernanda Dias", "1987-12-01", 50923687144, "Eliane", "2025-01-10 14:53:00"),
  ("Carlos Henrique", "1993-05-05", 37094218625, "Lúcia", "2025-01-07 09:47:18"),
  ("Tatiane Freitas", "1998-10-27", 61478230597, "Regina", "2025-01-01 19:08:22"),
  ("Tati F", "1998-10-27", 61478230597, "Regina", "2025-01-01 01:54:27");

```
# Problema 2
Após a inserção dos dados, devemos juntar todos eles na tabela stg_prontuario_PACIENTE, utilizando o seguinte código:

```sql

INSERT INTO stg_prontuario_PACIENTE(nome,dt_nascimento,cpf,nome_mae, dt_atualizacao)
SELECT nome,dt_nascimento,cpf,nome_mae, dt_atualizacao FROM stg_hospital_a
UNION
SELECT nome,dt_nascimento,cpf,nome_mae, dt_atualizacao FROM stg_hospital_b
UNION
SELECT nome,dt_nascimento,cpf,nome_mae, dt_atualizacao FROM stg_hospital_c;
-- O UNION serve para remover linhas duplicadas (exatamente iguais)

```
# Problema 3

Para verificar a quantidade de valores duplicados, usei como base o CPF, já que é único de cada pessoa.
```sql

-- o COUNT faz a contagem de cada cpf e retorna em "quantidade"
SELECT cpf, COUNT(*) AS "quantidade"
FROM stg_prontuario_PACIENTE
GROUP BY cpf
HAVING COUNT (*)> 1
ORDER BY Count(*) DESC;
-- HAVING COUNT garante que só serão exibidos CPFs repetidos (2 aparições ou mais) 
-- Esse último comando ordena os CPFs que mais aparecem em ordem decrescente (maior para o menor)

```

![image](https://github.com/user-attachments/assets/0ae2df4b-09fc-4c23-a04a-7599773cdb63)

# Problema 4

Agora, para cada conjunto de pacientes repetidos, precisamos retornar somente aqueles com data de atualização mais recente.
Para isso, utilizaremos o seguinte código:
```sql

-- O p.* é um nome para a tabela, dado mais abaixo. O comando [apelido].* Puxa todos os elementos dela (nome, cpf...)
SELECT p.*
FROM stg_prontuario_PACIENTE p
INNER JOIN (
    SELECT cpf, MAX(dt_atualizacao) AS dt_atualizacao
    FROM stg_prontuario_PACIENTE
    GROUP BY cpf
    HAVING COUNT(*) > 1
-- A checagem retorna somente os CPFs duplicados e sua data de atualização

) dup ON p.cpf = dup.cpf AND p.dt_atualizacao = dup.dt_atualizacao;
--
-- O a última linha é uma condição: Somente juntar o resto dos dados ta tabela p se a data de atualização e CPF forem os mesmos
-- Retorna somente as pessoas com CPFs duplicados  
```
![image](https://github.com/user-attachments/assets/b2eb2d95-a3e7-4cc3-aee4-dd1378c8124b)

![image](https://github.com/user-attachments/assets/08656b86-1fa8-4b3b-9c79-37cae77d100f)


# Problema 5
Incompleto

## [Solução](https://github.com/LucasPy1/DesafioEDS/blob/ea30ae024ca45a934ae91b4e62dc7d3e7c8f946b/Problemas_codigos/problema5.py)

O mesmo processo se repetirá para os outros arquivos. Para resolver esse desafio, basta ler todos os arquivos da pasta sigtap que têm o nome layout. Com isso, é possível saber em quais partes do texto (posição 1,2...) estarão os dados que precisamos. É possível, então, usar a função strip para extrair somente os dados que queremos, possibilitando a inserção dos mesmos no banco de dados. Após a limpeza dos dados, é necessário fazer a conexão com o banco de dados e criar as respectivas tabelas dos arquivos, as quais necessitam ter os mesmos atributos do arquivo original,  inserindo, por fim, os dados nelas.

# Problema 6

## [Resolução em Python](https://github.com/LucasPy1/DesafioEDS/blob/4849278e425355786560f5a460e9956c3abf93a4/Problemas_codigos/problema6.py)

![image](https://github.com/user-attachments/assets/370b6558-ae1c-4ee5-a979-209dd33b2810)

![image](https://github.com/user-attachments/assets/5b81cf6b-4e31-4154-b207-c661e0750e20)

# Problema 7

Eu modelaria a minha tabela da seguinte forma:
- Criação da tabela stg_atendimentos:

![image](https://github.com/user-attachments/assets/07d37edb-4b31-41be-a0ad-2f3ba25be90c)

> tp_atendimento -> tipo do atendimento

> dt_atendimento -> data do atendimento

- Criação da tabela stg_prescricao:

![image](https://github.com/user-attachments/assets/b90099b9-066c-44cb-9374-c17c67f94393)

> O uso de "FOREIGN KEY" atribui somente um atendimento a uma prescrição, evitando possíveis conflitos futuros


# Problema 8
Para calcular a média, primeiro devemos inserir dados de teste nas tabelas atendimento e prescrição, respectivamente:

![image](https://github.com/user-attachments/assets/3eefe8ad-d5a4-4937-b7b7-055800d97154)

![image](https://github.com/user-attachments/assets/70edf7ed-cdce-4c16-b78c-5ff1d2301154)

Depois, devemos criar a consulta SQL responsável por fazer o cálculo da média:

![image](https://github.com/user-attachments/assets/7785362f-505c-4c78-b4ff-3261ce789bc2)

Por fim, temos como resultado uma média de 2 medicamentos por atendimento de Urgência.

# Problema 9
Resolução do desafio 9, relativo à checagem de medicamentos prescritos e no estoque
## [Solução](https://github.com/LucasPy1/DesafioEDS/blob/3d19d2e3b2e5740246f7bf5e3f70a0fded8f0283/Problemas_codigos/problema9.py)

![image](https://github.com/user-attachments/assets/9949794d-3583-4e20-8aae-0763709dfd8e)


# Problema 10
## [Solução](https://github.com/LucasPy1/DesafioEDS/blob/ea30ae024ca45a934ae91b4e62dc7d3e7c8f946b/Problemas_codigos/problema10.py)

Resolução do último desafio(10), sobre a criação de gŕaficos com base no número de atendimentos. Para isso, usei a biblioteca matplotlib e montei um gráfico de colunas com as datas listadas no código. Abaixo, seguem 2 exemplos de gráficos com diferentes datas:

#### Exemplo 1

![image](https://github.com/user-attachments/assets/deb0bb52-2b21-4bd0-a591-97e5bf8ff400)

![image](https://github.com/user-attachments/assets/6b0620e0-59f8-4a39-baa5-79f58a01d7fb)

#### Exemplo 2

![image](https://github.com/user-attachments/assets/e578d7be-30cf-482c-a5f8-c7fb723a93c0)

![image](https://github.com/user-attachments/assets/03522456-9564-4006-8bfc-d95179f6e2cf)


Apesar de simples, esse gráfico seria um ótimo início para uma eventual análise de dados em um consultório, podendo medir seu desempenho e auxiliar na tomada de decisões administrativa.

Futuramente, tanto o banco de dados quanto o gráfico poderiam ser melhorados e integrados de forma a registrar os atendimentos automaticamente e exibir isso em um gráfico de colunas com uma maior, quantidade de dias, sendo um indicador mais preciso e eficiente.

# Referências
Abaixo, estão algumas referências usadas em problemas específicos e em outros.

Problema 1
https://www.sqlitetutorial.net/sqlite-date/
https://www.sqlitetutorial.net/sqlite-cheat-sheet/
https://www.geeksforgeeks.org/sqlite-insert-into-select/

Problema 3
https://database.guide/6-ways-to-select-duplicate-rows-in-sqlite/

Problema 4
https://stackoverflow.com/questions/22200587/get-records-for-the-latest-timestamp-in-sqlite

Problema 5
https://stackoverflow.com/questions/21546739/load-data-from-txt-with-pandas#21546823

Problema 6
https://www.sqlite.org/foreignkeys.html
https://stackoverflow.com/questions/1884818/how-do-i-add-a-foreign-key-to-an-existing-sqlite-table

chatgpt.com






