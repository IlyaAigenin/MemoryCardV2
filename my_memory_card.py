from PyQt5.QtCore import Qt                                             #Импорт библиотеки
from PyQt5.QtWidgets import (                                           #Импорт доп. библиотеки из библиоткеи
        QApplication, QWidget,                                          #Список:
        QHBoxLayout, QVBoxLayout,                                       #                           
        QGroupBox, QButtonGroup, QRadioButton,                          #  
        QPushButton, QLabel)                                            #
from random import shuffle                                              #Импорт рандомного перепешивания (для вопросов)
 
class Question():                                                       #Создание класса
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3): #Создание вопроса, правильного ответа, и 3х неправильных.
        self.question = question                                        #Приравнивание вопроса к вопросу (?)
        self.right_answer = right_answer                                #Приравнивание правильного ответа к правильному (?)
        self.wrong1 = wrong1                                            #Приравнивание неправильного вопроса к неправильному (?)
        self.wrong2 = wrong2                                            #Приравнивание неправильного вопроса 2 к неправильному 2 (?)
        self.wrong3 = wrong3                                            #Приравнивание неправильного вопроса 3 к неправильному 3 (?)

                            #Этот спискок стоит соблюдать, при создании листов
 
questions_list = []                                                     #Создание самих вопросов.
questions_list.append(Question('Какая самая новая модель смартфона Samsung?', 'Galaxy S22 Ultra', 'Galaxy A53 5G', 'Galaxy Tab S8', 'Galaxy S20 FE')) #Вопрос, и его комплектуещее
questions_list.append(Question('Какой порт является рабочим в Minecraft для многих провайдеров?', '25565', '25575', '19922', '20044')) #Вопрос 2, и его комплектуещее
questions_list.append(Question('В каком месяце был основан VelRest?', 'Апрель', 'Март', 'Февраль', 'Нет правильного ответа'))
questions_list.append(Question('Какой домен у сервера VelRest?', '.ru', '.su', '.net', '.com'))
questions_list.append(Question('В каком месяце был полный выпус режима "GRIEF"?', 'Июнь', 'Май', 'Апрель', 'Июль'))
questions_list.append(Question('В каком месяце был полный выпус режима "ANARHY"?', 'Июль', 'Май', 'Апрель', 'Июнь'))
questions_list.append(Question('Какое ядро стоит на прокси VelRest?', 'BungeeCord+BotFilter', 'Velocity', 'BungeeCord', 'Velocity+BotFilter'))
questions_list.append(Question('Какой плагин был удалён на анархии VelRest по причине бага?', '3x3 pickaxe (кирка)', 'LiteBans (баны)', 'EssentialsX (команды и т.д.)', 'ServerList (лист)'))
questions_list.append(Question('Какой был рекордный онлайн на сервере VelRest?', '16', '25', '51', '40')) #Вопрос 3, и его комплектуещее

app = QApplication([])                                                  #Создание кнопок и текста вопроса.
 
btn_OK = QPushButton('| Ответить')                                      #Создание кнопки ответа
lb_Question = QLabel('Вопрос.')                                         #Текст вопроса
 
RadioGroupBox = QGroupBox("Варианты ответов")                           #Возможность переход между ответами в вопросе.
 
rbtn_1 = QRadioButton('Вариант 1')                                      #Создание кнопки первого ответа
rbtn_2 = QRadioButton('Вариант 2')                                      #Создание кнопки второго ответа
rbtn_3 = QRadioButton('Вариант 3')                                      #Создание кнопки третьего ответа
rbtn_4 = QRadioButton('Вариант 4')                                      #Создание кнопки четвёртого ответа
 
RadioGroup = QButtonGroup()                                             #Группировка переключателей, чтобы управлять ими.
RadioGroup.addButton(rbtn_1)                                            #1-ый переключатель
RadioGroup.addButton(rbtn_2)                                            #2-ой переключатель
RadioGroup.addButton(rbtn_3)                                            #3-ий переключатель
RadioGroup.addButton(rbtn_4)                                            #4-ый переключатель
 
layout_ans1 = QHBoxLayout()                                             #Горизонтальные ответы будут внутри вертикали (?)
layout_ans2 = QVBoxLayout()                                             #Вертикальные ответы будут внутри горизонтали (?)
layout_ans3 = QVBoxLayout()                                             #Вертикальные ответы будут внутри горизонтали (?)
layout_ans2.addWidget(rbtn_1)                                           #Два ответа в 1-ый столбец [1 отв.]
layout_ans2.addWidget(rbtn_2)                                           #Два ответа в 1-ый столбец [2 отв.]
layout_ans3.addWidget(rbtn_3)                                           #Два ответа в 2-ой столбец [1 отв.]
layout_ans3.addWidget(rbtn_4)                                           #Два ответа в 2-ой столбец [2 отв.]
 
layout_ans1.addLayout(layout_ans2)                                      #Размещение стобов в одной строке
layout_ans1.addLayout(layout_ans3)                                      #Размещение стобов в одной строке
 
RadioGroupBox.setLayout(layout_ans1)                                    #Меню с ответами
 
AnsGroupBox = QGroupBox("Результат теста")                              #Вывод текста после ответа
lb_Result = QLabel('прав ты или нет')                                   #Показ результата [Правильно, али - нет]
lb_Correct = QLabel('ответ будет тут!')                                 #Показ результата [Правильный ответ]
 
layout_res = QVBoxLayout()                                              #Вертикальные ответы будут внутри горизонтали (?)
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop)) #Создание виджета результата (?)
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)  #Создание виджета с правильным ответом (?)
AnsGroupBox.setLayout(layout_res)                                       #Результат (?)
 
layout_line1 = QHBoxLayout()                                            #Вопрос теста
layout_line2 = QHBoxLayout()                                            #Варианты ответа, или результат теста.
layout_line3 = QHBoxLayout()                                            #Создание кнопки: "Ответить"
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide()                                                      #Скрытие панели с ответом, сначала должна быть видна панель вопросов
 
layout_line3.addStretch(1)                                              #Размер
layout_line3.addWidget(btn_OK, stretch=2)                               #Увеличение размера кнопки
layout_line3.addStretch(1)                                              #Размер
 
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)                         
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)                                               #Пробел между содержимым
 
def show_result():
    RadioGroupBox.hide()                                                #Панель ответов
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')                                  #Переход на след. вопрос
 
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    #Сброс Выбранной кнопки
    RadioGroup.setExclusive(False)                                      #Снятие ограничения, чтобы можно было сбросить кнопку
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)                                       #Возвращение ограничения, теперь только одна кнопка может быть выбрана
 
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
 
def ask(q: Question):
    ''' функция записывает значения вопроса и ответов в соответствующие виджеты, 
    при этом варианты ответов распределяются случайным образом'''
    shuffle(answers) # перемешали список из кнопок, теперь на первом месте списка какая-то непредсказуемая кнопка
    answers[0].setText(q.right_answer) # первый элемент списка заполним правильным ответом, остальные - неверными
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question) # вопрос
    lb_Correct.setText(q.right_answer) # ответ 
    show_question() # показываем панель вопросов 
 
def show_correct(res):
    ''' показать результат - установим переданный текст в надпись результат и покажем нужную панель '''
    lb_Result.setText(res)
    show_result()
 
def check_answer():
    ''' если выбран какой-то вариант ответа, то надо проверить и показать панель ответов'''
    if answers[0].isChecked():
        # правильный ответ!
        show_correct('Правильно!')
        window.score = window.score + 1
        window.total += 1
        print('| Кол-во вопросов: ', window.total)
        print('| Кол-во правильных ответов: ', window.score)
        print('| Рейтинг:', (window.score / window.total * 100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            # неправильный ответ!
            show_correct('Неверно!')
            window.total += 1
            print('| Кол-во вопросов: ', window.total)
            print('| Кол-во правильных ответов: ', window.score)
            print('| Рейт:', (window.score / window.total * 100), '%')
 
def next_question():
    #задает следующий вопрос из списка
    # этой функции нужна переменная, в которой будет указываться номер текущего вопроса
    # эту переменную можно сделать глобальной, либо же сделать свойством глобального объекта (app или window)
    # мы заведем (ниже) свойство window.cur_question.
    window.cur_question = window.cur_question + 1 # переходим к следующему вопросу
    if window.cur_question >= len(questions_list):
        window.cur_question = 0 # если список вопросов закончился - идем сначала
    q = questions_list[window.cur_question] # взяли вопрос                  
    ask(q) # спросили
 
def click_OK():
    ''' определяет, надо ли показывать другой вопрос либо проверить ответ на этот '''
    if btn_OK.text() == 'Ответить':
        check_answer() # проверка ответа
    else:
        next_question() # следующий вопрос

 
window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('MC. Upgrade by: Molda1n, TEREHUSHA')
# текущий вопрос из списка сделаем свойством объекта окно, так мы сможем спокойно менять его из функции
window.cur_question = -1    # по-хорошему такие переменные должны быть свойствами, 
                            # только надо писать класс, экземпляры которого получат такие свойства, 
                            # но python позволяет создать свойство у отдельно взятого экземпляра
 
btn_OK.clicked.connect(click_OK) # по нажатии на кнопку выбираем, что конкретно происходит
 
# все настроено, осталось задать вопрос и показать окно

window.score = 0
window.total = 0

next_question()
window.resize(700, 400)
window.show()
app.exec()