from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import NumericProperty, ObjectProperty
from kivy.core.window import Window

Window.size= 320, 650

# Definição do gerenciador de tela
class JanelaGerenciadora(ScreenManager):
    pass

# Definição da tela principal
class MenuScreen(Screen):
    pass

# Definição da tela de créditos
class CreditsScreen(Screen):
    pass


# Definição da tela de perguntas
class QuestionsScreen(Screen):
    score = NumericProperty(0)
    question_number = NumericProperty(1)
    question = ObjectProperty(None)
    answer_1 = ObjectProperty(None)
    answer_2 = ObjectProperty(None)
    answer_3 = ObjectProperty(None)
    answer_4 = ObjectProperty(None)
    answer_5 = ObjectProperty(None)

    # Lista de perguntas e respostas
    questions = [
        {
            "question": "Qual é a capital da França?",
            "answers": [
                "Londres",
                "Madrid",
                "Paris",
                "Berlim",
                "Roma"
            ],
            "correct_answer": "Paris"
        },
        {
            "question": "Qual é o maior animal terrestre?",
            "answers": [
                "Elefante",
                "Girafa",
                "Rinoceronte",
                "Hipopótamo",
                "Leão"
            ],
            "correct_answer": "Elefante"
        },
        {
            "question": "Qual é a capital da Austrália?",
            "answers": [
                "Sydney",
                "Melbourne",
                "Canberra",
                "Brisbane",
                "Adelaide"
            ],
            "correct_answer": "Canberra"
        }
    ]

    # Inicialização da tela de perguntas
    def on_enter(self):
        self.load_question()

    # Carrega a próxima pergunta na tela
    def load_question(self):
        question_data = self.questions[self.question_number - 1]
        self.question.text = question_data["question"]
        self.answer_1.text = question_data["answers"][0]
        self.answer_2.text = question_data["answers"][1]
        self.answer_3.text = question_data["answers"][2]
        self.answer_4.text = question_data["answers"][3]
        self.answer_5.text = question_data["answers"][4]

    # Lida com a seleção de uma resposta
    def on_answer_select(self, answer_text):
        question_data = self.questions[self.question_number - 1]
        if answer_text == question_data["correct_answer"]:
            self.score += 1
        self.question_number += 1
        if self.question_number > len(self.questions):
            self.manager.current = "menu"
        else:
            self.load_question()


# Definição do aplicativo
class QuestionsApp(MDApp):
    def build(self):
        self.title = "QuizBio"
#        screen_manager = Builder.load_file('main.kv')
#        return screen_manager
        return Builder.load_file('main.kv')

QuestionsApp().run()

