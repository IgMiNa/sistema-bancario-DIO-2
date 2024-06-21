
def menu():
    menu = """\n
    ============== MENU ==============
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [nu] Novo usuário
    [lc] Listar contas
    [q] Sair
"""
    print(menu)
    return input("Escolha a operação desejada: ")

def depositar(saldo,valor,extrato,/):
    try:
        if valor >= 0:
            saldo += valor
            extrato.append(f"+R$ {valor:.2f}")
            print(f"\nDepósito de R$ {valor:.2f} foi realizado com sucesso!")
            return saldo, extrato
        
        else:
            print("\nO valor do deposíto deve ser positivo.")
            return saldo, extrato
        
    except ValueError:
        print("\nO valor digitado é inválido.")
        return saldo, extrato

def sacar(*,saldo,valor,limite,limite_saques,n_saques,extrato):
    saques = n_saques == limite_saques
    limite_quant = valor > limite
    saldo_baixo = valor > saldo
    try:
        if saques:
            print("\nA quantidade limite de saquês diários foi atingida.")
            return saldo, n_saques, extrato
        
        elif limite_quant:
            print("\nO valor do saldo é maior que o limite proposto.")
            return saldo, n_saques, extrato
        
        elif saldo_baixo:
            print("\nO valor do saldo é menor que o valor de saquê.")
            return saldo, n_saques, extrato
        
        elif valor >= 0:
            n_saques += 1
            saldo -= valor
            print(saldo)
            extrato.append(f"-R$ {valor:.2f}")
            print(f"\nSaque de R$ {valor:.2f} foi realizado com sucesso!")
            print(n_saques)
            return saldo, n_saques, extrato
        else:
            print("\nO valor tem que ser positivo.")
    except ValueError:
        print("\nO valor digitado é inválido.")

def exibir_extrato(extrato):
    print("\n=====EXTRATO=====")
    for dado in extrato:
        print(dado)

def criar_usuario(usuarios):
    cpf = input("\nInforme o CPF (somente números): ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print("\nUsuário com esse CPF já existe!")
        return usuarios

    nome = input("Informe o nome completo: ")
    dt_nasc = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    user = {"nome": nome, "data de nascimento": dt_nasc, "cpf": cpf, "endereço": endereco}
    usuarios.append(user)
    print("\nUsuário foi craido com sucesso!")
    return usuarios

def filtrar_usuario(cpf, usuarios):
    usuario_filtrado = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None

def criar_conta(agencia,contas,usuarios):
    cpf = input("\nInforme o número do CPF do titular da conta: ")
    conta_existente = filtrar_conta(cpf, contas)
    usuario = filtrar_usuario(cpf,usuarios)

    if conta_existente:
        print("\nJá existe uma conta com esse CPF!")
        return contas
    
    elif usuario:    
        n_conta = len(contas) + 1 
        conta = {"agência": agencia, "número da conta": n_conta, "cpf": cpf}
        contas.append(conta)
        print("\nConta criada com sucesso!")
        return contas
    
    else:
        print("\nUsuário não encontrado, finalizando operação de criação de conta!")
        return contas

def filtrar_conta(cpf, contas):
    conta_filtrada = [conta for conta in contas if conta['cpf'] == cpf]
    return conta_filtrada[0] if conta_filtrada else None

def listar_contas(contas):
    print("\n             =====CONTAS=====")
    for dado in contas:
        print(f"Agência: {dado['agência']} | Número da conta: {dado['número da conta']} | CPF: {dado['cpf']}")

def main():
    LIMITES_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    n_saques = 0
    limite = 500
    extrato = []
    usuarios = []
    contas = []

    while True:
        resultado = menu()
        match resultado:
            case "d":
                valor = input("Qual é o valor que deseja depositar: ")
                saldo,extrato = depositar(saldo, float(valor), extrato)
            
            case "s":
                valor = input("Qual é o valor que deseja sacar: ")
                saldo, n_saques, extrato = sacar(saldo = saldo, valor = float(valor), limite = limite, limite_saques = LIMITES_SAQUES, n_saques = n_saques, extrato = extrato)
            
            case "e":
                exibir_extrato(extrato)

            case "nc":
                contas = criar_conta(AGENCIA,contas,usuarios)
            
            case "nu":
                usuarios = criar_usuario(usuarios)
            
            case "lc":
                listar_contas(contas)
            
            case "q":
                break

            case _:
                print("Seleção inválida.")

if __name__ == "__main__":
    main()