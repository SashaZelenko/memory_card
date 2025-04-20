#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('В какой стране было открытие олимпиады в 2024 году?', "Во Франции", "В Германии", "В России", "В Греции"))
question_list.append(Question('Какой сейчас год?', "2024", "2025", "2030", "2070"))
question_list.append(Question('Какого врямя года не сушествует?', "зималь", "зима", "лето", "осень"))
question_list.append(Question('Сколько месяцев в году?', "12", "13", "14", "15"))
question_list.append(Question('Кто из них не футболист?', "Стефен Карри", "Лионель Месси", "Криштиану Роналду", "Златан Ибрагимович"))
question_list.append(Question('Какой город сталица России?', "Москва", "Санкт-Питербург", "Тюмень", "Челябинск"))
question_list.append(Question('Сколько лет Дубровскому старшему из романа Дубровсий?', "там не назван точнай возрост", "53", "64", "70"))
question_list.append(Question('Какой фильм ужасов самый страшный?', "Ужасаюший 3", "Оно", "Домовой", "Опасные воды"))
#question_list.append(Question('Скоко месяцев в году?', "12", "13", "14", "15"))
#question_list.append(Question('Скоко месяцев в году?', "12", "13", "14", "15"))
#question_list.append(Question('Скоко месяцев в году?', "12", "13", "14", "15"))
#question_list.append(Question('Скоко месяцев в году?', "12", "13", "14", "15"))
#question_list.append(Question('Скоко месяцев в году?', "12", "13", "14", "15"))
#question_list.append(Question('Скоко месяцев в году?', "12", "13", "14", "15"))
#question_list.append(Question('Скоко месяцев в году?', "12", "13", "14", "15"))

app = QApplication([]) #Приложение
window = QWidget()#Окно
window.setWindowTitle('Memory Card')#Сделать имя для окна
text = QLabel('Какой национальности не сушествует?')
window.move(900, 70)#Сдвиг экрана
window.resize(400, 200)#Размер экрана

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чульмцы')
rbtn_4 = QRadioButton('Алеуты')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)
button = QPushButton('Ответить')

AnsGroupBox = QGroupBox('Результат теста')

AnsGroupBox.hide()
result = QLabel('правильно/неправильно')
itog = QLabel('тут будет правельный ответ')

layout_res = QVBoxLayout()
layout_res.addWidget(result)
layout_res.addWidget(itog)
AnsGroupBox.setLayout(layout_res)


line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 =QHBoxLayout()

line1.addWidget(text, alignment = (Qt.AlignCenter | Qt.AlignVCenter))
line2.addWidget(RadioGroupBox)
line2.addWidget(AnsGroupBox)
line3.addWidget(button, alignment = (Qt.AlignCenter | Qt.AlignVCenter))
glav = QVBoxLayout()
glav.addLayout(line1)
glav.addLayout(line2)
glav.addLayout(line3)
window.setLayout(glav)

# RadioGroupBox.hide() #времено прячем варианты ответа
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button.setText('Следуший вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q: Question):
    shuffle(answers)#метод перемешивания списка из кнопок
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    text.setText(q.question) #вопрос
    itog.setText(q.right_answer) #
    show_question() #функция с панелью

def show_correct(res):
    result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правельно!')
        window.score += 1
        print('Статистика: \n Всего вопросов: ', window.total, '\n Правельных ответов: ', window.score)
        print('Рейтинг: ', (window.score/window.total * 100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг: ', (window.score/window.total * 100), '%')
q = Question('В каком месяце 28 дней?', "во всех", "в марте", "в июле", "в феврале")


def next_question():
    window.total += 1
    window.cur_question +=1 #переход к следушему вопросу
    if window.cur_question >= len(question_list):
        window.cur_question = 0 #обнуляем счётчик
    q = question_list[window.cur_question]
    ask(q) #cпросили

def click_ок():
    if button.text()=='Ответить':
        check_answer()
    else:
        next_question()

button.clicked.connect(click_ок)
window.score = 0
window.total = 0
window.cur_question = -1
next_question()
window.show()
app.exec()