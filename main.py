import smtplib
from email.mime.text import MIMEText
import config


def main():
    with open('letter.html', 'r') as file:
        html = file.read()

    msg = MIMEText(html, 'html')

    msg['Subject'] = config.MAIL_THEME
    smtpObj = smtplib.SMTP('smtp.yandex.ru', 587)
    smtpObj.starttls()

    smtpObj.login(config.SENDER, 'p23LRvst')
    smtpObj.sendmail(config.SENDER_NAME, config.RECEIVERS, msg.as_string())
    print("Successfully sent email")
    smtpObj.quit()


if __name__ == '__main__':
    main()
