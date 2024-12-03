"""
Criar um programa em Python que permita ao departamento de manutenção de equipamentos informáticos gerir pedidos de forma eficiente, utilizando funções para modularidade e organização do código.
"""

def registar_pedido(pedidos):
    id_pedido = len(pedidos) + 1
    descricao = input("Descrição do problema: ")
    estado = "Pendente"
    pedidos[id_pedido] = {"descricao": descricao, "estado": estado}
    print(f"Pedido #{id_pedido} registado com sucesso!")

def consultar_pedido(pedidos):
    id_pedido = int(input("ID do pedido a consultar: "))
    if id_pedido in pedidos:
        pedido = pedidos[id_pedido]
        print(f"Pedido #{id_pedido} - Descrição: {pedido['descricao']}, Estado: {pedido['estado']}")
    else:
        print("Pedido não encontrado.")

def atualizar_estado(pedidos):
    id_pedido = int(input("ID do pedido a atualizar: "))
    if id_pedido in pedidos:
        novo_estado = input("Novo estado (Pendente/Em Andamento/Concluído): ")
        if novo_estado in ["Pendente", "Em Andamento", "Concluído"]:
            pedidos[id_pedido]["estado"] = novo_estado
            print(f"Estado do pedido #{id_pedido} atualizado para '{novo_estado}'.")
        else:
            print("Estado inválido.")
    else:
        print("Pedido não encontrado.")

def eliminar_pedido(pedidos):
    id_pedido = int(input("ID do pedido a eliminar: "))
    if id_pedido in pedidos:
        pedidos.pop(id_pedido)
        print("Pedido eliminado")
    else:
        print("Pedido não encontrado.")

def exibir_pedidos(pedidos):
    print("\nLista de Pedidos:")
    print("ID\tDescrição\t\tEstado")
    print("-" * 40)
    for id_pedido, info in pedidos.items():
        print(f"{id_pedido}\t{info['descricao'][:15]}\t\t{info['estado']}")

def main():
    pedidos = {}
    while True:
        print("\nSistema de Gestão de Pedidos - Manutenção")
        print("1. Registar Pedido")
        print("2. Consultar Pedido")
        print("3. Atualizar Estado")
        print("4. Exibir Todos os Pedidos")
        print("5. Eliminar Pedido")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            registar_pedido(pedidos)
        elif opcao == "2":
            consultar_pedido(pedidos)
        elif opcao == "3":
            atualizar_estado(pedidos)
        elif opcao == "4":
            exibir_pedidos(pedidos)
        elif opcao == "5":
            eliminar_pedido(pedidos)
        elif opcao == "6":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()

