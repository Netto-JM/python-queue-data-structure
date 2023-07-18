import sys


def txt_importer(path_file: str):
    """Aqui irá sua implementação"""

    # Verifica se o arquivo tem a extensão correta
    if not path_file.endswith('.txt'):
        print('Formato inválido', file=sys.stderr)
        return None

    try:
        # Abre o arquivo para leitura
        with open(path_file, 'r') as file:
            # Lê as linhas do arquivo e retorna uma lista
            lines = file.read().split('\n')
            return lines

    except FileNotFoundError:
        print(f'Arquivo {path_file} não encontrado', file=sys.stderr)
        return None
