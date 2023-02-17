from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import NumericProperty, StringProperty, ListProperty
from kivy.clock import Clock
from kivy.lang import Builder

Builder.load_file("main.kv")

class Quiz(Screen):
    score = NumericProperty(0)
    question_number = NumericProperty(1)
    question = StringProperty()
    options = ListProperty([])
    answer = StringProperty()

    def on_enter(self, *args):
        self.load_question()

    def load_question(self):
        questions = [
            {
                "question": "Qual o maior planeta do sistema solar?",
                "options": ["Marte", "Vênus", "Júpiter", "Saturno", "Terra"],
                "answer": "Júpiter"
            },
            {
                "question": "Qual o elemento químico mais abundante na crosta terrestre?",
                "options": ["Oxigênio", "Silício", "Alumínio", "Ferro", "Cálcio"],
                "answer": "Oxigênio"
            },
            {
                "question": "Quem é o autor do livro 'Grande Sertão: Veredas'?",
                "options": ["Machado de Assis", "Guimarães Rosa", "Jorge Amado", "Clarice Lispector", "Lima Barreto"],
                "answer": "Guimarães Rosa"
            }
        ]

        question = questions[self.question_number - 1]
        self.question = question["question"]
        self.options = question["options"]
        self.answer = question["answer"]

    def check_answer(self, answer):
        if answer == self.answer:
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
sm.add_widget(Quiz(name="quiz"))
sm.add_widget(Result(name="result"))

class QuizApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    QuizApp().run()