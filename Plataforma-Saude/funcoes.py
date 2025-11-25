from paciente import Paciente # Importa a classe paciente para criar novos pacientes

def executarEscolha(estado, escolha):
    """
    Controla o fluxo principal do programa com base na opção escolhida pelo usuário.
    A função utiliza match/case para organizar as opções do menu.
    """
    match escolha:
        case 1:
            cadastrarPaciente(estado) # Cadastra um novo paciente
        case 2:
            exibirEstatisticas(estado) # Exibe as estátisticas gerais dos pacientes
        case 3:
            buscarPaciente(estado) # Busca um paciente pelo nome
        case 4:
            exibirTodosPacientes(estado) # Exibe todos os pacientes cadastrados
        case 5:
            print("\nEncerrando o sistema...")
            return True # Retorna True para encerrar o loop principal no main
        case _:
            print("\nOpção inválida, tente novamente.")
    return False # Retorna False para continuar o programa

def cadastrarPaciente(estado):
    """
    Cadastra um novo paciente coletando nome, idade e telefone.
    Atualiza o dicionário de estado com os dados do paciente.
    """
    nome = str(input("\nNome do paciente: "))
    idade = int(input("Idade: "))
    telefone = input("Telefone: ")
    
    # Cria um objeto Paciente
    paciente = Paciente(nome, idade, telefone)

    # Armazena o objeto na lista de pacientes
    estado['listaPacientes'].append(paciente)

    # Atualiza contadores do estado
    estado['totalPacientes'] += 1
    estado['totalIdades'] += idade
    print("\nPaciente cadastrado com sucesso!")
    
def exibirEstatisticas(estado):
    """
    Exibe estatísticas gerais:
    - Número total de pacientes
    - Idade média
    - Paciente mais novo e mais velho
    """
    if estado["listaPacientes"]:
        print(f"\nNúmero total de pacientes cadastrados: {estado['totalPacientes']}")

        # Cálculo da média das idades
        mediaIdades = estado['totalIdades'] / estado['totalPacientes']
        print(f"Idade média dos pacientes: {mediaIdades:.1f}")

        # Usa funções max e min para guardar o paciente mais novo e mais velho
        pacienteMaisNovo = min(estado["listaPacientes"], key=lambda p: p.idade)
        pacienteMaisVelho = max(estado["listaPacientes"], key=lambda p: p.idade)

        print(f"Paciente mais novo: {pacienteMaisNovo.nome} ({pacienteMaisNovo.idade}) anos")
        print(f"Paciente mais velho: {pacienteMaisVelho.nome} ({pacienteMaisVelho.idade}) anos")
    else:
        print("É necessário pelo menos um paciente cadastrado!")

def buscarPaciente(estado):
    """
    Permite buscar um paciente pelo nome.
    A busca ignora diferenças de maiúsculas/minúsculas.
    """
    if not estado["listaPacientes"]:
        print("Nenhum paciente cadastrado.")
        return
    
    nomeBusca = input("Nome do Paciente: ")

    # Busca usando next() e expressão geradora
    paciente = next((p for p in estado["listaPacientes"] if p.nome.lower() == nomeBusca.lower()), None)
    if paciente:
        paciente.exibirDadosPaciente()
    else:
        print("Paciente não encontrado.")

def exibirTodosPacientes(estado):
    """
    Lista todos os pacientes cadastrados e exibe seus dados.
    """
    if not estado["listaPacientes"]:
        print("Nenhum paciente cadastrado")
        return
    
    print("\n=== LISTA DE PACIENTES CADASTRADOS ===\n")
    
    for i, paciente in enumerate(estado["listaPacientes"], start=1):
        print(f"Paciente {i}:")
        paciente.exibirDadosPaciente()
        print("-" * 40)