#! python3
#-*- coding:UTF-8 -*-
# mcb.pyw - Saves and loads pieces of text to the clipboard.
#
# 			МНОГОЗАРЯДНЫЙ БУФЕР ОБМЕНА
#
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
# in Windows инструкция в книге "автоматизация рутинных задач" на стр 552
# 		win + r  mcb save <keyword>
# 		win + r  py mcb <keyword>
# 		win + r  mcb list
# 		win + r  mcb del <keyword>
# 		win + r  mcb del


import shelve, pyperclip, sys #подключаются модули: shelve - включение
#хранилища информации, pyperclip - для копирования и вставки, sys - для чтения
# аргументов командной строки

mcbShelf = shelve.open('mcb')   #в переменную mcbShelf записывается содержимое
#хранилища mcb

# Save clipboard content. Сохранение содержимого командной строки
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
#Если аргументов в строке 3 и второй из них "save"
    mcbShelf[sys.argv[2]] = pyperclip.paste()
#то третий записывается в переменную mcbShelf в качестве ключа для содержимого
# буфера обмена
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'del':
#Если аргументов в строке 3 и второй из них "del"
    del mcbShelf[sys.argv[2]]
#из хранилища удаляется содержимое с ключем
elif len(sys.argv) == 2:
# в противном случае, если аргументов 2 значит, или запрашивается список ключей
#  или сам контент
# List keywords and load content.
    if sys.argv[1].lower() == 'list':
#если второй аргумент "list"
        pyperclip.copy(str(list(mcbShelf.keys())))
#в буфер обмена передаются все ключи,чтоб посмотреть
    elif sys.argv[1].lower() == 'del':
#если второй аргумент "del"
    	mcbShelf.clear()
#полностью удаляются все значения
    elif sys.argv[1] in mcbShelf:
#если второй аргумент содержится в переменной mcbShelf
        pyperclip.copy(mcbShelf[sys.argv[1]])
#в буфер обмена передается то, для чего он является ключем
mcbShelf.close()
#хранилище выключается