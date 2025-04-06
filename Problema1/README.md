# Problema 1

Para resolver o teste proposto pela EDS, estarei utilizando o banco de dados SQLITE, na extensão do VSCODE.
Essa decisão foi tomada já que a base (SQLITE) é ideal para projetos pequenos, além de preferência pessoal.

Primeiramente, criarei várias tabelas de dados dos três hospitais, já que o SQLITE não suporta a criação de schemas.

```sql
-- Cada tabela é criada na mesma estrutura de um schema, com a adaptação necessária ao final

CREATE TABLE stg_hospital_a_pacientes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    dt_nascimento DATE NOT NULL,
    cpf INTEGER NOT NULL,
    nome_mae TEXT, 
    dt_atualizacao TIMESTAMP
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

