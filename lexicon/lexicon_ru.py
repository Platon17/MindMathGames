from data import max_variants, max_n_tickets

LEXICON_RU: dict[str, str] = {
    # ОБЩИЕ
    'btn_yes': '✅ <b>ДА!</b>',
    'btn_no': '❌ <b>НЕТ</b>',
    'btn_cancel': '❌ Отменить',
    'btn_back': '⬅️ Назад',
    'btn_home': '🏘 Домой',
    # main menu
    'btn_solve': '🧠 Решать',
    'btn_train': '⚔️ Тренироваться',
    'btn_research': '🧑‍🔬 Исследовать',
    'btn_AI': '🦾 Другие ИИ',
    'btn_speak': '🗣 Поговорить',
    'btn_language': '🇷🇺 Язык 🇬🇧',
    # sub menu
    'btn_tickets': '🎫 Билетики',
    'btn_cutting': '✂️ Разрезания',
    'btn_path': 'Лучший путь',
    'btn_simm': 'Симметрия',
    'btn_chet': 'Чётное-нечётное',
    'btn_artur': '🤴 Делёж короля Артура',
    'btn_add': '➕ Добавить',

    'btn_quotes': '☁️ Цитаты',
    'btn_jokes': '😂 Смешное',
    'btn_weather': '🌤 Погода',
    'btn_sport': '🚴 Спорт',
    'btn_politics': '️👮 Политика',

    'btn_options': '🔧 Настройки',
    'btn_give_up': '🤲 Сдаюсь!',
    'btnRU': '🇷🇺 Русский',
    'txtRU': 'Русский',
    'btnEN': '🇬🇧English',
    'txtEN': 'English',
    'btnDE': '🇩🇪Deutsche',
    'txtDE': 'Deutsche',
    'btnCH': '🇨🇳Chinese',
    'txtCH': 'Chinese',
    'btnJP': '🇯🇵Japan',

    'btn_all_False': 'Только один результат',
    'btn_all_True': 'Все результаты',
    'btn_opers_+-': 'Операторы +-',
    'btn_opers_+-*/': 'Операторы +-*/',
    'btn_opers_+-*/_': 'Операторы +-*/_',
    'f_excess_cutting':'част',
    'f_n_cutting':'лишн',
    'f_all_true':'результат',
    'f_all_false':'результат',
    '2_btn_cut':'на 2 части',
    '3_btn_cut':'на 3 части',
    '4_btn_cut':'на 4 части',
    '5_btn_cut':'на 5 частей',
    '6_btn_cut':'на 6 частей',
    '7_btn_cut':'на 7 частей',
    '8_btn_cut':'на 8 частей',
    '0_btn_excess':'нет лишних',
    '1_btn_excess':'1 лишний',
    '2_btn_excess':'2 лишних',
    '3_btn_excess':'3 лишних',
    '4_btn_excess':'4 лишних',
    '5_btn_excess':'5 лишних',
    'but_1': 'Кнопка 1',
    'but_2': 'Кнопка 2',
    'but_3': 'Кнопка 3',
    'but_4': 'Кнопка 4',
    'but_5': 'Кнопка 5',
    'but_6': 'Кнопка 6',
    'but_7': 'Кнопка 7',
    'btn_1': '1',
    'btn_2': '2',
    'btn_3': '3',
    'btn_4': '4',
    'btn_5': '5',
    'btn_6': '6',
    'btn_7': '7',
    'btn_8': '8',
    'btn_9': '9',
    'btn_10': '10',
    'btn_11': '11',
    # ЯЗЫК
    # СТАРТ
    'back': 'Назад',
    'start':    'старт',

    'choice_lang': 'Выбери язык общение.\
    Choice your language',
    'Hello1': 'ПРИВЕТ! Я умею играть в игры!',
    'Hello2': "Здравствуйте. Чтобы начать играть нажмите кнопку '/start'. Чтобы обратиться за помощью нажмите кнопку '/help'.",

    'what_lang1':'На каком языке Вы предпочитаете общаться?',
    'what_lang2':'Выберите язык общения.',
    'what_lang3':'Выберите язык.',
    'what_lang4':'На каком языке с Вами следует говорить?',

    'solve_lang':'Если захотите поменять язык общения можете просто сказать: "English", "русский", "Deutsch", "Chinese" и другие. И я, тоже, сразу же изменю язык общения.',
    
    'lang_unknown':'Я такого языка не знаю. Мне потребуется время, чтобы познакомиться и выучить его.',
    'lang_known':'Я уже начала изучать его, но, пока, не владею им на должном уровне. Поэтому предлагаю, пока, не меня язык общения.',
    
    'hello1':'Привет, меня зовут Гуся!',
    'hello2':'Добрый день, меня зовут Гуся!',
    'hello3':'Рада приветствовать тебя! Меня зовут Гуся!',
    
    'whats_name1':'Как мне тебя называть?',
    'whats_name2':'Как тебя зовут?',
    'whats_name3':'Как ты хочешь, чтобы я к Вам обращалась?',

    'hello_again':'Рада снова тебя видеть!',
    
    'about1':'Я могу решать логические задачи. Помогу в их исследовании. Ещё я могу потренировать тебя в их решении. Мы можем просто поболтать. Или исследовать искусственные интеллекты.\nЯ могу поделиться знаменитой цитатой мли рассказать какую-нибудь смешную историю или анекдот. Если тебе что-то непонятно и нужна помощь только спроси!',
    # MAIN MENU
    'home': 'Домой',
    'mm': 'Я много что умею. \nЧто будем делать?',
    'choise_action': 'Выбери действие',
    'solve': 'Решать',
    'reserch': 'Исследовать',
    'train': 'Тренироваться',
    'speak': 'Поговорить',
    'AI': 'Другие ИИ',
    'options': 'Настройки',

    'help1':'Для решения задач - скажи: "Решать" или "Реши билетик" или "Найди лучший путь" или "Реши симметрию" и так далее.Если ты хочешь исследовать какую-нибудь задачу просто попроси об этом.Если хочешь потренироваться в решении задач, только попроси: "Задай" или "Задай билетик" или "Спроси лучший путь" и так далее.',
    'solve_about':'Я могу решить логические задачи: Билетики, Разрезание, Быстрый путь, Симметрия и другие. Если ты, вдруг, знаешь задачи, которые неизвестны мне, поделись со мной, и я, обязательно, научусь их решать.',


    # РЕШАТЬ
    'f_solve':'реши',
    'f_train':'задай',
    'f_solve1':'найди',

    'txt_solve': 'Выбери задачу!',
    'choise_tasks': 'Выбери задачу',

    'tickets': 'Билетики',
    'cutting': 'Разрезание',
    'simm': 'Симметрия',
    'chet': 'Чёт-нечёт',
    'path': 'Путь',
    'artur': 'Делёж короля Артура',
    'add': 'Добавить',


    'f_give_up':'даюсь',
    'f_ticket':'билет',
    'f_cutting':'разрез',
    'f_path':'путь',
    'f_chet':'чётн',
    'f_simm':'симметр',
    'f_artur':'артур',

    'give_up':'Сдаюсь!',

    'chosen_tickets':'Это одна из моих любимых задач.',
    'need_tickets':'Назовите несколько чисел, и я расставлю знаки так, чтобы  результат будет последним названным Вами числом.\nПожалуйста, не называйте много чисел (не более 10), а не то я могу сильно задуматься.',
    'wrong_ticket':'Неправильный билет',


    'result_ticket1':'Это было легко!',
    'result_only_max':f'Я нашла очень много вариантов. Пожалуй, я покажу Вам только {max_variants} из них. В настройках можно изменить варианты операций.',
    'result_time1':'И заняло у меня всего секунд.',
    'result_time2':'Мне потребовалось всего секунд.',
    'result_all1':'Посмотри сколько у меня есть вариантов:',
    'wait_more1':'Жду следующую задачу....',
    
    'wrong1':'Всё перепробовала. Это невозможно.',
    
    'wrong_time':' Это займёт очень много времени. Задай другую задачу.',

    'solve_оptions':'Вы можешь изменить параметры задачи, просто скажи: "Настройки \
Вы можете изменить доступные знаки. \
Например: ''operates=+-'' оставит из всех возможных операций только сложение и вычитание.\
Если вам нужны все возможные варианты, скажите: "Все", а если Вас интересуют любой, попросите: "Только один" или "Любой".',

    'tickets_оptions':'Вы можешь изменить параметры задачи, просто скажи: "Настройки \
Вы можете изменить доступные знаки. \
Например: ''operates=+-'' оставит из всех возможных операций только сложение и вычитание.\
Если вам нужны все возможные варианты, скажите: "Все", а если Вас интересуют любой, попросите: "Только один" или "Любой".',

    #CUTTING
    'f_cut':'разрез',
    'give_up':'Сдаюсь!',

    'chosen_cutting':'Это моя любимая задача.',
    'need_cutting':'введите несколько строк где ''+'' - клетка занятая фигурой',
    'wrong_cutting':'Неправильный ввод данных',
    'not_solve_cutting':'Вашу фигуру невозможно разрезать',
    'try_again_cutting':'Введите другую фигуру',


    'result_cutting1':'Это было легко!',
    'try_again_path': 'Введите другую матрицу чисел.',
    'txt_research':'Исследование оче',
    'txt_speak':'Я очень люблю болтать',
    'politics':'politics',
    'quote':'quote',
    'joke':'joke',
    'weather':'weather',

    'quote1':'quote',
    'quote2':'quote',
    'quote3':'quote',
    'quote4':'quote',
    'joke1':'joke',
    'joke2':'joke',
    'joke3':'joke',
    'joke4':'joke',










    'end': 'Конец'
}
