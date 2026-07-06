"""
dados.py

Arquivo responsável por armazenar todas as informações utilizadas
pelo sistema PyLearning.
"""

# ==========================
# CONCEITOS DE PYTHON
# ==========================

conceitos = {

    # ==========================
    # CONCEITOS BÁSICOS
    # ==========================

    "variáveis": """
O que são?

Variáveis são espaços na memória utilizados para armazenar informações durante a execução de um programa.

Quando utilizar?

Sempre que for necessário guardar um valor para utilizá-lo posteriormente.

Exemplo:

nome = "Gabriela"
idade = 29

print(nome)
print(idade)

Saída:

Gabriela
20
""",

    "input": """
O que é?

A função input() permite que o usuário digite informações durante a execução do programa.

Quando utilizar?

Sempre que o programa precisar receber dados do usuário.

Exemplo:

nome = input("Digite seu nome: ")

print("Olá,", nome)

Saída:

Digite seu nome: Gabriela
Olá, Gabriela
""",

    "print": """
O que é?

A função print() é utilizada para exibir informações na tela.

Quando utilizar?

Sempre que desejar mostrar mensagens, resultados ou valores ao usuário.

Exemplo:

print("Bem-vindo ao PyLearning!")

Saída:

Bem-vindo ao PyLearning!
""",

    "comentários": """
O que são?

Comentários são trechos do código que não são executados pelo Python.

Quando utilizar?

Para explicar partes importantes do programa e facilitar sua manutenção.

Exemplo:

# Exibe uma mensagem na tela
print("Olá!")

Saída:

Olá!
""",

    # ==========================
    # ESTRUTURAS CONDICIONAIS
    # ==========================

    "if": """
O que é?

A estrutura if é utilizada para tomar decisões no programa com base em uma condição.

Quando utilizar?

Sempre que for necessário executar um bloco de código apenas se algo for verdadeiro.

Exemplo:

idade = 18

if idade >= 18:
    print("Maior de idade")

Saída:

Maior de idade
""",

    "elif": """
O que é?

A estrutura elif permite testar múltiplas condições em sequência.

Quando utilizar?

Quando houver mais de duas possibilidades de decisão.

Exemplo:

nota = 7

if nota >= 9:
    print("Excelente")
elif nota >= 6:
    print("Aprovado")
else:
    print("Reprovado")

Saída:

Aprovado
""",

    "else": """
O que é?

A estrutura else executa um bloco de código quando nenhuma condição anterior é verdadeira.

Quando utilizar?

Quando for necessário definir uma ação padrão.

Exemplo:

idade = 15

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

Saída:

Menor de idade
""",

    # ==========================
    # LAÇOS DE REPETIÇÃO
    # ==========================

    "while": """
O que é?

O while é um laço de repetição que executa um bloco enquanto uma condição for verdadeira.

Quando utilizar?

Quando não se sabe exatamente quantas vezes o bloco será repetido.

Exemplo:

contador = 1

while contador <= 5:
    print(contador)
    contador += 1

Saída:

1
2
3
4
5
""",

    "for": """
O que é?

O for é um laço de repetição utilizado para percorrer sequências.

Quando utilizar?

Quando já se sabe a quantidade de repetições ou ao percorrer listas.

Exemplo:

for i in range(1, 6):
    print(i)

Saída:

1
2
3
4
5
""",

    "break": """
O que é?

O break interrompe imediatamente um laço de repetição.

Quando utilizar?

Quando for necessário parar o loop antes do fim.

Exemplo:

for i in range(10):
    if i == 5:
        break
    print(i)

Saída:

0
1
2
3
4
""",

    "continue": """
O que é?

O continue faz o loop pular a iteração atual e seguir para a próxima.

Quando utilizar?

Quando quiser ignorar um valor específico dentro do loop.

Exemplo:

for i in range(5):
    if i == 2:
        continue
    print(i)

Saída:

0
1
3
4
""",

    "range": """
O que é?

A função range() gera uma sequência de números.

Quando utilizar?

Principalmente em loops for.

Exemplo:

for i in range(1, 6):
    print(i)

Saída:

1
2
3
4
5
""",

    # ==========================
    # FUNÇÕES
    # ==========================

    "funções": """
O que são?

Funções são blocos de código reutilizáveis que executam tarefas específicas.

Quando utilizar?

Quando quiser evitar repetição de código e organizar melhor o programa.

Exemplo:

def saudacao(nome):
    print("Olá,", nome)

saudacao("Gabriela")

Saída:

Olá, Gabriela
""",

    "return": """
O que é?

O return é usado para fazer uma função devolver um valor.

Quando utilizar?

Quando for necessário armazenar ou reutilizar o resultado de uma função.

Exemplo:

def soma(a, b):
    return a + b

resultado = soma(5, 3)
print(resultado)

Saída:

8
""",

    # ==========================
    # ESTRUTURAS DE DADOS
    # ==========================

    "listas": """
O que são?

Listas são estruturas que armazenam múltiplos valores em uma única variável.

Quando utilizar?

Quando for necessário trabalhar com vários dados juntos.

Exemplo:

frutas = ["maçã", "banana", "laranja"]

print(frutas)
print(frutas[0])

Saída:

['maçã', 'banana', 'laranja']
maçã
""",

    "tuplas": """
O que são?

Tuplas são semelhantes às listas, mas não podem ser alteradas.

Quando utilizar?

Quando os dados não devem ser modificados.

Exemplo:

cores = ("azul", "verde", "vermelho")

print(cores[1])

Saída:

verde
""",

    "dicionários": """
O que são?

Dicionários armazenam dados em pares de chave e valor.

Quando utilizar?

Quando cada informação precisa de uma identificação específica.

Exemplo:

aluno = {
    "nome": "Gabriela",
    "idade": 20
}

print(aluno["nome"])

Saída:

Gabriela
""",

    # ==========================
    # MANIPULAÇÃO DE LISTAS
    # ==========================

    "append": """
O que é?

O append adiciona um novo elemento ao final de uma lista.

Quando utilizar?

Quando quiser inserir novos dados em uma lista.

Exemplo:

nomes = ["Ana", "Carlos"]
nomes.append("Maria")

print(nomes)

Saída:

['Ana', 'Carlos', 'Maria']
""",

    "remove": """
O que é?

O remove elimina um elemento específico de uma lista.

Quando utilizar?

Quando quiser remover um valor conhecido.

Exemplo:

cores = ["azul", "verde", "vermelho"]
cores.remove("verde")

print(cores)

Saída:

['azul', 'vermelho']
""",

    "len": """
O que é?

A função len retorna a quantidade de elementos de uma estrutura.

Quando utilizar?

Quando quiser saber o tamanho de listas, strings ou tuplas.

Exemplo:

nome = "Python"

print(len(nome))

Saída:

6
""",

    # ==========================
    # OPERADORES
    # ==========================

    "operações matemáticas": """
O que são?

São operações básicas realizadas com números.

Operadores:

+ soma
- subtração
* multiplicação
/ divisão
// divisão inteira
% resto da divisão
** potência

Exemplo:

a = 10
b = 3

print(a + b)
print(a % b)

Saída:

13
1
""",

    "operadores relacionais": """
O que são?

São operadores usados para comparar valores.

Operadores:

== igual
!= diferente
>
<
>=
<=

Exemplo:

idade = 18

print(idade >= 18)

Saída:

True
""",

    "operadores lógicos": """
O que são?

São operadores usados para combinar condições.

Operadores:

and
or
not

Exemplo:

idade = 18
tem_carteira = True

if idade >= 18 and tem_carteira:
    print("Pode dirigir")

Saída:

Pode dirigir
""",

    # ==========================
    # MÓDULOS E BIBLIOTECAS
    # ==========================

    "import": """
O que é?

O import permite utilizar bibliotecas e módulos externos no programa.

Quando utilizar?

Sempre que precisar de funcionalidades prontas do Python.

Exemplo:

import random

print(random.randint(1, 10))

Saída:

Um número aleatório entre 1 e 10
""",

    "random": """
O que é?

A biblioteca random é usada para gerar valores aleatórios.

Quando utilizar?

Em jogos, sorteios, quizzes e seleção de dados aleatórios.

Exemplo:

import random

numero = random.randint(1, 100)

print(numero)

Saída:

Um número aleatório entre 1 e 100
""",

    "datetime": """
O que é?

A biblioteca datetime permite trabalhar com datas e horários.

Quando utilizar?

Para registrar horários, criar logs ou controlar tempo.

Exemplo:

from datetime import datetime

agora = datetime.now()

print(agora)

Saída:

Data e hora atual do sistema
""",

    "os": """
O que é?

A biblioteca os permite interagir com o sistema operacional.

Quando utilizar?

Para manipular arquivos e verificar diretórios.

Exemplo:

import os

if os.path.exists("historico.txt"):
    print("Arquivo existe")

Saída:

Arquivo existe
""",

    # ==========================
    # TRATAMENTO DE ERROS
    # ==========================

    "try": """
O que é?

O try é usado para tratar erros que podem acontecer durante a execução do programa.

Quando utilizar?

Sempre que houver risco de erro em entradas do usuário ou operações.

Exemplo:

try:
    numero = int(input("Digite um número: "))
except ValueError:
    print("Digite apenas números")

Saída:

(depende da entrada do usuário)
""",

    # ==========================
    # MANIPULAÇÃO DE ARQUIVOS
    # ==========================

    "arquivos": """
O que são?

Arquivos permitem salvar informações de forma permanente no computador.

Quando utilizar?

Quando for necessário armazenar dados mesmo após fechar o programa.

Exemplo:

with open("historico.txt", "a") as arquivo:
    arquivo.write("Novo registro\\n")

Saída:

Texto salvo no arquivo historico.txt
"""

}

# ==========================
# EXERCÍCIOS
# ==========================

exercicios = {
    "fácil": [
        "Crie um programa que leia o nome do usuário e exiba uma saudação.",
        "Leia dois números e mostre a soma entre eles.",
        "Peça a idade de uma pessoa e informe se ela é maior de idade."
    ],

    "médio": [
        "Crie um programa que leia cinco números e mostre o maior deles.",
        "Faça um programa utilizando while para contar de 1 até 20.",
        "Crie uma função que receba dois números e retorne o maior."
    ],

    "difícil": [
        "Desenvolva um sistema simples de cadastro utilizando listas.",
        "Crie um programa que leia nomes até o usuário digitar 'sair'.",
        "Implemente uma calculadora utilizando funções."
    ]
}

# ==========================
# DESAFIOS
# ==========================

desafios = [
    "Crie um programa que descubra se um número é primo.",
    "Desenvolva um jogo de adivinhação.",
    "Faça um sistema de notas utilizando listas.",
    "Implemente um menu utilizando while True.",
    "Crie um programa que ordene uma lista sem utilizar sort()."
]

# ==========================
# QUIZ
# ==========================

quiz = [

    {
        "pergunta": "Qual função é utilizada para exibir informações na tela?",

        "alternativas": [
            "A) input()",
            "B) print()",
            "C) len()",
            "D) type()"
        ],

        "resposta": "B"
    },

    {
        "pergunta": "Qual estrutura é utilizada para repetição?",

        "alternativas": [
            "A) if",
            "B) else",
            "C) while",
            "D) break"
        ],

        "resposta": "C"
    },

    {
        "pergunta": "Qual estrutura armazena vários elementos em Python?",

        "alternativas": [
            "A) Lista",
            "B) Float",
            "C) Boolean",
            "D) String"
        ],

        "resposta": "A"
    }

]

# ==========================
# PLANOS DE ESTUDO
# ==========================

planos_estudo = {

    "iniciante": [
        "Estudar variáveis",
        "Aprender operadores",
        "Praticar condicionais",
        "Resolver exercícios básicos"
    ],

    "intermediário": [
        "Estudar funções",
        "Aprender listas",
        "Praticar dicionários",
        "Resolver desafios intermediários"
    ],

    "avançado": [
        "Estudar módulos",
        "Manipulação de arquivos",
        "Tratamento de exceções",
        "Desenvolver projetos completos"
    ]

}