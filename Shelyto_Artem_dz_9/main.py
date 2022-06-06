# class Auto:
#     # атрибуты класса
#     auto_count = 0
#     car_box =[]
#
#     # методы класса
#     def on_auto_start(self, auto_name, auto_model, auto_year):
#         print("Автомобиль заведен")
#         self.auto_name = auto_name
#         self.auto_model = auto_model
#         self.auto_year = auto_year
#         Auto.auto_count += 1
#         Auto.car_box.append(self.auto_name)
#
# a = Auto()
# a.on_auto_start("Lexus", "RX 350L", 2019)
# print(a.auto_name)
# print(a.auto_count)
# print(a.car_box)
# print(f'В гараже: {a.car_box}')
#
# a_2 = Auto()
# a_2.on_auto_start("Mazda", "CX 9", 2018)
# print(a_2.auto_name)
# print(a_2.auto_count)
# print(f'В гараже: {a.car_box}')
#
# a = Auto()
# a.on_auto_start("Lexus", "RX 350L", 2019)
# print(a.auto_name)
# print(a.auto_count)
# print(f'В гараже: {a.car_box}')

# class Auto:
#     # атрибуты класса
#     auto_count = 0
#     # методы класса
#     def __init__(self):
#         Auto.auto_count += 1
#         print(Auto.auto_count)
#
#
# a_1 = Auto()
# a_2 = Auto()
# a_3 = Auto()
direction = 'напрао'
right_direction = ['направо', 'налево', 'прямо', 'назад']
assert direction in right_direction, 'нераспознанное направление движения'
print(f'Машина  движется {direction}')

