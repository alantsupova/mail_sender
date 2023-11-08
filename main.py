import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import config

def main():
    msg = MIMEMultipart()
    msg.set_charset('utf-8')

    msg['From'] = config.SENDER_NAME
    msg['To'] = ', '.join(config.RECEIVERS)
    msg['Subject'] = config.MAIL_THEME

    with open('letter.html', 'r') as file:
        html = file.read()
        body = MIMEText(html, 'html')
        msg.attach(body)

    smtpObj = smtplib.SMTP('smtp.yandex.ru', 587)
    smtpObj.starttls()

    smtpObj.login(config.SENDER, 'p23LRvst')
    smtpObj.sendmail(config.SENDER_NAME, config.RECEIVERS, msg.as_string())
    print("Successfully sent email")
    smtpObj.quit()

if __name__ == '__main__':
    main()
