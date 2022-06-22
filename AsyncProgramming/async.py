import asyncio
import aiosmtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

your_email = "tankmansodari.073@kathford.edu.np"
email_to = "tankamansodari7@gmail.com"
password = "sseccus@tankmans"
subject = "Ekbana Temperature Report"
text = """\
    Hi,
    Your device temperature is getting Down.do something"""


MAIL_PARAMS = {'TLS': True, 'host': 'smtp.gmail.com',
               'password': password, 'user': your_email, 'port': 587}


class AsyncEmail():
    async def send_mail_async(sender, to, subject, text, textType='plain', **params):

        # Default Parameters
        cc = params.get("cc", [])
        bcc = params.get("bcc", [])
        mail_params = params.get("mail_params", MAIL_PARAMS)

        # Prepare Message
        msg = MIMEMultipart()
        msg.preamble = subject
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ', '.join(to)
        if len(cc):
            msg['Cc'] = ', '.join(cc)
        if len(bcc):
            msg['Bcc'] = ', '.join(bcc)

        msg.attach(MIMEText(text, textType, 'utf-8'))

        # Contact SMTP server and send Message
        host = mail_params.get('host', 'localhost')
        isSSL = mail_params.get('SSL', False)
        isTLS = mail_params.get('TLS', False)
        port = mail_params.get('port', 465 if isSSL else 25)
        smtp = aiosmtplib.SMTP(hostname=host, port=port, use_tls=isSSL)
        await smtp.connect()
        if isTLS:
            await smtp.starttls()
        if 'user' in mail_params:
            await smtp.login(mail_params['user'], mail_params['password'])

        await smtp.send_message(msg)
        await smtp.quit()

    def hello():
        print("hello world")


co1 = AsyncEmail.send_mail_async(your_email,
                                 [email_to],
                                 subject,
                                 text,
                                 textType="plain")
AsyncEmail.hello()
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(co1))
loop.close()
