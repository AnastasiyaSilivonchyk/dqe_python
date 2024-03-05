import re


def fix_mistakes(original_str):
    fix_mistakes_str = re.sub(r'\siz\s', ' is ', original_str, flags=re.I)
    return fix_mistakes_str


def create_sentence_list(str_wo_mistakes):
    str_split = str_wo_mistakes.replace('\n', '').replace('\t', '').split('.')
    return str_split


def fix_capitalization(input_str_list):
    for i in range(len(input_str_list)):
        input_str_list[i] = input_str_list[i].strip().capitalize()
    return input_str_list


def create_last_sentence(fixed_str):
    new_sentence = []
    for i in fixed_str:
        txt = i.split(' ')
        last_txt = txt[-1]
        if last_txt != '':
            new_sentence.append(last_txt)
    return new_sentence


def calculation_of_spaces(entire_string):
    count_spaces = 0
    for ch in entire_string:
        if ch.isspace():
            count_spaces += 1
    print('The number of spaces: ', count_spaces)

str_txt = """homEwork:
tHis iz your homeWork, copy these Text to variable.



You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

fix_iz_str = fix_mistakes(str_txt)
sent_list = create_sentence_list(fix_iz_str)
fix_case_str = fix_capitalization(sent_list)
lst_sent = create_last_sentence(fix_case_str)
final_str = '. '.join(fix_case_str) + ' '.join(lst_sent).capitalize() + '.'
print(final_str)
calculation_of_spaces(str_txt)