def send_email(message,recipient,*, sender = "university.help@gmail.ru"):
    okonch = (".ru",".com",".net")
    if sender.endswith(okonch) and recipient.endswith(okonch) and "@" in recipient and sender:
        if sender == recipient:
            print("Невозможно отправить письмо самому себе")
        elif sender != "university.help@gmail.ru":
            print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отпарвлено с адреса ", sender, "на адрес ", recipient)
        else:
            print("Письмо успешно отправлено с адреса ", sender,  "на адрес", recipient)
    else:
         print("Невозможно отправить письмо с адреса ", sender, "на адрес ", recipient)

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.fan@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
