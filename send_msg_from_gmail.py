import smtplib

def send_mail():

    with smtplib.SMTP('smtp.gmail.com' , 587) as smtp:

        smtp.ehlo()

        smtp.starttls()

        smtp.ehlo()

        smtp.login('your email' , 'email password')

        subject = 'subject of msg'
        body = 'the msg'

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail('Your Email' , 'Email You Want To Send The msg' , msg )

send_mail()