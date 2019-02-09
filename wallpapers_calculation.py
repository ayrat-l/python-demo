import math
from lib import perimeter_of_the_room

print('Программа для рассчёта количества рулонов (в шт.) необходимых при ремонте комнаты (помещения). \nДля начала необходимо определить периметр помещения.')
width_of_the_room = float(input('Введите ширину комнаты (м) > '))
length_of_the_room = float(input('Введите длину комнаты (м) > '))
height_of_the_room = float(input('Введите высоту комнаты (м) > '))
print('*********' * 2)
#Как узнать периметр комнаты?
print('Периметр помещения = ', perimeter_of_the_room(width_of_the_room,length_of_the_room), 'м.')
print('*********' * 2)
print('Надеюсь вы уже подобрали обои? Тогда введите их ширину и длину...')
width_of_the_wallpaper = float(input('Введите ширину рулона обоев (м) > '))
length_of_the_wallpaper = float(input('Введите длину рулона обоев (м) > '))
canvas_quantity = perimeter_of_the_room / width_of_the_wallpaper #Расчет количества полотен обоев
canvas_quantity = math.ceil(canvas_quantity) #округляем до ближайшего наибольшего целого числа)
canvas_quantity_in_1_wallpapers = (length_of_the_wallpaper / (height_of_the_room + 0.10))#an additional margin of 10 cm (дополнительный запас 10 см)
canvas_quantity_in_1_wallpapers = math.floor(canvas_quantity_in_1_wallpapers)
quantity_wallpapers = perimeter_of_the_room / canvas_quantity_in_1_wallpapers
print('*********' * 2)
print(quantity_wallpapers, ' шт. рулона хватит для оклейки всей комнаты (помещения).')
print('*********' * 2)

