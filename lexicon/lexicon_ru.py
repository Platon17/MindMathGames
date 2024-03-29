from data import max_variants, max_n_tickets

LEXICON_RU: dict[str, str] = {
    # ОБЩИЕ #👥🎲🧩🛤🛣👯‍♀️👐👯👯‍♂️👯‍♂️
    'btn_yes': '✅ <b>ДА!</b>',
    'btn_no': '❌ <b>НЕТ</b>',
    'btn_cancel': '❌ Отменить',
    'btn_back': '⬅️ Назад',
    'btn_home': '🏘 Домой',
    'btn_options': '🔧 Настройки',
    'btn_give_up': '🤲 Сдаюсь!',
    # main menu
    'btn_solve': '🧩️ Решать',
    'btn_train': '🧠 Тренироваться',
    'btn_research': '🧑‍🔬 Исследовать',
    'btn_play': '🎲 Играть',
    'btn_AI': '🦾 Другие ИИ',
    'btn_speak': '🗣 Поговорить',
    'btn_language': '🇷🇺 Язык 🇬🇧',
    'btn_examples': '🎲 Случайный пример',
    # sub menu
    'btn_tickets': '🎫 Билетики',
    'btn_cutting': '✂️ Разрезания',
    'btn_path': '♟ Лучший путь',
    'btn_simm': '👯‍♀️ Симметрия',
    'btn_chet': '🔢 Чётное-нечётное',
    'btn_artur': '🤴 Делёж короля Артура',
    'btn_add': '➕ Добавить',

    'solved':'Кажется я уже решала такую задачу',

    'solve_path': 'Найди лучший путь по этой матрице',
    'for_give_up': 'Если не можешь решить задачу и хочешь узнать ответ - скажи "Сдаюсь"',

    'research_about': 'Здесь Вы можете проводить исследования математических задач',
    'train_about': 'Здесь Вы можете совершенствовать свой интеллект, тренируясь в решении задач разной степени сложности',
    'txt_solve_path': 'Найдите самый дорогой путь, который может пройти хромая ладья, которая может ходить только вниз и вправо, двигаясь из левой верхней клетки в правую нижнюю.',
    'input_path': 'Введите матрицу чисел',

    'txt_solve_artur': 'Король Артур посадил за круглый стол рыцарей и Мерлина, которому вручил золотые монеты. По приказу Артура Мерлин оставил у себя одну монету, а оставшиеся разделил пополам и отдал соседним рыцарям. В каждый следующий момент времени все сидевшие за столом стали поступать аналогично: делить имевшиеся у них деньги на две равные части и отдавать соседям (естественно, тут же получая половину их денег). Тот, у кого оказалось нечетное количество монет, одну оставлял себе и приплюсовывал к сумме, полученной от соседей. Будет ли у всех рыцарей поровну монет после достаточно большого числа таких операций?',
    'input_artur_k': 'Введите количество рыцарей (в том числе и Мерлина):',
    'input_artur_c': 'Введите количество золотых монет, которые Артур вручил Мерлину:',
    'n_operation': 'Количество операций: ',
    'sucsess': 'Успешно поделили!',
    'unsucsess': 'Поделить не получится',

    'txt_solve_simm': 'Задана фигура. Какое минимальное количество клеток нужно удалить для симметричности фигуры. Возможны все виды симметрии.',
    'input_simm': 'Введите фигуру (''+''-фигура, ''другой знак''- пустота)',
    'try_again_simm': 'Введите следующую фигуру (''+''-фигура, ''другой знак''- пустота)',
    
    'txt_solve_chet': 'Задана фигура. В какие клетки нужно поставить точки, чтобы получилось исходная фигура',
    'input_chet': 'Введите фигуру (''+''-фигура, ''другой знак''- пустота)',
    'not_solve_chet': 'Я перепробовала все варианты. Задачу решить невозможно!',
    'try_again_chet': 'Введите другую фигуру (''+''-фигура, ''другой знак''- пустота)',

    'btn_quotes': '☁️ Цитаты',
    'btn_jokes': '😂 Смешное',
    'btn_weather': '🌤 Погода',
    'btn_sport': '🚴 Спорт',
    'btn_politics': '️👮 Политика',

    'btnRU': '🇷🇺 Русский',
    'Russian': 'Русский',
    'btnEN': '🇬🇧English',
    'English': 'English',
    'btnDE': '🇩🇪Deutsche',
    'Deutsche': 'Deutsche',
    'btnCH': '🇨🇳Chinese',
    'Chinese': 'Chinese',
    'btnJP': '🇯🇵Japanese',
    'Japanese': 'Japanese',

    'btn_all_False': 'Только один результат',
    'btn_all_True': 'Все результаты',
    'btn_opers_+-': 'Операторы +-',
    'btn_opers_+-*/': 'Операторы +-*/',
    'btn_opers_+-*/_': 'Операторы +-*/_',
    # ПОИСКИ ПО
    'f_solve': 'реши',
    'f_train': 'задай',

    'f_give_up': 'даюсь',
    'f_ticket': 'билет',
    'f_cutting': 'разрез',
    'f_path': 'путь',
    'f_chet': 'чётн',
    'f_simm': 'симметр',
    'f_artur': 'артур',

    'f_excess_cutting':'лишн',
    'f_n_cutting':'част',
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
    # ЯЗЫК
    # СТАРТ

    'what_lang1':'На каком языке Вы предпочитаете общаться?',
    'what_lang2':'Выберите язык общения.',
    'what_lang3':'Выберите язык.',
    'what_lang4':'На каком языке с Вами следует говорить?',
    'choice_lang': 'Выбери язык общения',
    'solve_lang':'Если захотите поменять язык общения можете просто сказать: "English", "русский", "Deutsch", "Chinese" и другие. И я, тоже, сразу же буду разговаривать с Вами на выбранном языке.',
    
    'lang_unknown':'Я такого языка не знаю. Мне потребуется время, чтобы познакомиться и выучить его.',
    'lang_known':'Я уже начала изучать его, но, пока, не владею им на должном уровне. Поэтому предлагаю, пока, не меня язык общения.',
    
    'hello1':'Привет, меня зовут Гуся!',
    'hello2':'Добрый день, меня зовут Гуся!',
    'hello3':'Рада приветствовать тебя! Меня зовут Гуся!',

    'hello_again1':'Привет! Рада снова тебя видеть!',
    'hello_again2':'Привет! Это снова Вы?',
    'whats_name1':'Как мне тебя называть?',
    'whats_name2':'Как тебя зовут?',
    'whats_name3':'Как ты хочешь, чтобы я к Вам обращалась?',


    'about1':'Я могу решать логические задачи, помогать в их исследовании. Ещё я могу потренировать тебя в их решении. Мы можем поиграть или поболтать, или исследовать искусственные интеллекты.\
    Если тебе что-то непонятно и нужна помощь только спроси!',
    # MAIN MENU
    'home': 'Домой',
    'mm': 'Я много что умею. \nЧто будем делать?',
    'choise_action': 'Выбери действие',
    'solve': 'Решать',
    'reserch': 'Исследовать',
    'train': 'Тренироваться',
    'speak': 'Поговорить',
    'play': 'Играть',
    'AI': 'Искуственные интеллекты',

    'help1':'Для решения задач - скажи: "Решать" или "Реши билетик" или "Найди лучший путь" или "Реши симметрию" и так далее.Если ты хочешь исследовать какую-нибудь задачу просто попроси об этом.Если хочешь потренироваться в решении задач, только попроси: "Задай" или "Задай билетик" или "Спроси лучший путь" и так далее.',
    'solve_about':'Я могу решить логические задачи: Билетики, Разрезание, Лучший путь, Симметрия и другие. Если ты, вдруг, знаешь задачи, которые неизвестны мне, поделись со мной, и я, обязательно, научусь их решать.',

    # РЕШАТЬ

    'txt_solve': 'Выбери задачу!',
    'choise_tasks': 'Выбери задачу',
    'chosen_tickets':'Это одна из моих любимых задач.',
    'need_tickets':'Назовите несколько чисел, и я расставлю знаки так, чтобы  результат будет последним названным Вами числом.\nПожалуйста, не называйте много чисел (не более 10), а не то я могу сильно задуматься.',
    'wrong_ticket':'Неправильный билет',
    'result1':'Это было легко!',
    'result2':'Я сделала это',
    'result_ticket1':'Это было легко!',
    'result_ticket2':'Я сделала это',
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

    # QUOTERS ЦИТАТЫ
    'quote1':'"Знание без границ." - Уильям Шекспир',
    'quote2':'"Обучение - это двигатель профессионального успеха." - Джон Коттер',
    'quote3':'"Знание - это единственное богатство, которое увеличивается, когда его делят." - Сократ',
    'quote4':'"Обучение - это карта к успеху." - Малькольм Форбс',
    'quote5':'"Обучение - это начало перемен." - Гарвардский университет',
    'quote6':'"Обучение - это двигатель технологического прогресса." - Билл Гейтс',
    'quote7':'"Самый лучший способ предсказать будущее - это создать его." - Питер Друкер',
    'quote8':'"Учение - это светлый путь к познанию." - Артур Шопенгауэр',
    'quote9':'"Обучение - это мост от прошлого к будущему." - Фрэнклин Розевелт',
    'quote10':'"Истинное образование - это то, что остается после того, как вы забыли все, что вы узнали." - Альберт Эйнштейн',
    'quote11':'"Учиться можно всю жизнь, и чем больше учишься, тем больше понимаешь, насколько ты ничтожен." - Чарли Мунгер',
    'quote12':'"Чем более образованным становишься, тем меньше пространства видишь для сомнений." - Томас Андерсон',
    'quote13':'"Научись тому, что учишь, и научи тому, что знаешь." - Конфуций',
    'quote14':'"Всякое знание начинается с обучения." - Аристотель',
    'quote15':'"Обучение - это наилучший путь к саморазвитию." - Джон Ф. Кеннеди',
    'quote16':'"Образование - это двигатель научных открытий." - Мария Митчелл',
    'quote17':'"Учиться всегда и везде." - Жан-Жак Руссо',
    'quote18':'"Чем больше ты узнаешь, тем больше поймешь, насколько мало ты знаешь." - Альберт Эйнштейн',
    'quote19':'"Обучение - это двигатель экономического роста." - Джон Ф. Кеннеди',
    'quote20':'"Учиться - это жить дважды." - Марк Твен',
    'quote21':'"Учиться значит расти, а расти значит жить." - Ричард П. Фейнман',
    'quote22':'"Обучение - это начало процесса. Развитие - это результат." - Эдвард Деминг',
    'quote23':'"Знание - это сокровище, которое нельзя украсть." - Альфред Норт Уайтхед',
    'quote24':'"Знание без действия бесполезно." - Аристотель',
    'quote25':'"Обучение - это дар, который никто не может у вас отнять." - Б.Б. Кинг',
    'quote26':'"Образование - это самое мощное оружие, которое вы можете использовать, чтобы изменить мир." - Нельсон Мандела',
    'quote27':'"Обучение - это двигатель инноваций." - Питер Друкер',
    'quote28':'"Учеба - это единственное средство, которое может изменить мир." - Малала Юсуфзай',
    'quote29':'"Учиться - это начало мудрости." - Аристотель',
    'quote30':'"Образование - это оружие массового поражения." - Нельсон Мандела',
    'quote31':'"Каждый человек должен учиться в течение всей жизни." - Джон Ф. Кеннеди',
    'quote32':'"Обучение - это двигатель духовного развития." - Далай Лама',
    'quote33':'"Образование - это двигатель социальной справедливости." - Майкл Фарадэй',
    'quote34':'"Обучение - это сила, а незнание - это бессилие." - Джим Рон',
    'quote35':'"Обучение - это лучший инвестиционный проект." - Энтони Дж. Д''Анджело',
    'quote36':'"Каждая минута обучения приносит пользу в будущем." - Кит Миллер',
    'quote37':'"Обучение - это начало богатства, здоровья и мудрости." - Платон',
    'quote38':'"Нельзя быть слишком образованным." - Конфуций',
    'quote39':'"Обучение - это путь к осуществлению мечты." - Джейми Паолетта',
    'quote40':'"Образование - это корень роста от инфанта до старости." - Джон Дьюи',
    'quote41':'"Образование - это мост от прошлого к будущему." - Фрэнклин Розевелт',
    'quote42':'"Обучение - это двигатель мира." - Маргарет Мид',
    'quote43':'"Образование - это мощнейший инструмент, который вы можете использовать для изменения мира." - Нельсон Мандела',
    'quote44':'"Сложно обучить человека то, что он уже знает." - Джон Локк',
    'quote45':'"Учиться - это открывать двери в мир возможностей." - Фрэнк Шерман',
    'quote46':'"Научиться чему-то новому - это как открывать дверь в новый мир." - Джейсон Биггс',
    'quote47':'"Учись так, будто тебе никогда не придется зарабатывать деньги, и работай так, будто ты никогда не учился." - Уоррен Баффет',
    'quote48':'"Обучение - это двигатель экологического осознания." - Рейчел Карсен',
    'quote49':'"Образование - это те вложения, которые невозможно потерять." - Б.Б. Кинг',
    'quote50':'"Обучение - это инвестиция в будущее." - Джордж Карвер',
    'quote51':'"Не обучение, а обучение делает человека полным." - Демокрит',
    'quote52':'"Обучение - это ключ к раскрытию своего потенциала." - Уинстон Черчилль',
    'quote53':'"Знание - сила." - Фрэнсис Бэкон',
    'quote54':'"Не учиться - значит начать стареть." - Билл Гейтс',
    'quote55':'"Обучение - это двигатель культурного развития." - Альберт Эйнштейн',
    'quote56':'"Обучение - это двигатель творчества." - Леонардо да Винчи',
    'quote57':'"Учеба - это процесс, который продолжается всю жизнь." - Питер Друкер',
    'quote58':'"Знание - это сила, а учение - это ключ к развитию этой силы." - Джим Рон',
    'quote59':'"Образование - это мост из прошлого в будущее." - Франклин D. Roosevelt',
    'quote60':'"Обучение - это двигатель прогресса." - Карл Роджерс',
    'quote61':'"Обучение - это дорога к успеху." - Стейси Джонс',
    'quote62':'"Чтение - это мост от прошлого к будущему." - Маргарет Фуллер',
    'quote63':'"Образование - это путь к успешной карьере." - Майкл Фарадэй',
    'quote64':'"Люди не перестают учиться после окончания школы, они просто меняют учителей." - Уолтер Андерсон',
    'quote65':'"Самая большая опасность для нашего будущего - это невежество." - Джон Ф. Кеннеди',
    'quote66':'"Обучение - это светлый путь к познанию." - Артур Шопенгауэр',
    'quote67':'"Самая важная вещь - это не переставать задаваться вопросами." - Альберт Эйнштейн',
    'quote68':'"Обучение - это сокровище, которое никто не может украсть." - Альфред Норт Уайтхед',
    'quote69':'"Образование - это ключ к открытию золотой клетки." - Джордж Вашингтон Карвер',
    'quote70':'"Обучение - это ключ к самосовершенствованию." - Лоренс Питер',
    'quote71':'"Образование - это ключ к личной свободе." - Опра Уинфри',
    'quote72':'"Учись, как будто ты будешь жить вечно." - Ганди',
    'quote73':'"Чем больше вы узнаете, тем больше сможете сделать. Чем больше сделаете, тем больше достигнете." - Альберт Эйнштейн',
    'quote74':'"Образование - это подарок, который длится всю жизнь." - Чарльз Джеймс',
    'quote75':'"Учись с увлечением, и ты никогда не будешь работать ни дня в своей жизни." - Конфуций',
    'quote76':'"Будьте лучшей версией себя каждый день." - Неизвестный автор',
    'quote77':'"Самая большая инвестиция - это инвестиция в собственное образование." - Альберт Эйнштейн',
    'quote78':'"Самый большой учитель - это опыт." - Леонардо да Винчи',
    'quote79':'"Знание - это сила, но использование знания - это мудрость." - Роберт Келли',
    'quote80':'"Обучение - свет, а невежество - тьма." - Конфуций',
    'quote81':'"Человек всегда должен быть готов к обучению, потому что жизнь никогда не перестает учить." - Генри Форд',
    'quote82':'"Сделайте свой мозг своим лучшим другом." - Ральф Уолдо Эмерсон',
    'quote83':'"Знание - это сила." - Фрэнсис Бэкон',
    'quote84':'"Образование - это ключ к открыванию дверей в мире возможностей." - Барак Обама',
    'quote85':'"Образование - это двигатель социального мобильности." - Малала Юсуфзай',
    'quote86':'"Учиться - это открывать новые горизонты." - Лейоне Гейц',
    'quote87':'"Образование - это двигатель карьерного роста." - Энн Дубовик',
    'quote88':'"Учеба открывает горизонты, но обучение раскрывает потенциал." - Джон C. Maxwell',
    'quote89':'"Обучение - это самый надежный способ изменить свою жизнь." - Нельсон Мандела',
    'quote90':'"Образование - это двигатель прогресса." - Карл Роджерс',
    'quote91':'"Секрет успеха - никогда не останавливаться учиться." - Джон Вуден',
    'quote92':'"Знание - это ключ к возможностям." - Бенджамин Франклин',
    'quote93':'"Знание - это ключ к возможностям, а обучение - это путь к достижению их." - Дэвид Гаффни',
    'quote94':'"Обучение - это путь к лидерству." - Хасан II',
    'quote95':'"Обучение - это процесс открытия мира." - Джордж Уилл',
    'quote96':'"Обучение - это ключ к свободе." - Джордж Вашингтон Карвер',
    'quote97':'"Каждый человек - это новая история, которую нужно изучить." - Чак Паланик',
    'quote98':'"Обучение никогда не бывает бесполезным." - Леонардо да Винчи',
    'quote99':'"Всегда есть место для улучшения." - Шри Чинмой',
    'quote100':'"Обучение - это приключение, которое никогда не заканчивается." - Жозеф Бротовски',
    
    
    
    
    'joke1':'joke',
    'joke2':'joke',
    'joke3':'joke',
    'joke4':'joke',










    'end': 'Конец'
}


