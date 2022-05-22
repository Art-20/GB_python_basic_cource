# project_name = 'my_project'
# folder = r'C:\Users\Artem\Desktop\555'
# import os
# new_folder=os.path.join(folder, project_name)
# os.mkdir(new_folder)
import os
folder = r'C:\Users\Artem\AppData\Local\Programs\Python\Python310\Lib\site-packages\aiohttp'
# py_files = os.listdir(folder)
# py_files = [item
#             for item in os.listdir(folder)
#             if item.lower().endswith('.py')]
# print(py_files)

# py_files = [os.path.join(folder,item)
# for item in os.listdir(folder)
# if item.lower().endswith('.py')]
# print(py_files)

import os
# dir_name = 'sample_dir'
# if not os.path.exists(dir_name):
#     os.mkdir(dir_name)
#
# dir_path = os.path.join('data', 'src')
# if not os.path.exists(dir_path):
#     os.makedirs(dir_path)

# dir_name = 'first_out_dir'
# new_dir_name = '../first_out_dir'
#
# if os.path.exists(dir_name) and not os.path.exists(new_dir_name):
#     os.rename(dir_name, new_dir_name)
# else:
#     print('есть такая папка')

# def copyfileobj(fsrc, fdst, length=16*1024):
#     """copy data from file-like object fsrc to file-like object fdst"""
#     while 1:
#         buf = fsrc.read(length)
#         if not buf:
#             break
#     fdst.write(buf)

# import random
# import shutil
# for _ in range(3):
#     with open('data/hello.txt', encoding='utf-8') as src:
#         with open('data/summary.txt', 'a', encoding='utf-8') as dst:
#                 head_size = random.randrange(5)
#                 print(head_size, src.read(head_size))
#                 shutil.copyfileobj(src, dst)

# import os
# from shutil import copyfile, copy, copy2
# def show_stat(f_path):
#     stat = os.stat(f_path)
#     print('{f_p}:\n\tperm - {perm}, modify {m_t:.0f}, access {a_t:.0f}'.format(
#         f_p=f_path,
#         perm=oct(stat.st_mode),
#         m_t=stat.st_mtime,
#         a_t=stat.st_atime,
#     ))
# src = 'data/summary.txt'
# show_stat(src)
# show_stat(copyfile(src, 'new_data/summary_clone.txt'))
# show_stat(copy(src, 'new_data'))
# show_stat(copy2(src, 'new_data/summary_clone_2.txt'))

# создание словаря со структурой проекта
# folders_structure = {}
# #чтение файла конфигуратора
# with open('config.yaml', 'r', encoding='utf-8') as f:
#     # построчный поиск папок и файлов
#     for line in f:
#         print(line.strip('\n'))
#         # поиск названия проекта
#         if line.startswith('|--'):
#             project_name = line[3:].strip('\n')
#             print('project_name', project_name)
#         # поиск папок первого уровня - ключи для словаря
#         elif line.startswith('  |--'):
#             folder = line[5:].strip('\n')
#             print('folder', folder)
#             file_list = []
#         # поиск файлов в папках первого уровня - значения для словаря
#         elif line.startswith('  | |--') and line.count('.'):
#             file = line[7:].strip('\n')
#             print('file', file)
#             # добавления значения в список для данного ключа
#             file_list.append(file)
#             # обновление списка значений в словаре для данного ключа
#             folders_structure[folder] = file_list
#             print(file_list)
#         # поиск папок в папках первого уровня - значения для словаря
#         elif line.startswith('  | |--'):
#             folder_2_lev = line[7:].strip('\n')
#             print('folder_2_lev', folder_2_lev)
#             # добавления значения в список для данного ключа
#             file_list.append(folder_2_lev)
#             # обновление списка значений в словаре для данного ключа
#             folders_structure[folder] = file_list
#             print(file_list)
#
# print(project_name, '\n', folders_structure)
# project_name = 'mu_pr'
folder_name = 'sample_dir'
name = 'first.py'
path = os.path.join(folder_name, name)
print(path)
f = open(path, 'w')



# size = os.stat(file_name).st_size
       # print(file, file_name, size)
       # i = 0
       # while size > 0:
       #    size =  size // 10
       #    i += 1
       # key = 10**i

# file_name = os.path.join(root_dir, 'fymrcsedg.bin')
# size = os.stat(file_name).st_size
# print(file_name, size)



