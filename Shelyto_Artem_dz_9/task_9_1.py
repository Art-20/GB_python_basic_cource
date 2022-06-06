# Задание 1
# Создать класс TrafficLight (светофор):
#
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (red) составляет 4 секунды, второго (yellow) — 2 секунды, третьего (green) — 3 секунды;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный) и в stdout каждый цвет должен принтоваться ТОЛЬКО ОДИН раз в момент переключения с указанием исходного кол-ва секунд, т.е. формат строки вывода <текущий цвет> <значение секунд> сек;
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Пример, stdout при обращении к методу running:
#
# $ traffic = TrafficLight()
# $ traffic.running()
# red 4 сек
# yellow 2 сек
# green 3 сек
# # Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.

class TrafficLight:
    color = {'red': 4, 'yellow': 2, 'green': 3}

    def running(self):
        check_switching_order = ['red', 'yellow', 'green']
        check_count = 0
        for key, val in self.color.items():
            assert key == check_switching_order[check_count], f'Неверный порядок влючения режимов светофора: {key} вместо {check_switching_order[check_count]}'
            print(f'{key} {val} сек')
            check_count += 1
        print('\n')



if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()

    traffic_2 = TrafficLight()
    traffic_2.color = {'red': 5, 'yellow': 8, 'green': 5}
    traffic_2.running()

    traffic_3 = TrafficLight()
    traffic_3.color = {'blue': 5, 'yellow': 8, 'green': 5}
    traffic_3.running()

