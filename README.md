# Sistema Bancário com Python

Este é um projeto de um sistema bancário simples, desenvolvido em **Python** como prática de lógica de programação, estruturas de controle, funções e organização de código.

Esta versão simula uma estrutura básica de banco, com suporte a múltiplos **usuários** e **contas bancárias**.

---

## Funcionalidades

O sistema permite ao usuário realizar as seguintes operações:

- `[d]` Depositar  
- `[s]` Sacar  
- `[e]` Exibir extrato  
- `[nu]` Criar novo usuário  
- `[nc]` Criar nova conta  
- `[lc]` Listar contas existentes  
- `[q]` Sair do sistema

---

## Regras de Negócio

### Depósitos

- Apenas valores **positivos** são aceitos.
- O valor é somado ao saldo e registrado no extrato da conta.

### Saques

- Cada usuário pode realizar até **3 saques por dia**.
- O valor de cada saque não pode ultrapassar **R$ 500,00**.
- Saques não são permitidos caso o **saldo seja insuficiente**.

### Extrato

- Lista todas as movimentações da conta (depósitos e saques).
- Caso não haja movimentações, exibe uma mensagem apropriada.
- Mostra o **saldo atual** formatado em `R$ xxx.xx`.

### Usuários e Contas

- Cada **usuário é identificado por CPF** (não pode haver duplicidade).
- Uma conta só pode ser criada para um **usuário já existente**.
- Cada conta possui número, agência e está associada a um usuário.

---

## Tecnologias Utilizadas

- Linguagem: **Python 3**
- Bibliotecas externas: **Nenhuma**
- Entrada e saída de dados: via **terminal (CLI)**

---

## Conceitos Praticados

- Estruturas de controle (`if`, `elif`, `else`)
- Repetição com `while`
- Manipulação de strings e formatação com `f-strings`
- Parâmetros posicionais e nomeados em funções
- Listas, dicionários e operações com coleções
- Organização de código em funções reutilizáveis

---

## Como Executar

1. Certifique-se de que o **Python 3** está instalado em sua máquina.
2. Copie o código-fonte para um arquivo chamado `sistema_bancario.py`.
3. No terminal ou prompt de comando, execute:

```bash
python banco.py
```
