from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import random


class MenuScreen(Screen):
    pass


class CreditsScreen(Screen):
    pass


class QuestionsScreen(Screen):
    score = NumericProperty(0)
    question_number = NumericProperty(1)
    question = StringProperty("")
    answers = []
    correct_answer = ""

    def on_pre_enter(self):
        self.question_number += 1
        self.get_question()

    def get_question(self):
        with open("questions.txt", "r", encoding="utf-8") as f:
            questions = f.read().split("\n\n")
        random_question = random.choice(questions).split("\n")
        self.question = random_question[0]
        self.correct_answer = random_question[1]
        self.answers = random_question[1:]
        random.shuffle(self.answers)

    def on_answer_select(self, answer):
        if answer == self.correct_answer:
            self.score += 1
        self.manager.current = "questions"

    def on_score(self, instance, score):
        self.ids.score_label.text = f"Pontuação: {score}"

    def on_question(self, instance, question):
        self.ids.question_label.text = f"Pergunta {self.question_number}: {question}"
        for i, answer in enumerate(self.answers):
            self.ids[f"answer_button_{i}"].text = answer


class QuizBIOApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(CreditsScreen(name="credits"))
        sm.add_widget(QuestionsScreen(name="questions"))
        return sm


if __name__ == "__main__":
    QuizBIOApp().run()
