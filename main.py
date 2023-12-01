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

    smtpObj.login(config.SENDER, 'xebjzzLUNbzQgT7v9yCB')
    i = 0
    for re in receivers:
        i += 1
        print(i)
        try:
            msg = MIMEMultipart()
            msg.set_charset('utf-8')
            msg['From'] = config.SENDER_NAME
            msg['Subject'] = config.MAIL_THEME
            msg['To'] = re
            with open('letter.html', 'r') as file:
                html = file.read()
                body = MIMEText(html, 'html')
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
