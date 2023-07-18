from ting_file_management.queue import Queue
from typing import List


def get_occurrencies(target: str, lines: List, show_lines: bool) -> List[dict]:
    occurrences = []
    for line_index, line in enumerate(lines, start=1):
        if target in line.lower():
            occurrence = {"linha": line_index}
            if show_lines:
                occurrence["conteudo"] = line
            occurrences.append(occurrence)
    return occurrences


def check_words(target: str, instance: Queue, show_lines: bool) -> List[dict]:
    result = []

    for dict in instance.queue:
        path_file = dict.get("nome_do_arquivo")
        lines = dict.get("linhas_do_arquivo")
        occurrences = get_occurrencies(target, lines, show_lines)

        if occurrences:
            result.append({
                "palavra": target,
                "arquivo": path_file,
                "ocorrencias": occurrences
            })

    return result


def exists_word(word: str, instance: Queue) -> List[dict]:
    result = check_words(word.lower(), instance, False)

    return result


def search_by_word(word: str, instance: Queue) -> List[dict]:
    result = check_words(word.lower(), instance, True)

    return result
