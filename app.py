
import json
from flask import Flask


def load_candidates():
    """загружает данные из файла"""
    with open("candidates.json", mode='r', encoding='utf-8') as file:
        data = file.read()
    return data


def get_all():
    """возвращает всех кандидатов в виде списка словарей"""
    return candidates_list


def get_by_pk(pk):
    """вернет кандидата по pk в виде словаря"""
    for el in candidates_list:
        if el["pk"] == pk:
            return el


def get_by_skill(skill_name):
    """вернет кандидатовов по навыку в виде списка словарей"""
    candidates_of_skill = []
    for el in candidates_list:
        if skill_name.lower() in el['skills'].lower().split(', '):
            candidates_of_skill.append(el)
    return candidates_of_skill


candidates_list = json.loads(load_candidates())


app = Flask(__name__)

@app.route("/")
def page_index():
    """представление для отображения всех кагдидатов"""
    s = ''
    s += '<pre>\n'
    for el in get_all():
        s += f"Имя кандидата - {el['name']}\n"
        s += f"Позиция кандидата: {el['position']}\n"
        s += f"Навыки: {el['skills']}\n\n"

    return s[:-1] + '</pre>\n'


@app.route("/candidates/<int:pk>")
def page_candidates(pk):
    """представление для отображения одного кандидата по номеру"""
    s = ''
    el = get_by_pk(pk)
    s += f'<img src= "{el["picture"]}">'
    s += '<pre>\n'

    s += f"Имя кандидата - {el['name']}\n"
    s += f"Позиция кандидата: {el['position']}\n"
    s += f"Навыки: {el['skills']}\n"

    return s + '</pre>\n'


@app.route("/skills/<skill>")
def page_by_skill(skill):
    """представление для отображения всех кагдидатов имеющих запрошенный скилл"""
    s = ''
    s += '<pre>\n'
    for el in get_by_skill(skill):
        s += f"Имя кандидата - {el['name']}\n"
        s += f"Позиция кандидата: {el['position']}\n"
        s += f"Навыки: {el['skills']}\n\n"

    return s[:-1] + '</pre>\n'


app.run()
