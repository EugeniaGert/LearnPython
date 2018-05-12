def get_answer(question):
    answers = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
    return answers.get(question.lower(), ':-)')


def get_answer_2(question, answers_dict):
    return answers_dict.get(question.lower())


def get_answer_3(question):
    answers1 = {"привет": "И тебе привет!", "пока": "Увидимся"}
    answers2 = {"как дела": "Лучше всех"}
    dialogs = [answers1, answers2]

    for dialog1 in dialogs:
        answer1 = get_answer_2(question, dialog1)
        if answer1 is not None:
            return answer1
    return 'ответа нет'


print(get_answer_3('как дела'))
print(get_answer_3('нет вопросов'))

