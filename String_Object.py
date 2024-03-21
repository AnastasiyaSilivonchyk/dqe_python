input_txt = """homEwork:
tHis iz your homeWork, copy these Text to variable.



You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""


split_text = input_txt.replace('\n', '').split('.')


for i in range(len(split_text)):
    split_text[i] = split_text[i].strip().capitalize().replace(' iz', ' is')


new_sentence = []

for i in split_text:
    txt = i.split(' ')
    last_txt = txt[-1]
    if last_txt != '':
        new_sentence.append(last_txt)


final_string = '. '.join(split_text) + ' '.join(new_sentence).capitalize() + '.'
print(final_string)

cnt_spaces = 0

for i in input_txt:
    if i.isspace():
        cnt_spaces += 1


print('The amount of spaces: ', cnt_spaces)