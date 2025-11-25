def formatarTelefone(telefoneBruto: str) -> str:
    """
    Recebe um telefone em formato bruto (contendo caracteres variados)
    e retorna o número formatado no padrão: (DD) XXXXX-XXXX.

    Etapas:
    1. Remove qualquer caractere que não seja número.
    2. Separa os primeiros dois dígitos como DDD.
    3. Divide o restante entre prefixo e sufixo conforme o padrão mobile atual.
    """

     # Extrai apenas os dígitos numéricos do telefone
    digitos = ''.join(ch for ch in telefoneBruto if ch.isdigit())

     # Define DDD e partes do telefone
    ddd = digitos[:2]       # Primeiros dois dígitos
    parte1 = digitos[2:7]   # Cinco dígitos seguintes (prefixo)
    parte2 = digitos[7:]    # Últimos dígitos (sufixo)

    # Retorna o número formatado
    return f"({ddd}) {parte1}-{parte2}"