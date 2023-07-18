import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue
from typing import List


def is_valid_path(path_file: str, instance: Queue):
    for dict in instance.queue:
        if dict.get("nome_do_arquivo") == path_file:
            return False
    return True


def get_dict_data(lines: List[str], path_file: str):
    dict = {}
    dict["nome_do_arquivo"] = path_file
    dict["qtd_linhas"] = len(lines)
    dict["linhas_do_arquivo"] = lines
    return dict


def process(path_file: str, instance: Queue):
    if is_valid_path(path_file, instance):
        lines = txt_importer(path_file)
        dict_data = get_dict_data(lines, path_file)
        instance.enqueue(dict_data)
        print(dict_data)


def remove(instance: Queue):
    if len(instance) == 0:
        print("Não há elementos")
    else:
        dict = instance.dequeue()
        print(f"Arquivo {dict.get('nome_do_arquivo')} removido com sucesso")


def file_metadata(instance: Queue, position: int):
    if position < 0 or position >= len(instance):
        print("Posição inválida", file=sys.stderr)
    else:
        dict = instance.search(position)
        print(dict)
