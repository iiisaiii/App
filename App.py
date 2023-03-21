from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.clock import Clock

Builder.load_string(
    """
<QuestionScreen>:

    BoxLayout:
        orientation: "vertical"
        size: root.width, root.height
        padding : 20
        spacing: 70
        height: self.minimum_height
        canvas.before:
            Color: 
                rgba: 0.1, 1, 0.7, 1
            Rectangle: 
                pos: self.pos
                size: self.size

        RelativeLayout:

            Label:
                id: Label_Ad
                text: "Adınız nedir?:"
                color: 0.5,0.5,0.7
                font_size: 25
                pos_hint: {"center_x": 0.5, "top": 1}

            TextInput:
                id: spinner_name
                font_size: 20
                multiline: True  # set multiline to True
                size_hint_y: None
                height: max(self.minimum_height, 20)
                pos_hint: {"center_x": 0.5, "top": 0}
                on_text: root.spinner_1(self.text)

        RelativeLayout:

            Label:
                text: "Cinsiyetiniz nedir?:"
                color: 0.5,0.5,0.7
                font_size: 25
                pos_hint: {"center_x": 0.5, "top": 1}

            Spinner:
                id: spinner_gender
                text: "Cinsiyet"
                font_size: 20
                size_hint_x: None
                size_hint: 0.4, 0.8
                values: ["Erkek", "Kadın"]
                pos_hint: {"center_x": 0.5, "top": 0}
                on_text: root.spinner_2(self.text)
                canvas.before:
                    Color: 
                        rgba: 1, 1, 1, 1
                    Rectangle: 
                        pos: self.pos
                        size: self.size


        RelativeLayout:

            Label:
                text: "Medeni haliniz nedir?:"
                color: 0.5,0.5,0.7
                font_size: 25
                pos_hint: {"center_x": 0.5, "top": 1}

            Spinner:
                id: spinner_medeni
                text: "Medeni Hal"
                font_size: 20
                size_hint_x: None
                size_hint: 0.4, 0.8
                values : ["Evli" , "Bekar"]
                pos_hint: {"center_x": 0.5, "top": 0}
                on_text: root.spinner_4(self.text)


        RelativeLayout:

            Label:
                text: "Mesleğiniz nedir?:"
                color: 0.5,0.5,0.7
                font_size: 25
                pos_hint: {"center_x": 0.5, "top": 1}

            TextInput:
                id: spinner_job
                font_size: 20
                multiline: True  # set multiline to True
                size_hint_y: None
                height: max(self.minimum_height, 20)
                pos_hint: {"center_x": 0.5, "top": 0}
                on_text: root.spinner_3(self.text)

        Button:
            text: "Submit"
            font_size: 20
            size_hint_y: None
            size_hint_x: 0.3
            height: "40dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_press: root.get_recommendation()

"""
)

sm = ScreenManager()


class QuestionScreen(Screen):
    value1 = ""
    value2 = ""
    value3 = ""
    value4 = ""

    def spinner_1(self, value1):
        self.value1 = value1
        self.ids.spinner_name.text = f"{value1}"

    def spinner_2(self, value2):
        self.value2 = value2
        self.ids.spinner_gender.text = f"{value2}"

    def spinner_4(self, value4):
        self.value4 = value4
        self.ids.spinner_medeni.text = f"{value4}"

    def spinner_3(self, value3):
        self.value3 = value3
        self.ids.spinner_job.text = f"{value3}"

    def get_recommendation(self):
        file_path = "user_data.txt"
        with open(file_path, "a") as f:
            f.write(f"Adı: {self.value1}\n")
            f.write(f"Cinsiyeti: {self.value2}\n")
            f.write(f"Medeni Hali: {self.value4}\n")
            f.write(f"Mesleği: {self.value3}\n")
        self.clear_form()
        label = Label(text="Kaydedildi!", color=(0, 0, 0), font_size=30)
        self.add_widget(label)
        Clock.schedule_once(lambda dt: self.remove_widget(label), 1)

    def clear_form(self):
        self.ids.spinner_name.text = ""
        self.ids.spinner_gender.text = "Cinsiyet"
        self.ids.spinner_medeni.text = "Medeni Hal"
        self.ids.spinner_job.text = ""


sm.add_widget(QuestionScreen(name="question"))


class RecommendationApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    RecommendationApp().run()
