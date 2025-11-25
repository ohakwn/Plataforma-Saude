from utils import formatarTelefone

class Paciente:
    def __init__(self, nome, idade, telefone):
        """
        Construtor da classe Paciente.
        Recebe nome, idade e telefone do paciente.
        O telefone é processado pela função formatarTelefone para padronização.
        """
        self.nome = nome
        self.idade = idade
        self.telefone = formatarTelefone(telefone)

    def exibirDadosPaciente(self):
        """
        Exibe os dados completos do paciente no console.
        Esta função é chamada quando o usuário deseja visualizar informações individuais.
        """
        print(f"\nNome do Paciente: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Telefone: {self.telefone}")