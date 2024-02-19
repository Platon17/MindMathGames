from data import max_variants, max_n_tickets

LEXICON_EN: dict[str, str] = {
    # ОБЩИЕ #
    'btn_yes': '✅ <b>YES!</b>',
    'btn_no': '❌ <b>NO</b>',
    'btn_cancel': '❌ Cancel',
    'btn_back': '⬅️ Back',
    'btn_home': '🏘 Home',
    'btn_options': '🔧 Options',
    'btn_give_up': '🤲 Give up!',
    # main menu
    'btn_solve': '🧩️ Solve',
    'btn_train': '🧠 Train',
    'btn_research': '🧑‍🔬 Research',
    'btn_play': '🎲 Play',
    'btn_AI': '🦾 AI',
    'btn_speak': '🗣 Speak',
    'btn_language': '🇷🇺 Language 🇬🇧',
    'btn_examples': '🎲 Random examples',
    # sub menu
    'btn_tickets': '🎫 Tickets',
    'btn_cutting': '✂️ Cutting',
    'btn_path': '♟ Best Path',
    'btn_simm': '👯‍♀️ Simm',
    'btn_chet': '🔢 Ord-or-noord',
    'btn_artur': '🤴 King Artur',
    'btn_add': '➕ Add',

    'solve_path': 'Search the best path in this matrix',
    'for_give_up': 'Say Give Up, if you dont solve ti',

    'research_about': 'Research is ...',
    'train_about': 'Train is ...',
    'txt_solve_path': 'Search the best path in this matrix',
    'input_path': 'Введите матрицу чисел',

    'txt_solve_artur': 'task King Artur....',
    'input_artur_k': 'Input number of knights: ',
    'input_artur_c': 'Input number of coins ',
    'n_operation': 'Number of knights: ',
    'sucsess': 'Sucsess!',
    'unsucsess': 'Not sucsess!',

    'btn_quotes': '☁️ Quotes',
    'btn_jokes': '😂 Funny',
    'btn_weather': '🌤 Weather',
    'btn_sport': '🚴 Sport',
    'btn_politics': '️👮 Politics',

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

    'btn_all_False': 'Only one result',
    'btn_all_True': 'All results ',
    'btn_opers_+-': 'Operations +-',
    'btn_opers_+-*/': 'Operations +-*/',
    'btn_opers_+-*/_': 'Operations +-*/_',
    # ПОИСКИ ПО
    'f_solve': 'solve',
    'f_train': 'train',

    'f_give_up': 'give up',
    'f_ticket': 'ticket',
    'f_cutting': 'cutting',
    'f_path': 'path',
    'f_chet': 'ord',
    'f_simm': 'simmetr',
    'f_artur': 'artur',

    'f_excess_cutting': 'excess',
    'f_n_cutting': 'part',
    '2_btn_cut': 'to 2 parts',
    '3_btn_cut': 'to 3 parts',
    '4_btn_cut': 'to 4 parts',
    '5_btn_cut': 'to 5 parts',
    '6_btn_cut': 'to 6 parts',
    '7_btn_cut': 'to 7 parts',
    '8_btn_cut': 'to 8 parts',
    '0_btn_excess': 'no excess',
    '1_btn_excess': '1 excess',
    '2_btn_excess': '2 excess',
    '3_btn_excess': '3 excess',
    '4_btn_excess': '4 excess',
    '5_btn_excess': '5 excess',
    # ЯЗЫК
    # СТАРТ

    'what_lang1': 'What language do you speak?',
    'what_lang2': 'What language do you prefer?',
    'what_lang3': 'Do you speak...',
    'what_lang4': 'what_lang4',
    'choice_lang': 'What language do you speak?',
    'solve_lang': 'For change language say: "English", "русский", "Deutsch", "Chinese" or other',

    'lang_unknown': 'I don''t speak it. I need time for know it',
    'lang_known': 'I have started to study it. But...',

    'hello1': 'Hi, my name is Gusya!',
    'hello2': 'Hello, my name is Gusya!',
    'hello3': 'Welcome, my name is Gusya!',

    'hello_again1': 'Hello! Glad to se you again',
    'hello_again2': 'Hello! Glad to se you again',
    'whats_name1': 'What''s you name?',
    'whats_name2': 'What''s you name?',
    'whats_name3': 'What''s you name?',

    'about1': 'I can solve tasks, help in your research, train to solve tasks, play, speak... ',
    # MAIN MENU
    'home': 'home',
    'choise_action': 'Choise action',
    'solve': 'Solve',
    'reserch': 'Research',
    'train': 'Train',
    'speak': 'Speak',
    'play': 'Play',
    'AI': 'AI',

    # РЕШАТЬ

    'txt_solve': 'Choice task',
    'choise_tasks': 'choise task',
    'chosen_tickets': 'It is one of the my favorite tasks',
    'need_tickets': 'Say numbers',
    'wrong_ticket': 'wrong ticket',
    'result1': 'It is easy!',
    'result2': 'I have done it!',
    'result_ticket1': 'It is easy!',
    'result_ticket2': 'I have done it!',
    'result_only_max': f'I have find many variants. I say you only {max_variants}',
    'result_all1': 'Watch how many variants I have:',
    'wait_more1': 'Wait next task....',

    'wrong1': 'It is imposible',

    # CUTTING
    'f_cut': 'cut',
    'give_up': 'give up',

    'chosen_cutting': 'It is one of the my favorite tasks',
    'need_cutting': '''+'''' - dot of figure',
    'wrong_cutting': 'wrong',
    'not_solve_cutting': 'It is impossible',
    'try_again_cutting': 'Input other tasks',

    'result_cutting1': 'It is easy!',
    'try_again_path': 'Input other matrix of path',
    'txt_research': 'Research ....',
    'txt_speak': 'I real like speak...',
    'politics': 'politics',
    'quote': 'quote',
    'joke': 'joke',
    'weather': 'weather',

    # QUOTERS ЦИТАТЫ

    'joke1': 'joke',
    'joke2': 'joke',
    'joke3': 'joke',
    'joke4': 'joke',

    'end': 'end'
}


