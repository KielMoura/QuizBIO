from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, NumericProperty
from kivy.lang import Builder

Builder.load_file("main.kv")

# Definir as perguntas do quiz
QUESTIONS = [
    {
        "text": "Qual é a maior organela da célula?",
        "answers": [
            "Mitocôndria",
            "Complexo de Golgi",
            "Retículo endoplasmático",
            "Núcleo",
            "Lisossomo"
        ],
        "correct_answer": "Núcleo"
    },
    {
        "text": "Qual é a célula responsável pela defesa do organismo?",
        "answers": [
            "Célula-tronco",
            "Célula nervosa",
            "Célula muscular",
            "Célula do sistema imunológico",
            "Célula de Langerhans"
        ],
        "correct_answer": "Célula do sistema imunológico"
    },
    {
        "text": "Qual é o tecido responsável pela condução de impulsos nervosos?",
        "answers": [
            "Epitelial",
            "Muscular",
            "Nervoso",
            "Conjuntivo",
            "Cartilaginoso"
        ],
        "correct_answer": "Nervoso"
    }
]


class MenuScreen(Screen):
    pass


class CreditsScreen(Screen):
    pass


class QuestionsScreen(Screen):
    score = NumericProperty(0)
    question_number = NumericProperty(1)
    question = ObjectProperty(None)
    answer_1 = ObjectProperty(None)
    answer_2 = ObjectProperty(None)
    answer_3 = ObjectProperty(None)
    answer_4 = ObjectProperty(None)
    answer_5 = ObjectProperty(None)

    def on_pre_enter(self, *args):
        # Exibir a primeira pergunta
        self.display_question()

    def display_question(self):
        current_question = QUESTIONS[self.question_number - 1]
        self.question.text = current_question["text"]
        self.answer_1.text = current_question["answers"][0]
        self.answer_2.text = current_question["answers"][1]
        self.answer_3.text = current_question["answers"][2]
        self.answer_4.text = current_question["answers"][3]
        self.answer_5.text = current_question["answers"][4]

    def on_answer_select(self, selected_answer):
        current_question = QUESTIONS[self.question_number - 1]
        if selected_answer == current_question["correct_answer"]:
            self.score += 1
        self.question_number += 1
        if self.question_number <= len(QUESTIONS):
            self.display_question()
        else:
            # Se já exibiu todas as perguntas, exibir a tela de resultados
            self.manager.current = "credits"


class QuizBIOApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(CreditsScreen(name="credits"))
        sm.add_widget(QuestionsScreen(name="questions"))
        return sm


if __name__ == "__main__":
    QuizBIOApp().run()
