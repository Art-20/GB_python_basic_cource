# #1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
# как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
# можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?


import os


def folder_creating(name: str):
    """"
    Создает папку
    """
    if not os.path.exists(name):
        os.mkdir(name)

def creating_1_lev(name_list:list, path:str):
    """"
      Создает список папок
    """
    for name in name_list:
        folder = os.path.join(path, name)
        folder_creating(folder)


def creating_project(name: str, path: str, name_list: list):
    """"
          Создает проект со структурой
    """
    folder = os.path.join(path, name)
    folder_creating(folder)
    creating_1_lev(name_list, folder)






# название проекта
project_name = 'DZ7'

# путь по которому будет создан проект
folder = r'C:\Users\Artem\Desktop\555'
# folder = r'C:\Users\Artem\PycharmProjects\GB_python_basic_cource\Shelyto_Artem_dz_7'

#список папок проекта
folder_1_lev = ['settings', 'mainapp', 'adminapp', 'authapp']

#вызов функции для создания проекта
creating_project(project_name, folder, folder_1_lev)
