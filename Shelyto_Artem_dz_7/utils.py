import os

def folder_creating(name: str):
    """"
    Создает папку
    """
    if not os.path.exists(name):
        os.mkdir(name)

def creating_1_lev_1(name_list:list, path:str):
    """"
      Создает список папок из списка
    """
    for name in name_list:
        folder = os.path.join(path, name)
        folder_creating(folder)

def creating_1_lev_2(project_name: str, name: str):
    """"
      Создает список папок
    """
    folder = os.path.join(project_name, name)
    folder_creating(folder)



def creating_project(name: str, path: str, name_list: list):
    """"
          Создает проект со структурой
    """
    folder = os.path.join(path, name)
    folder_creating(folder)
    creating_1_lev_1(name_list, folder)

def creating_structure_dict(file:str):
    """
              Функция открывает config.yaml и создает словарь со структурой проекта.
              Возвращает название проекта и словарь со структурой
    """
    # создание словаря со структурой проекта
    folders_structure = {}
    # чтение файла конфигуратора
    with open(file, 'r', encoding='utf-8') as f:
        # построчный поиск папок и файлов
        for line in f:
            # поиск названия проекта
            if line.startswith('|--'):
                project_name = line[3:].strip('\n')
            # поиск папок первого уровня - ключи для словаря
            elif line.startswith('  |--'):
                folder = line[5:].strip('\n')
                # создание списка значений ключа
                file_list = []
            # поиск файлов в папках первого уровня - значения для словаря
            elif line.startswith('  | |--') and line.count('.'):
                file = line[7:].strip('\n')
                # добавления значения в список для данного ключа
                file_list.append(file)
                # обновление списка значений в словаре для данного ключа
                folders_structure[folder] = file_list
            # поиск папок в папках первого уровня - значения для словаря
            elif line.startswith('  | |--'):
                folder_2_lev = line[7:].strip('\n')
                # добавления значения в список для данного ключа
                file_list.append(folder_2_lev)
                # обновление списка значений в словаре для данного ключа
                folders_structure[folder] = file_list
    return project_name, folders_structure

