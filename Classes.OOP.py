import random
from datetime import datetime, date
import re
from Functions_M3 import fix_capitalization
import os


class UserInterface:
    """Class for decision making about type of data ingestion"""
    def __init__(self):
        self.input_type = input("Please, select the option of news push:\n"
                                "1.Manual input\n"
                                "2.Input from text file\n")

    def define_manual_input_newstype(self):
        news_type = input("Please, select what type of news you want to publish:\n"
                      "1.News\n"
                      "2.Private ad\n"
                      "3.I want to add my own publication\n")
        return news_type


class Publication:
    """Parent class for any manual publication"""
    def __init__(self):
        self.publication_text = input("Please enter the main text of your publication:\n")


class News(Publication):
    """Class for News manual input"""
    def __init__(self):
        super().__init__()
        self.city = input("Please enter the city:\n")
        self.publ_date = datetime.now()

    def build_news_publication(self):
        news = ["News", self.publication_text, self.city + ", " + str(self.publ_date)]
        return news


class PrivateAd(Publication):
    """Class for Private Ad manual input"""
    def __init__(self):
        super().__init__()
        self.date_exp = datetime.strptime(input("Please enter the expiration date in the format yyyy-mm-dd:\n"), "%Y-%m-%d").date()
        self.days_left = (self.date_exp-date.today()).days

    def build_advertisement_publication(self):
        private_ad = ['Private Ad', self.publication_text, 'Actual until: ' + str(self.date_exp) + ', ' + str(self.days_left) + ' days left']
        return private_ad


class WorkoutExercises(Publication):
    """Class for Excercise manual input"""
    def __init__(self):
        super().__init__()
        self.repeat_set = random.randint(1, 4)
        self.repeat_time = random.randint(10, 20)

    def build_workout(self):
        exercise = ['WorkoutExercise', f"Your today's exercise is {self.publication_text}", f'Please repeat {self.repeat_set} sets of {self.repeat_time} times']
        return exercise


class InputFromTextFile:
    """Class for parsing a publications from a text file"""
    def __init__(self, txt_file_path):
        self.txt_file_path = txt_file_path

    def get_publication_from_text_file(self):
        with open(self.txt_file_path, 'r') as file:
            file_lines = file.readlines()

            publication = []

        for line in file_lines:
            sentences = re.split(r'(?<=[.!?])', line)
            fixed_lines = fix_capitalization(sentences)
            publication.extend(fixed_lines)
        return publication


class PublishToFile:
    """Class for pushing publication into the output file"""
    def __init__(self, publ_type):
        self.publ_type = publ_type
        with open(output_file_path, 'a') as f:
            for line in publ_type:
                f.write(line)
                f.write('\n')
            f.write('-'*20)
            f.write('\n'*4)


# function to check if the particular text in the output file
def is_text_in_file(file_path, text):
    with open(file_path, 'r') as file:
        for line in file:
            if text in line:
                return True
    return False


# get the list of files to parse, only one file is expected at a time
def get_the_file_to_parse(folder_path):
    files_list = os.listdir(folder_path)
    if len(files_list) == 1:
        file_path_to_parse = os.path.join(folder_path, files_list[0])
        return file_path_to_parse
    elif len(files_list) > 1:
        return "There are more than 1 file in the folder."
    else:
        return "No file to process."


output_file_path = "newsfeed.txt"
input_file_path = get_the_file_to_parse('TxtNews')


type_of_publication = UserInterface()

if type_of_publication.input_type == '1':
    news_type = type_of_publication.define_manual_input_newstype()
    if news_type == '1':
        news = News()
        news_to_publish = news.build_news_publication()
        publish = PublishToFile(news_to_publish)
        if is_text_in_file(output_file_path, news_to_publish[1]):
            print(f"News with text '{news_to_publish[1]}' was published.")
        else:
            print(f"News wasn't published.")
    elif news_type == '2':
        private_ad = PrivateAd()
        private_ad_to_publish = private_ad.build_advertisement_publication()
        publish = PublishToFile(private_ad_to_publish)
        if is_text_in_file(output_file_path, private_ad_to_publish[1]):
            print(f"Private Ad with text '{private_ad_to_publish[1]}' was published.")
        else:
            print(f"Private Ad wasn't published.")
    elif news_type == '3':
        own_publ = WorkoutExercises()
        own_publ_to_publish = own_publ.build_workout()
        publish = PublishToFile(own_publ_to_publish)
        if is_text_in_file(output_file_path, own_publ_to_publish[1]):
            print(f"Exercise with text '{own_publ_to_publish[1]}' was published.")
        else:
            print(f"Exercise wasn't published.")
elif type_of_publication.input_type == '2':
    if input_file_path != 'There are more than 1 file in the folder.' and input_file_path != 'No file to process.':
        news_from_text_file = InputFromTextFile(input_file_path)
        news_from_file_to_publish = news_from_text_file.get_publication_from_text_file()
        publish = PublishToFile(news_from_file_to_publish)
        if is_text_in_file(output_file_path, news_from_file_to_publish[1]):
            print(f"The file was successfully processed")
            os.remove(input_file_path)
        else:
            print(f"Publications from the file weren't processed.")
    else:
        print(input_file_path)