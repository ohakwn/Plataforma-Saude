from funcoes import executarEscolha # Importa a função que processa o menu
from menu import exibirMenu # Importa a função que exibe o menu na tela

# Dicionário que armazena o estado geral do sistema
estado = {
    "listaPacientes": [], # Guarda objetos do tipo Paciente
    "totalPacientes": 0,  # Contagem total de pacientes cadastrados
    "totalIdades": 0      # Soma das idades, usada para calcular a média posteriormente
}

# Loop principal do sistema
while True:
    exibirMenu() # Exibe o menu de opções

    try:
         # Coleta a opção escolhida pelo usuário e converte para inteiro
        escolha = int(input("Escolha uma opção: "))
    except ValueError:
        # Caso o usuário digite algo inválido, o programa não quebra
        print("\nDigite um número válido!")
        continue # Retorna ao início do loop
    
    # Passa a escolha para a função central que decide o fluxo
    if executarEscolha(estado, escolha):
        break # Interrompe o loop caso a função retorne True (opção de sair)