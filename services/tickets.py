import time                         # подключаем модуль time
from itertools import product  # составление комбинаций
from random import randint

def str_to_num(line:str)->list[str]:
	numbers: list = []
	if line.find(' ') < 1:  # если совсем нет пробелов, будем считать, что каждая цифра - число
		for n in line:
			if n.isdigit():
				numbers.append(n)
	else:  # если пробелы есть будем искать числа разделенные пробелами
		lines: list = line.split()
		for word in lines:
			if word.replace('.', '').isdigit():
				numbers.append(word)
	return numbers

def str_to_numbers(line:str)->dict:
	result: dict = {}
	line = line.replace(',', ' ').replace(':', ' ').replace(';', ' ').strip()
	nEq = line.find('=')
	numbers: list[str]=[]
	if nEq > 0:  # если есть '='
		numbers = str_to_num(line[:nEq])
		result['pos_eq'] = len(numbers)
		numbers = numbers + str_to_num(line[nEq + 1:])
	else:
		numbers = str_to_num(line)
		result['pos_eq'] = 0
	result['numbers'] = numbers
	return result

def numbers_to_s(numbers:list,oper:str)->str:
	s:str =''
	n_oper: int = len(oper)
	if len(numbers) == 0: return s
	s = str(numbers[0])
	for i in range(n_oper):
		if oper[i] != '_':
			s += oper[i]  # добавляем знак
		s = s + str(numbers[i + 1])  # добавляем следующее число
	return s


def numbers_to_list_pos_eq(numbers:list,pos_eq, all:bool=True, op:str = "_+-*/")->list[str]:
	lines:list[str]=[]
	n_numbers:int = len(numbers)
	n_opersL:int = pos_eq-1
	n_opersR:int = n_numbers-pos_eq-1
	if n_opersL==n_opersR==0:
		return lines
	if n_opersL!=0:
		for operL in product(op, repeat=n_opersL):  # перебираем все доступные варианты как рпсставить (n_op) занков (op)
			sL: str = numbers_to_s(numbers[:pos_eq], operL)
			if sL.find('/0')>0: continue
			if n_opersR!=0:
				for operR in product(op,repeat=n_opersR):  # перебираем все доступные варианты как рпсставить (n_op) занков (op)
					sR: str = numbers_to_s(numbers[pos_eq:], operR)
					if (sR==sL) or (sR.find('/0')>0): continue
					try:
						if eval(sL) == eval(sR):
							lines.append(sL + "=" + sR)
							if not all: return lines
					except:
						continue
			else:
				sR:str = str(numbers[pos_eq])
				if (sR==sL) or (sR.find('/0')>0): continue
				try:
					if eval(sL) == eval(sR):
						lines.append(sL + "=" + sR)
						if not all: return lines
				except:
					continue
	else:
		sL: str = numbers[0]
		for operR in product(op,repeat=n_opersR):  # перебираем все доступные варианты как рпсставить (n_op) занков (op)
			sR: str = numbers_to_s(numbers[pos_eq:], operR)
			if (sR==sL) or (sR.find('/0')>0): continue
			try:
				if eval(sL) == eval(sR):
					lines.append(sL + "=" + sR)
					if not all: return lines
			except:
				continue
	return lines

def solve_ticket(numbers:list, pos_eq:int =0, all:bool=True, op:str = "_+-*/")->list[str]:
	lines:list = []
	n_numbers:int = len(numbers)
	if n_numbers == 0: return lines
	if pos_eq == 0:
		for p in range(n_numbers-1,0,-1):
			lines = lines + numbers_to_list_pos_eq(numbers, p, all, op)
	else:
		lines = lines + numbers_to_list_pos_eq(numbers, pos_eq, all, op)
	return lines

def solve(numbers:list[int|float], pos_eq:int=0, all:bool=True, op:str = "+-*/_")->dict|bool:
	res_dict: dict[str,[list|int|bool|tuple]] = {}
	start = time.thread_time()
	result:list=solve_ticket(numbers,pos_eq,all,op)
	if result:
		res_dict['result']=result
		#	res_dict['op']=op
		res_dict['time']=time.thread_time() - start
		return res_dict
	return False

def numbers_opers(numbers:list, opers:str)->bool:
	n_numbers=len(numbers)
	n_opers=len(opers)
	if (n_numbers-1!=n_opers) or (n_numbers==0): return False
	i = 0
	s = str(numbers[0])
	for op in opers:
		if op!='_' and op!=' ':
			s += op # добавляем знак
		i +=1
		s += numbers[i]	# добавляем следующее число
	pos_eq = s.find('=')
	sL:str = s[:pos_eq]
	sR:str = s[pos_eq+1:]
	try:
		if eval(sL)==eval(sR):
			return True
	except:
		return False
	return False

def gen_ticket(min_n:int, max_n:int, max_m:int, opers:str='+-*_/')->list:
	is_find_ticket = False
	while not is_find_ticket:
		n = randint(min_n,max_n)
		numbers: list = []
		for i in range(n):
			numbers.append(randint(1, max_m))
			result = solve_ticket(numbers, 0, False, opers)
		if result:
			is_find_ticket = True
	ticket:str=result[0]
	for ch in opers+'=':
		ticket=ticket.replace(ch,' ')
	return str_to_num(ticket)

if __name__ == "__main__":
	print(gen_ticket(5, 10, 20, '+-*_/'))
	exit()
	print("Программа билетики может:")
	print("1. Решить задачу")
	print("2. Сгенерировать")
	do = int(input("Выберите действие: "))
	if do == 2:
		print(gen_ticket(5,10,20,'+-*_/'))
		exit()
	print("")
	ln = input("input numbers and result").split() # строка
	# фиксируем время старта работы кода
	start = time.thread_time()
	for s in solve_ticket(ln):
		print(s)
	finish = time.thread_time()  # фиксируем время окончания работы кода
	print('Время работы: ' + str(finish - start))  # вычитаем время старта из времени окончания и выводим результат