from ting_file_management.queue import Queue


def exists_word(word: str, instance: Queue):
    result = []
    target = word.lower()

    for item in instance.items:
        path_file = item.get("nome_do_arquivo")
        lines = item.get("linhas_do_arquivo")
        occurrences = []

        for line_index, line in enumerate(lines, start=1):
            if target in line.lower():
                occurrences.append({"linha": line_index})

        if occurrences:
            result.append({
                "palavra": word,
                "arquivo": path_file,
                "ocorrencias": occurrences
            })

    return result


def search_by_word(word: str, instance: Queue):
    """Aqui irá sua implementação"""
