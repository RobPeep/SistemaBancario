# Sistema Bancario com Python

Este é um projeto simples de um sistema bancário feito em Python, desenvolvido como desafio para praticar estruturas de controle, laços e manipulação de variáveis.

## Funcionalidades

O sistema permite ao usuário realizar as seguintes operações:

- **D - Depositar**: adiciona um valor positivo ao saldo.
- **S - Sacar**: permite até 3 saques diários de no máximo R$ 500 por operação, desde que haja saldo suficiente.
- **E - Extrato**: exibe todas as movimentações realizadas (depósitos e saques), bem como o saldo atual.
- **Q - Sair**: encerra o programa.

## Regras de Negócio

- Depósitos só aceitam valores **positivos**.
- Saques:
  - Permitidos apenas até **3 por dia**.
  - O valor de cada saque não pode ultrapassar **R$ 500,00**.
  - O saque não pode ser feito se o saldo for **insuficiente**.
- O extrato lista todas as movimentações. Caso não haja movimentações, exibe uma mensagem informativa.
- Todos os valores são exibidos no formato `R$ xxx.xx`.

## Tecnologias Utilizadas

- Linguagem: **Python 3**
- Ferramentas: Nenhuma biblioteca externa — apenas **funções nativas** da linguagem

## Conceitos Praticados

- `if / elif / else`
- `while True`
- Manipulação de strings (`f-strings`)
- Operadores lógicos e condicionais
- Validação de dados do usuário

##  Como executar

1. Certifique-se de que o **Python 3** está instalado na sua máquina.
2. Clone este repositório ou copie o código-fonte para um arquivo `banco.py`.
3. Execute o arquivo no terminal ou em uma IDE:

