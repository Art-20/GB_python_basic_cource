# class MyClass:
#     def __setattr__(self, attr, value):
#         '''
#             Шляпа
#         '''
#         if attr == "width":
#             self.__dict__[attr] = value
#             print(value)
#         else:
#             print(f"Атрибут {attr} недопустим")
# mc = MyClass()
# mc.lenght = 40

# class Class1:
#     def __init__(self, param):
#         self.param = param
#     def __str__(self):
#         return str(self.param)
#
# class Class2:
#     def __init__(self, *args):
#         self.my_list = []
#         for el in args:
#             self.my_list.append(Class1(el))
#
#
# my_obj = Class2(10, True, "text")
# print(my_obj.my_list[1])
# print(my_obj.my_list[0])
# print(my_obj.my_list[2])
#
#
#
# class Class1:
#     def __init__(self, param):
#         self.param = param
#     def __str__(self):
#         return str(self.param)
#
# class Class2:
#     def __init__(self, *args):
#         self.my_list = []
#         for el in args:
#             self.my_list.append(Class1(el))
#     def __getitem__(self, index):
#         return self.my_list[index]
#
# my_obj = Class2(10, True, "text")
# print(my_obj.my_list[0])
# print(my_obj[1])
# print(my_obj[2])
# out = ''
# k = [1, 2]
# k = str(k)
# result = out.join(k)
# print(result)

#
# def p_wrapper(func):
#     print(func)
#     def tag_wrapper(*args, **kwargs):
#         print('args', args)
#         print('kwargs', kwargs)
#         markup = func(*args, **kwargs)
#         print(markup)
#         return markup
#     return tag_wrapper
#
#
# @p_wrapper
# def render_input(field):
#     return f'<input id="id_{field}" type="text" name="{field}">'
#
# username_f = render_input('username')
# print(render_input)
# def p_wrapper(func):
#     def tag_wrapper(*args, **kwargs):
#         markup = func(*args, **kwargs)
#         return f'<p>{markup}</p>'
#     return tag_wrapper
#
#
# @p_wrapper
# def render_input(field):
#     return f'<input id="id_{field}" type="text" name="{field}">'
#
#
# username_f = render_input('username')
# print(username_f)
# def simple_cache(func):
#     cache = {}
#     def wrapper(*args):
#         nonlocal cache
#         key = str(*args)
#         if key not in cache:
#             cache[key] = func(*args)
#         return cache[key]
#     return wrapper
# @simple_cache
# def render_input(field):
#     print(f"call render_input('{field}')")
#     return f'<input id="id_{field}" type="text" name="{field}">'
#
# username_f = render_input('username')
# password_f = render_input('password')
# username_f_2 = render_input('username')
# print(username_f)
# print(password_f)
# print(username_f_2)


# from time import perf_counter
# print(f'{perf_counter()}: script started')
# def simple_cache(func):
#     cache = {}
#     print(f'{perf_counter()}: {func.__name__} cache created ({id(cache)})')
#     def wrapper(*args):
#         nonlocal cache
#         key = tuple(args)
#         if key not in cache:
#             cache[key] = func(*args)
#         return cache[key]
#     return wrapper
#
#
# @simple_cache
# def calc_sum(x, y):
#     return x + y
# @simple_cache
# def calc_mul(x, y):
#     return x * y

# def simple_cache(func):
#     cache = {}
#     def wrapper(*args):
#         nonlocal cache
#         key = str(*args)
#         if key not in cache:
#             cache[key] = func(*args)
#         return cache[key]
#     return wrapper
#
#
# def logger(func):
#     def wrapper(*args):
#         result = func(*args)
#         print(f'\tcall {func.__name__}({", ".join(map(str, args))})')
#         return result
#     return wrapper
#
#
# @simple_cache
# @logger
# def render_input(field):
#     return f'<input id="id_{field}" type="text" name="{field}">'
#
# username_f = render_input('username')
# password_f = render_input('password')
# username_f_2 = render_input('username')
# print(username_f)
# print(password_f)
# print(username_f_2)
#
# number = 0
# result = ''
# cells = 11
# i = 1

# while cells != 0:
#     if i < number:
#         result = f'{result}*'
#         i += 1
#         cells -= 1
#     elif i % number == 0:
#         result = f'{result}*\n'
#         cells -= 1
#         i = 1
#
# print(result)
    # i = 0
    # while i < number:
    #     if cells == 0:
    #         break
    #     else:
    #         result = f'{result}*'
    #         i += 1
    #         cells -= 1


#     result = f'{result}\n'
#     cells -= 1
#     i = 0
# print(result)
# while cells != 0:
#     while i < number:
#         result = f'{result}*'
#         i += 1
#         cells -= 1
#
#     result = f'{result}\n'
#     cells -= 1
#     i = 0




