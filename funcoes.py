"""
funcoes.py

Arquivo responsável por todas as funcionalidades do PyLearning.
"""

import random
from datetime import datetime

from dados import (
    conceitos,
    exercicios,
    desafios,
    quiz,
    planos_estudo
)

def cabecalho(titulo):
    print("\n" + "=" * 42)
    print(titulo)
    print("=" * 42)

def tirar_duvida():
    """
    Permite ao usuário fazer perguntas livres sobre Python.
    O sistema tenta identificar palavras-chave e retornar a explicação correspondente.
    """

    while True:

        cabecalho("TIRAR DÚVIDAS")

        print("\nDigite sua dúvida ou 'voltar' para retornar ao menu.")

        pergunta = input("\nSua dúvida: ").lower()

        if pergunta == "voltar":
            break

        resposta_encontrada = False

        palavras = pergunta.split()

        for palavra in palavras:
            if palavra in conceitos:
                print("\n" + "-" * 50)
                print(conceitos[palavra])
                print("-" * 50)
                resposta_encontrada = True
                break

        if not resposta_encontrada:
            print("\nNão encontrei uma resposta para essa dúvida.")
            print("Tente usar termos como: while, listas, funções, if, etc.")

def explicar_conceito():
    """
    Exibe conceitos de Python de forma organizada por categorias.
    """

    while True:

        cabecalho("📚 EXPLICAR CONCEITOS")

        print("\nEscolha um conceito para estudar:")
        print("Ou digite 'voltar' para retornar ao menu.\n")

        # Lista organizada por categorias

        print("CONCEITOS BÁSICOS")
        print("- variáveis | input | print | comentários\n")

        print("ESTRUTURAS CONDICIONAIS")
        print("- if | elif | else\n")

        print("LAÇOS DE REPETIÇÃO")
        print("- while | for | break | continue | range\n")

        print("FUNÇÕES E DADOS")
        print("- funções | return | listas | tuplas | dicionários\n")

        print("OPERADORES")
        print("- operações matemáticas | operadores relacionais | operadores lógicos\n")

        print("BIBLIOTECAS E OUTROS")
        print("- import | random | datetime | os | arquivos\n")

        escolha = input("\nDigite o conceito desejado: ").lower().strip()

        if escolha == "voltar":
            break

        if escolha in conceitos:
            print("\n" + "-" * 42)
            print(conceitos[escolha])
            print("-" * 42)
        else:
            print("\n⚠ Conceito não encontrado.")
            print("Tente digitar exatamente um dos nomes exibidos.")

def gerar_exercicio():
    """
    Gera exercícios de programação com base no nível escolhido pelo usuário.
    """

    while True:

        cabecalho("📝 GERAR EXERCÍCIOS")

        print("\nEscolha o nível do exercício:")
        print("1 - Fácil")
        print("2 - Médio")
        print("3 - Difícil")
        print("Digite 'voltar' para retornar ao menu.")

        escolha = input("\nSua escolha: ").lower().strip()

        if escolha == "voltar":
            break

        if escolha == "1":
            nivel = "fácil"
        elif escolha == "2":
            nivel = "médio"
        elif escolha == "3":
            nivel = "difícil"
        else:
            print("\n⚠ Opção inválida. Tente novamente.")
            continue

        if nivel in exercicios:
            exercicio = random.choice(exercicios[nivel])

            print("\n" + "-" * 42)
            print(f"📌 Exercício nível {nivel.upper()}")
            print("-" * 42)
            print(exercicio)
            print("-" * 42)

        else:
            print("\nNenhum exercício encontrado para esse nível.")

def corrigir_codigo():
    """
    Analisa o código informado pelo usuário procurando
    erros comuns de sintaxe e boas práticas.
    """

    while True:

        cabecalho("🔍 CORRIGIR CÓDIGO")

        print("Cole seu código Python.")
        print("Digite 'FIM' em uma linha separada para finalizar.")
        print("Digite 'voltar' para retornar ao menu.\n")

        linhas = []

        while True:

            linha = input()

            if linha.lower() == "voltar":
                return

            if linha.upper() == "FIM":
                break

            linhas.append(linha)

        codigo = "\n".join(linhas)

        cabecalho("ANÁLISE DO CÓDIGO")

        erros = []

        # -----------------------------------
        # PRINT
        # -----------------------------------

        if "print" not in codigo:
            erros.append("Não encontrei nenhuma chamada da função print().")

        # -----------------------------------
        # PARÊNTESES
        # -----------------------------------

        if codigo.count("(") != codigo.count(")"):
            erros.append("Quantidade de parênteses diferente. Verifique '(' e ')'.")

        # -----------------------------------
        # ASPAS
        # -----------------------------------

        if codigo.count('"') % 2 != 0:
            erros.append('Existe uma quantidade ímpar de aspas duplas.')

        if codigo.count("'") % 2 != 0:
            erros.append("Existe uma quantidade ímpar de aspas simples.")

        # -----------------------------------
        # ANÁLISE LINHA A LINHA
        # -----------------------------------

        for numero, linha in enumerate(linhas, start=1):

            texto = linha.strip()

            if not texto:
                continue

            # if

            if texto.startswith("if") and not texto.endswith(":"):
                erros.append(f"Linha {numero}: o comando if deve terminar com ':'.")

            # elif

            if texto.startswith("elif") and not texto.endswith(":"):
                erros.append(f"Linha {numero}: o comando elif deve terminar com ':'.")

            # else

            if texto.startswith("else") and not texto.endswith(":"):
                erros.append(f"Linha {numero}: o comando else deve terminar com ':'.")

            # while

            if texto.startswith("while") and not texto.endswith(":"):
                erros.append(f"Linha {numero}: o comando while deve terminar com ':'.")

            # for

            if texto.startswith("for") and not texto.endswith(":"):
                erros.append(f"Linha {numero}: o comando for deve terminar com ':'.")

            # def

            if texto.startswith("def") and not texto.endswith(":"):
                erros.append(f"Linha {numero}: a definição da função deve terminar com ':'.")

            # input

            if "input" in texto and "input(" not in texto:
                erros.append(f"Linha {numero}: possível erro na chamada da função input().")

            # print

            if "print" in texto and "print(" not in texto:
                erros.append(f"Linha {numero}: possível erro na chamada da função print().")

            # igualdade

            if texto.startswith("if") and "=" in texto and "==" not in texto:
                erros.append(f"Linha {numero}: para comparar valores utilize '==' em vez de '='.")

        # -----------------------------------
        # RESULTADO
        # -----------------------------------

        if erros:

            print("Foram encontrados os seguintes possíveis problemas:\n")

            for erro in erros:
                print(f"• {erro}")

        else:

            print("✅ Nenhum erro básico foi encontrado.")
            print("Seu código parece estar bem estruturado!")

        print("\nLembre-se: esta é apenas uma análise básica e não substitui a execução do código.")

        print("-" * 42)

def criar_desafio():
    """
    Apresenta um desafio de programação aleatório para o usuário.
    """

    while True:

        cabecalho("🏆 CRIAR DESAFIO")

        print("\nGerando desafio...")

        desafio = random.choice(desafios)

        cabecalho("💡 DESAFIO DE PROGRAMAÇÃO")
        print(desafio)
        print("-" * 42)

        print("\nO que deseja fazer?")
        print("1 - Gerar outro desafio")
        print("2 - Voltar ao menu")

        opcao = input("\nEscolha: ").strip()

        if opcao == "2":
            break

        elif opcao != "1":
            print("\n⚠ Opção inválida. Voltando ao menu...")
            break

def iniciar_quiz():
    """
    Inicia um quiz de múltipla escolha sobre Python.
    """

    cabecalho("🏆 QUIZ PYTHON - PYLEARNING")

    pontuacao = 0

    for pergunta in quiz:

        print("\n" + "-" * 42)
        print(pergunta["pergunta"])

        for alternativa in pergunta["alternativas"]:
            print(alternativa)

        resposta = input("\nSua resposta (A, B, C ou D): ").upper().strip()

        if resposta == pergunta["resposta"]:
            print("✔ Correto!")
            pontuacao += 1
        else:
            print(f"✘ Incorreto! Resposta correta: {pergunta['resposta']}")

    cabecalho("RESULTADO FINAL")

    print(f"Você acertou {pontuacao} de {len(quiz)} perguntas.")

    if pontuacao == len(quiz):
        print("Excelente! Você domina o conteúdo!")
    elif pontuacao >= len(quiz) / 2:
        print("Bom desempenho! Continue praticando.")
    else:
        print("Reforce seus estudos e tente novamente.")

def plano_estudos():
    """
    Gera um plano de estudos personalizado com base no nível do usuário.
    """

    while True:

        cabecalho("📘 PLANO DE ESTUDOS")

        print("\nEscolha seu nível:")
        print("1 - Iniciante")
        print("2 - Intermediário")
        print("3 - Avançado")
        print("Digite 'voltar' para retornar ao menu.")

        nivel = input("\nSua escolha: ").lower().strip()

        if nivel == "voltar":
            break

        if nivel == "1":
            chave = "iniciante"
        elif nivel == "2":
            chave = "intermediário"
        elif nivel == "3":
            chave = "avançado"
        else:
            print("\n⚠ Opção inválida. Tente novamente.")
            continue

        if chave in planos_estudo:

            print("\n" + "-" * 42)
            print(f"📌 PLANO {chave.upper()}")
            print("-" * 42)

            for item in planos_estudo[chave]:
                print(f"- {item}")

            print("-" * 42)

        else:
            print("\nPlano não encontrado.")

def registrar_historico(acao):
    """
    Registra uma ação do usuário no arquivo de histórico.
    """

    try:
        from datetime import datetime

        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        with open("historico.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"[{data_hora}] - {acao}\n")

    except Exception as e:
        print("Erro ao registrar histórico:", e)

def visualizar_historico():
    """
    Exibe o histórico de ações do usuário armazenado no arquivo.
    """

    cabecalho("📜 HISTÓRICO DE ESTUDOS")

    try:
        with open("historico.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

            if not linhas:
                print("Nenhum histórico encontrado ainda.")
            else:
                for linha in linhas:
                    print(linha.strip())

    except FileNotFoundError:
        print("Nenhum histórico encontrado. O arquivo ainda não foi criado.")

def configuracoes():
    """
    Menu de configurações do sistema PyLearning.
    """

    while True:

        cabecalho("⚙ CONFIGURAÇÕES")

        print("\n1 - Limpar histórico")
        print("2 - Informações do sistema")
        print("3 - Voltar ao menu")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            try:
                with open("historico.txt", "w", encoding="utf-8") as arquivo:
                    arquivo.write("")
                print("\n✔ Histórico limpo com sucesso!")
            except Exception as e:
                print("\nErro ao limpar histórico:", e)

        elif opcao == "2":
            print("\nPyLearning - Assistente de aprendizado de Python")
            print("Versão: 1.0")
            print("Projeto educacional para ensino de programação")

        elif opcao == "3":
            break

        else:
            print("\n⚠ Opção inválida.")

def sobre():
    """
    Exibe informações sobre o projeto PyLearning.
    """

    cabecalho("ℹ SOBRE O PYLEARNING 🧠")

    print("""
PyLearning é um projeto acadêmico de um assistente inteligente desenvolvido em Python
com o objetivo de auxiliar estudantes no aprendizado da linguagem.

O sistema oferece:
- Explicação de conceitos
- Exercícios práticos
- Desafios
- Quiz
- Correção de código
- Plano de estudos
- Histórico de atividades

Projeto desenvolvido para fins educacionais,
utilizando estruturas básicas e intermediárias de Python.
Sua desenvolvedora é a Gabriela de Oliveira Silva, aluna do SENAI, mas pode chamá-la de Gabs. :)
""")

