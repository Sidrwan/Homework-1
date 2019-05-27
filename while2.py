answer_question = {
    "Как дела?": "Хорошо", "Что делаешь?": "Программирую ",
    "А что потом?": "Спать", "Завтра какие планы?": "Программировать и спать!"
    }

def asc_user():
    while True:
        question = input("Ваш вопрос:")
        if question in answer_question:
            print(answer_question.get(question))

        else:
            print("Может еще попробуешь?")

asc_user()