import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import config
import pandas as pd


def get_receivers():
    df = pd.read_excel('mail.xlsx')
    return list(df['email'])


def main(receivers):
    smtpObj = smtplib.SMTP('smtp.mail.ru', 587)
    smtpObj.starttls()

    smtpObj.login(config.SENDER, 'Ncp3iry4fd6p7EeeWa77')
    i = 0
    for re in receivers:
        i += 1
        print(i)
        try:
            msg = MIMEMultipart()
            msg.set_charset('utf-8')
            msg['From'] = config.SENDER_NAME
            msg['Subject'] = 'Ссылка на трансляцию'
            msg['To'] = re
            # Если нужна рассылка html
            with open('letter.html', 'r') as file:
                html = file.read()
                body = MIMEText(html, 'html')
                msg.attach(body)
            # Если нужна рассылка текста
            # body = MIMEText("Добрый день. Вы получили это письмо, т.к. проходили регистрацию на онлайн-участие в круглом столе «О блокаде. Говорим с детьми».\n"
            #         "Трансляция будет поделена на две части — \n"
            #         "Часть I: https://youtube.com/live/4JJmqdw7Jbw?feature=share \n"
            #         "Часть II: https://youtube.com/live/lCH-XWpTJVg?feature=share \n"
            #         "Если во время трансляции что-то пошло не так, заново перейдите по ссылке или перезагрузите страницу. \n\n"
            #         "С уважением,\n"
            #         "библиотека СВОя", 'plain', 'utf-8')

            msg.attach(body)

            smtpObj.sendmail(config.SENDER_NAME, [re], msg.as_string())
            with open('success1.txt', 'a') as success_file:
                success_file.write(re + '\n')
        except Exception:
            with open('not_sended.txt', 'a') as not_sended_file:
                not_sended_file.write(re + '\n')
    print("Successfully sent email")
    smtpObj.quit()


if __name__ == '__main__':
    # main(['st077009@student.spbu.ru', 'svsha.ivanova@dsahejkl12jk'])

    main(get_receivers())
