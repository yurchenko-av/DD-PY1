def get_count_char(str_):
        str_low = ''.join(str_.lower().split())
        marks = ('.', ',', '!', '/n')
        str_only_char = str_low.replace(marks, '')
        dict_count_char = {}
        DEFAULT_COUNT = 0
        for char in str_only_char:
            if str_only_char.isalpha():
                dict_count_char[char] = dict_count_char.get(dict_count_char, DEFAULT_COUNT) + 1
        return dict_count_char


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
