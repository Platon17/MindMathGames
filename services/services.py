from aiogram.fsm.context import FSMContext
from var import user_dict
from random import randint

#  Мультиязычность
from lexicon.lexicon_ru import LEXICON_RU  # подключаем лексикон русского языка
from lexicon.lexicon_en import LEXICON_EN  # подключаем лексикон английского языка
from lexicon.symbols import SYMBOLS  # подключаем лексикон английского языка

def _sym(param: str) -> str:
    return SYMBOLS.get(param,param)

def _sLine(line: str) -> str:
    newLine:str = ''
    for ch in line:
        newLine = newLine + _sym(ch)
    return newLine

lexicon = {
    'ru': LEXICON_RU,
    'en': LEXICON_EN
}

def _sPath(line: str) -> str:
    newLine: str = ''
    n:int = 0
    for ch in line:
        if ch == 'R':
            n+=1
    after = 0
    before = n
    for ch in line:
        newLine = newLine + _sym(ch)
        if ch == 'R':
            after = after+1
            before = n - after
        if ch == 'D':
            newLine = newLine + _sym('_')*before + '\n' + _sym('_')*after
    return newLine + _sym('#')

lexicon = {
    'ru': LEXICON_RU,
    'en': LEXICON_EN
}

# язык смотрит в словаре
def _txt(param: str, id:int) -> str:
    n: int = 0
    k: int = 0
    for i in range(len(param) - 1, 0, -1):
        if param[i].isdigit():
            k += 1
            n += int(param[i]) * 10 ** (k - 1)
        else:
            break
    if n > 1:
        param = param[0:-k] + str(randint(1, n))
    lang = user_dict[id].get('lang', 'ru')
    return lexicon.get(lang, lexicon[lang]).get(param, param)
def _some(param: str, id:int) -> list:
    result:list =[]
    n: int = 0
    k: int = 0
    for i in range(len(param) - 1, 0, -1):
        if param[i].isdigit():
            k += 1
            n += int(param[i]) * 10 ** (k - 1)
        else:
            break
    lang = user_dict[id].get('lang', 'ru')
    if n > 1:
        base:str = param[0:-k]
        for i in range(1,n):
            param = base + str(i)
            result.append(lexicon.get(lang, lexicon[lang]).get(param, param))
    else:
        result.append(lexicon.get(lang, lexicon[lang]).get(param, param))

    return result

def _text(param: str, lang: str = 'ru') -> str:
    n: int = 0
    k: int = 0
    for i in range(len(param) - 1, 0, -1):
        if param[i].isdigit():
            k += 1
            n += int(param[i]) * 10**(k-1)
        else:
            break
    if n > 1:
        param = param[0:-k] + str(randint(1, n))
    return lexicon.get(lang, lexicon[lang]).get(param, param)
# асинхронная функция, язык смотрит из состояния
async def _atext(param: str, state: FSMContext=None) -> str:
    n: int = 0
    k: int = 0
    for i in range(len(param) - 1, 0, -1):
        if param[i].isdigit():
            k += 1
            n += int(param[i]) * 10 ** (k - 1)
        else:
            break
    if n > 1:
        param = param[0:-k] + str(randint(1, n))
    lang = 'ru'
    if state:
        lang = await state.get_data().get('lang','ru')
    return lexicon.get(lang, lexicon[lang]).get(param, param)


