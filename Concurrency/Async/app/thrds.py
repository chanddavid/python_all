import aiosmtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dataclasses import dataclass

@dataclass
class AsyncEmails: 
    your_email:str
    email_to:str
    password:str
    subject:str
    text:str
    textType:str 
    port:int
  
    async def send_mail_async(self, **params):
        MAIL_PARAMS = {'TLS': True, 'host': 'smtp.gmail.com',
                    'password': self.password, 'user': self.your_email, 'port': self.port}
        mail_params = params.get("mail_params", MAIL_PARAMS)

        # Prepare Message
        msg = MIMEMultipart()
        msg.preamble = self.subject
        msg['Subject'] = self.subject
        msg['From'] = self.your_email
        msg['To'] = ', '.join(self.email_to)
        msg.attach(MIMEText(self.text, self.textType, 'utf-8'))

        # Contact SMTP server and send Message
        host = mail_params.get('host', 'localhost')
        isSSL = mail_params.get('SSL', False)
        isTLS = mail_params.get('TLS', False)
        port = mail_params.get('port', 465 if isSSL else 25)
        smtp = aiosmtplib.SMTP(hostname=host, port=port, use_tls=isSSL)
        await smtp.connect()    
        if isTLS:
            await smtp.starttls()
            print("first")
        if 'user' in mail_params:
            await smtp.login(mail_params['user'], mail_params['password'])
            print("second")

        await smtp.send_message(msg)
        print("third")
        await smtp.quit()
        print("forth")
    

