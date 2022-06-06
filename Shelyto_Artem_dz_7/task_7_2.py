# Написать скрипт, создающий из config.yaml стартер для проекта со следующей
# структурой:


import utils
import os

# создание словаря из файла со структурой
file = 'config.yaml'
project = utils.creating_structure_dict(file)
print(project)



def creating_1_lev(project_name: str, name: str):
    """"
      Создает папки 1 уровня
    """
    folder = os.path.join(project_name, name)
    utils.folder_creating(folder)


def creating_2_lev(project_name: str, folder_name: str, name: str):
    """"
      Создает папки второго уровня
    """
    folder = os.path.join(project_name, folder_name, name)
    utils.folder_creating(folder)


def creating_file(project_name: str, folder_name: str, name: str):
    """"
      Создает файлы в папках второго уровня
    """
    path = os.path.join(project_name, folder_name, name)
    f = open(path, "w+")
    f.close()


# создаем проект
utils.folder_creating(project[0])

# создаем папки
for key, val in project[1].items():
    # создаем папки 1 уровня
    creating_1_lev(project[0], key)
    # создаем вложенные папки и файлы, ищем в значениях словаря папки и файлы
    for _ in val:
        # если файл - создаем файл
        if _.count('.'):
            creating_file(project[0], key, _)
        # если папка - создаем папку
        else:
            creating_2_lev(project[0], key, _)


