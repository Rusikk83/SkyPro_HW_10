
def load_candidates():
    """загружает данные из файла"""
    with open("candidates.json", mode='r', encoding='utf-8') as file:
        data = file.read()
    return data
