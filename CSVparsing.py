import csv
import re
from datetime import datetime, date


news_file = open('newsfeed.txt', 'r')
input_text = news_file.read()
modif_text = input_text.replace('\n', ' ').split(' ')
date_current = datetime.now().strftime("%Y%m%d_%H%M%S")


def get_words_list(text_from_file):
    word_lst = []
    for i in text_from_file:
        word = re.sub("[^A-Za-z]", "", i)
        word_lst.append(word)
    return word_lst


def get_letter_list(word_list):
    letter_list = []
    for i in range(len(word_list)):
        if word_list[i] != '':
            for letter in word_list[i]:
                letter_list.append(letter)
    return letter_list


def get_output_data(word_letter_list):
    cnt_common = {}
    cnt_upper = {}
    for strg in word_letter_list:
        lower_case_text = strg.lower()
        cnt_common[lower_case_text] = cnt_common.get(lower_case_text, 0) + 1
        if strg.isupper():
            cnt_upper[lower_case_text] = cnt_upper.get(lower_case_text, 0) + 1
    return cnt_common, cnt_upper


def write_words_file(word_list):
    file_name = f"OutputCSV/word_count_{date_current}.csv"
    with open(file_name, 'w', newline='') as WordCntFile:
        writer = csv.writer(WordCntFile)
        for word, cnt in word_list.items():
            writer.writerow([word, cnt])


def write_letter_file(letter_common, letter_upper, letter_list):
    header_list = ['letter', 'count_all', 'count_uppercase', 'percentage']
    with open(f'OutputCSV/letter_count_{date_current}.csv', 'w', newline='') as LetterCntFile:
        writer = csv.DictWriter(LetterCntFile, fieldnames=header_list)
        writer.writeheader()
        for letter, cnt in letter_common.items():
            writer.writerow({'letter': letter, 'count_all': cnt, 'count_uppercase': letter_upper.get(letter, 0), 'percentage': (cnt/len(letter_list))*100})

words = get_words_list(modif_text)
letter = get_letter_list(words)
words_for_file = get_output_data(words)[0]
letter_common_for_file, letter_upper_for_file = get_output_data(letter)[0], get_output_data(letter)[1]

write_words_file(words_for_file)

write_letter_file(letter_common_for_file, letter_upper_for_file, letter)
