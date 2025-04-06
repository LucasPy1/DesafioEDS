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


