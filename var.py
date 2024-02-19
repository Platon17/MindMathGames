from aiogram.fsm.storage.redis import Redis
import json
# Перемнные чтобы были доступны из любых модулей
# Создаем "базу данных" пользователей

user_dict: dict = {}
chet_dict: dict ={}
tickets_dict: dict ={}
cutting_dict: dict ={}

#redis = Redis(host='localhost')

tasks_dict:dict ={
	'tickets':{
		'1 2 3':'1+2=3',
		'2 2 4':'2+2=34'
	},
	'cutting':{
		'++/n++':'++/nHH',
		'++++':'++HH',
    	'+/n+/n+/n+':'+/n+/nH/nH',
	},
	'path':{
		'123/n123/n123':12,
		'125/n125/n125':18,
		'312/n312/n312':12,
	},
	'simm':{
		'++/n++':'__/n__',
		'++++':'____',
    	'+/n+/n+/n+':'_/n_/n_/n_',
	},
	'chet':{
		'+++/n+++/n+++':'__/n_+_/n___',
		'+++':'_+_',
	},
}