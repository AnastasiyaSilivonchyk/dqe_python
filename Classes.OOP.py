import random
from datetime import datetime, date


class UserInterface:
    def __init__(self):
        self.news_type = input("Please, select what type of news you want to publish:\n"
                      "1.News\n"
                      "2.Private ad\n"
                      "3.I want to add my own publication\n")


class Publication:
    def __init__(self):
        self.publication_text = input("Please enter the main text of your publication:\n")


class News(Publication):
    def __init__(self):
        super().__init__()
        self.city = input("Please enter the city:\n")
        self.publ_date = datetime.now()

    def build_news_publication(self):
        news = ["News", self.publication_text, self.city + ", " + str(self.publ_date)]
        return news


class PrivateAd(Publication):
    def __init__(self):
        super().__init__()
        self.date_exp = datetime.strptime(input("Please enter the expiration date in the format yyyy-mm-dd:\n"), "%Y-%m-%d").date()
        self.days_left = (self.date_exp-date.today()).days

    def build_advertisement_publication(self):
        private_ad = ['Private Ad', self.publication_text, 'Actual until: ' + str(self.date_exp) + ', ' + str(self.days_left) + ' days left']
        return private_ad


class WorkoutExercises(Publication):
    def __init__(self):
        super().__init__()
        self.repeat_set = random.randint(1, 4)
        self.repeat_time = random.randint(10, 20)

    def build_workout(self):
        exercise = ['WorkoutExercise', f"Your today's exercise is {self.publication_text}", f'Please repeat {self.repeat_set} sets of {self.repeat_time} times']
        return exercise


class PublishToFile:
    def __init__(self, publ_type):
        self.publ_type = publ_type
        with open(file_path, 'a') as f:
            for line in publ_type:
                f.write(line)
                f.write('\n')
            f.write('-'*20)
            f.write('\n'*4)


def is_text_in_file(file_path, text):
    with open(file_path, 'r') as file:
        for line in file:
            if text in line:
                return True
    return False

file_path = "newsfeed.txt"


type_of_publication = UserInterface()

if type_of_publication.news_type == '1':
    news = News()
    news_to_publish = news.build_news_publication()
    publish = PublishToFile(news_to_publish)
    if is_text_in_file(file_path, news_to_publish[1]):
        print(f"News with text '{news_to_publish[1]}' was published.")
    else:
        print(f"News wasn't published.")
elif type_of_publication.news_type == '2':
    private_ad = PrivateAd()
    private_ad_to_publish = private_ad.build_advertisement_publication()
    publish = PublishToFile(private_ad_to_publish)
    if is_text_in_file(file_path, private_ad_to_publish[1]):
        print(f"Private Ad with text '{private_ad_to_publish[1]}' was published.")
    else:
        print(f"Private Ad wasn't published.")
elif type_of_publication.news_type == '3':
    own_publ = WorkoutExercises()
    own_publ_to_publish = own_publ.build_workout()
    publish = PublishToFile(own_publ_to_publish)
    if is_text_in_file(file_path, own_publ_to_publish[1]):
        print(f"Exercise with text '{own_publ_to_publish[1]}' was published.")
    else:
        print(f"Exercise wasn't published.")