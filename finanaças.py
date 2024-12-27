def menu():
    return input("""
                Menu
            [1] - Adicionar Receita
            [2] - Adicionar Despesa
            [3] - Exibir Saldo
            [4] - Exibir Relatorio
            [5] - Sair    
        >>>""")

def procurar_mes(mes, meses):
    for item in meses:
        if item[0] == mes:
            return item
    
    novo_mes = (mes, [])
    meses.append(novo_mes)
    return novo_mes


meses = []
saldo = 0.0

while True:
    opcao = menu()
    match opcao:
        case "1":
            month = input("qual mes:")
            mes = procurar_mes(month, meses)
            valor = int(input("valor: "))
            categoria = input("categoria: ")
            data = input("data: ")
            mes[1].append({"tipo": "Receita", "valor": valor, "categoria": categoria, "data": data})
            saldo += valor
        
        
        case "2":
            month = input("qual mes:")
            mes = procurar_mes(month, meses)
            valor = int(input("valor: "))
            categoria = input("categoria: ")
            data = input("data: ")
            mes[1].append({"tipo": "Despesa", "valor": valor, "categoria": categoria, "data": data})
            saldo -= valor

  
        case "3":
            print(f"R${saldo}")

        case "4":
            break 

        case "5":
            print("Encerrando aplicação...")
            break 