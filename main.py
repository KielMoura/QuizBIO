from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import NumericProperty, StringProperty, ListProperty
from kivy.clock import Clock
from kivy.lang import Builder

import random

Builder.load_file("main.kv")

class Quiz(Screen):
    score = NumericProperty(0)
    question_number = NumericProperty(1)
    question = StringProperty()
    correct_option = NumericProperty()
    option1 = StringProperty('Option 1')
    option2 = StringProperty('Option 2')
    option3 = StringProperty('Option 3')
    option4 = StringProperty('Option 4')
    options = [option1, option2, option3, option4]
    
    # Resto da implementação da classe...


    def on_enter(self, *args):
        self.load_question()

    def load_question(self):
        questions = {
            "Qual é a capital da França?": ["Berlim", "Paris", "Londres", "Madrid", "Roma"],
            "Qual é a montanha mais alta do mundo?": ["Everest", "Aconcágua", "K2", "Denali", "Mont Blanc"],
            "Qual é o maior país do mundo em área territorial?": ["Canadá", "Estados Unidos", "China", "Rússia", "Brasil"]
        }

        question = random.choice(list(questions.keys()))

        self.question = question
        options = questions[question]
        if len(options) < 5:
            options += [""] * (5 - len(options))
        if questions[question][1] not in options:
            options[4] = questions[question][1]
        random.shuffle(options)
        self.option1 = options[0]
        self.option2 = options[1]
        self.option3 = options[2]
        self.option4 = options[3]
        self.option5 = options[4]
        self.correct_option = options.index(questions[question][1]) + 1

    def check_answer(self, answer):
        if answer == self.correct_option:
            self.score += 10
        self.question_number += 1
        if self.question_number > 3:
            sm.current = "result"
        else:
            Clock.schedule_once(lambda dt: self.load_question())

class Result(Screen):
    score = NumericProperty(0)

class ScreenManagement(ScreenManager):
    pass

sm = ScreenManagement()
sm.add_widget(Quiz(name="Quiz"))
sm.add_widget(Result(name="result"))

class QuizApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    QuizApp().run()
