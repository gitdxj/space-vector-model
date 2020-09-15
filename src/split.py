# -*- coding: utf-8 -*-
import re


def split_word(string):
    str = string
    # trans SPECIAL CHARACTER
    str = re.sub(r'Prof\.|prof\.', 'professor', str)
    str = re.sub(r'ies\W|ies$', 'i ', str)
    str = re.sub(r'i\'m|I\'m', 'I am ', str)
    str = re.sub(r'it\'s|It\'s', 'It is ', str)
    str = re.sub(r'can\'t|Can\'t', 'can not', str)
    str = re.sub(r'doesn\'t|Doesn\'t', 'does not', str)
    str = re.sub(r'\'re', " are", str)
    str = re.sub(r'i\W|i$', 'y ', str)
    str = re.sub(r's\W|s$', ' ', str)
    str = re.sub(r'let\'|Let\'', 'let us', str)
    str = re.sub(r'\Wy\W|\Wy$', ' I ', str)  # 针对i的修正
    str = re.sub(r'\Wi\W|\Wi$', ' is ', str)  # 针对is的修正

    outcome = []

    # match
    while len(str) > 0:
        while str[0] == ' ':
            str = re.sub(' ', '', str, count=1)

        pattern_date = re.compile(r'(\d{4})/(10|11|12|0\d{1}|\d{1})(/([12]\d{1}|3[01]|0\d{1}|\d{1}))?(^/)*')
        match_date = re.match(pattern_date, str)

        if match_date:
            # print('[' + match_date.group() + ']', end=' ')
            outcome.append(match_date.group())
            str = re.sub(pattern_date, '', str, count=1, flags=0)
            continue

        # match percentage
        pattern_percentage = re.compile(r'[\+|\-]?\d+(.\d+)?%')
        match_percentage = re.match(pattern_percentage, str)
        if match_percentage:
            # print('[' + match_percentage.group() + ']', end=' ')
            outcome.append(match_percentage.group())
            str = re.sub(pattern_percentage, '', str, count=1, flags=0)
            continue

        # match number
        pattern_num = re.compile(r'[0-9]+(,[0-9]+)*(.[0-9]+)*')  # ATTENTION 无法分辨每个, 之间的数位
        match_num = re.match(pattern_num, str)
        if match_num:
            # print('[' + match_num.group() + ']', end=' ')
            outcome.append(match_num.group())
            str = re.sub(pattern_num, '', str, count=1, flags=0)
            continue

        # NORMAL PART
        while str[0] == ',':
            str = re.sub(',', '', str, count=1)
        while str[0] == '.':
            str = re.sub('.', '', str, count=1)
        while str[0] == ' ':
            str = re.sub(' ', '', str, count=1)

        match_space = re.search(r' ', str)
        if match_space:
            u1, u2 = str.split(' ', 1)
            str = u2

            # match comma
            pattern_comma = re.compile(r'\w+,')
            match_comma = re.match(pattern_comma, u1)
            if match_comma:
                # print('[' + u1.split(',', 1)[0] + ']', end=' ')
                outcome.append(u1.split(',', 1)[0])
                continue

            # match dot
            pattern_dot = re.compile(r'\w+\.')
            match_dot = re.match(pattern_dot, u1)
            if match_dot:
                # print('[' + u1.split('.', 1)[0] + ']', end=' ')
                outcome.append(u1.split('.', 1)[0])
                continue

            # print('[' + u1 + ']', end=' ')
            outcome.append(u1)

        else:
            u1 = str

            # match comma
            pattern_comma = re.compile(r'\w+,')
            match_comma = re.match(pattern_comma, u1)
            if match_comma:
                # print('[' + u1.split(',', 1)[0] + ']', end=' ')
                outcome.append(u1.split(',', 1)[0])
                str = str.split(',', 1)[1]
                continue

            # match dot
            pattern_dot = re.compile(r'\w+\.')
            match_dot = re.match(pattern_dot, u1)
            if match_dot:
                # print('[' + u1.split('.', 1)[0] + ']', end=' ')
                outcome.append(u1.split('.', 1)[0])
                str = str.split('.', 1)[1]
                continue

            # print('[' + u1 + ']', end=' ')
            string_list = [letter for letter in str]
            string_list[0] = ''
            str = ''.join(string_list)
            # str[0] = '' #TypeError: 'str' object does not support item assignment
    return outcome



