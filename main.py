"""
main.py

Arquivo principal do sistema PyLearning.
Responsável pelo menu e execução do programa.
"""

from funcoes import (
    cabecalho,
    explicar_conceito,
    tirar_duvida,
    gerar_exercicio,
    corrigir_codigo,
    criar_desafio,
    iniciar_quiz,
    plano_estudos,
    registrar_historico,
    visualizar_historico,
    configuracoes,
    sobre
)

def main():

    while True:

        cabecalho("🧠 PYLEARNING - ASSISTENTE DE APRENDIZADO PYTHON")

        print("\nMENU PRINCIPAL")
        print("1 - Explicar conceitos")
        print("2 - Tirar dúvidas")
        print("3 - Gerar exercícios")
        print("4 - Corrigir código")
        print("5 - Criar desafios")
        print("6 - Iniciar quiz")
        print("7 - Plano de estudos")
        print("8 - Registrar histórico (teste manual)")
        print("9 - Visualizar histórico")
        print("10 - Configurações")
        print("11 - Sobre")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            registrar_historico("Acessou: Explicar conceitos")
            explicar_conceito()

        elif opcao == "2":
            registrar_historico("Acessou: Tirar dúvidas")
            tirar_duvida()

        elif opcao == "3":
            registrar_historico("Acessou: Gerar exercícios")
            gerar_exercicio()

        elif opcao == "4":
            registrar_historico("Acessou: Corrigir código")
            corrigir_codigo()

        elif opcao == "5":
            registrar_historico("Acessou: Criar desafios")
            criar_desafio()

        elif opcao == "6":
            registrar_historico("Acessou: Quiz")
            iniciar_quiz()

        elif opcao == "7":
            registrar_historico("Acessou: Plano de estudos")
            plano_estudos()

        elif opcao == "8":
            registrar_historico("Teste do sistema manual")
            print("\nRegistro manual feito.")

        elif opcao == "9":
            visualizar_historico()

        elif opcao == "10":
            configuracoes()

        elif opcao == "11":
            sobre()

        elif opcao == "0":
            print("\nEncerrando o PyLearning... Até logo e volte sempre que precisar! 🧠")
            break

        else:
            print("\n⚠ Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()