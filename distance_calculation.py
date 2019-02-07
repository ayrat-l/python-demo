from lib import distance_calculation

volume_fuel = int(input("Введите остаток топлива в баке (л) >> "))
expense_fuel = int(input("Введите средний расход на 100 км >> "))

print(distance_calculation(volume_fuel,expense_fuel))

