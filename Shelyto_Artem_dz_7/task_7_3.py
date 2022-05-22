# 3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
# Примечание: исходные файлы необходимо оставить;
# обратите внимание, что html-файлы расположены в родительских папках (они играют роль пространств имён);
# предусмотреть возможные исключительные ситуации; это реальная задача, которая решена, например, во фреймворке django.

import os
import shutil

# задаем путь проекта, папку куда будем собирать шаблоны c рабочим именем templates и финальным templates_new
root_dir = 'my_project'
templates = 'my_project\\my_project'
templates_new = 'my_project\\templates'

# проходим по папкам проекта и копирум их в черновую папку templates
for root, dirs, files in os.walk(root_dir):
    # print(root, len(dirs), len(files))
    try:
        if len(dirs) != 0:
            for dir in dirs:
                path = os.path.join(root, dir)
                temp = os.path.join(root_dir, root, dir)
                # print(dir, path, temp)
                if dir != root_dir:
                    shutil.copytree(path, temp)
    except FileExistsError as e:
                print(f'ошибка: {e}')
    except Exception as e:
        print(f'global error: {e}')
#переименовываем черновую папку templates в финальное название templates_new
# if os.path.exists(templates) and not os.path.exists(templates_new):

try:
    os.rename(templates, templates_new)
except FileExistsError as e:
  print(f'ошибка: {e}')
except Exception as e:
  print(f'global error: {e}')


# ВНИМАНИЕ:
# Работает только при первом запуске,
# при последующих запусках папка templates уже существует и переименовать черновую папку my_project не получется



