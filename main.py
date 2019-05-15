import os

print("0 - выйти из программы \n1 - Функция номер 1 \n2 - Функция номер 2\n3 - Функция номер 3\n4 - Функция номер 4")

name_file = "products.txt";

file = open(name_file, "r")
sort = []

for line in file:
	line = line.strip()
	line = line.split(";")
	sort.append(line)

max = int(sort[len(sort)-1][0])

access = True

def Work():
	global access
	what_to_continue = input('Хотите ли вы продолжить? Y/N \n')
	if what_to_continue.lower() == 'n':
		access = False

def Find():
	path = input('Укажите директорию: ')
	count = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
	print("Кол-во файлов в директории: " + str(count))

def Sort():
	global sort

	new_sort = sort

	new_sort.sort(key=lambda x:x[1].split()[0])

	return new_sort

def ChangeNumber():

	global max
	new_sort = Sort()

	id = []

	print('Введите id товаров, у которых хотите изменить количество.\n'
	'stop - остановка ввода id товаров. \n'
	'Максимальный id = ', max)

	workID = True

	while workID:
		numID = input('ID: ')
		if numID.isdigit():
			numID = int(numID)
			if numID <= max:
				id.append(numID)
			else:
				print('Максимальный ID = ', max, ', Вы ввели: ', numID)
		elif numID.lower() == 'stop':
			workID = False
		else:
			print('Неверный ID')

	count = int(input('Введите кол-во единиц товара, на которое хотите увеличить: '))

	for i in range(0, len(new_sort)):
		for j in range(0, len(id)):
			if int(new_sort[i][0]) == int(id[j]):
				new_sort[i][3] = int(new_sort[i][3]) + count
	return new_sort

def Save():
	new_sort = ChangeNumber()
	work = True
	while work:
		answer = input('Вы желаете сохранить результат как новый файл? Y/N \n')
		if answer.lower() == 'y':
			file_name = input('Тогда, введите название файла: ')
			new_file = open(file_name, 'tw', encoding='utf-8')
			for i in range(0, len(new_sort)):
				for j in range(0, len(new_sort[i])):
					if 0 <= j <= 2:
						new_file.write(str(new_sort[i][j]) + ";")
					else:
						new_file.write(str(new_sort[i][j]))
				new_file.write('\n')
		if answer.lower() == 'n':
			new_file = open('products.txt', 'r+')
			for i in range(0, len(new_sort)):
				for j in range(0, len(new_sort[i])):
					if 0 <= j <= 2:
						new_file.write(str(new_sort[i][j]) + ";")
					else:
						new_file.write(str(new_sort[i][j]))
				new_file.write('\n')
			work = False
			new_file.close()
		else:
			work = False

while access:
	cmd = input('Введите команду: ')
	if cmd == "0":
		check_exit = input('Закрыть программу? Y/N \n')
		if check_exit.lower() == 'y' or '1':
			access = False
		elif check_exit.lower() != 'n' or '0':
			print('Неверная команда')
	if cmd == "1":
		Find()
	if cmd == "2":
		print(Sort())
	if cmd == "3":
		print(ChangeNumber())
	if cmd == "4":
		Save()
	if not cmd.isdigit():
		print('Неизвестная команда')
	if not 'check_exit' in globals() or not 'check_exit' in locals():
		Work()