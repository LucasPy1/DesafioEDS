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
INSERT INTO stg_hospital_a(nome,dt_nascimento,cpf,nome_mae,dt_atualizacao)
VALUES("Lucas Pereira", "2000-01-01", 12345678912, "Gertrudes", "2025-01-07 13:59:55"),
      ("Mariana Silva", "1995-07-12", 23456789012, "Bruna", "2025-01-02 09:30:45"),
      ("João Oliveira", "1988-03-25", 56789123456, "Fernanda", "2025-01-03 15:45:03"),
      ("Mari Silv", "1995-07-12", 23456789012, "Bruna", "2025-01-05 04:35:30"),
      ("Lucas P", "2000-01-01", 12345678912, "Gertrudes", "2025-01-01 02:00:23");



