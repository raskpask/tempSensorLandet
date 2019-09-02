import imaplib, smtplib
import email
from requests.exceptions import ConnectionError

class Mail_Handler:
    
    def __init__(self):
        self.emailaddress = "blidohuset@gmail.com"
        self.passw = "koppen123"
        self.imapserver = "imap.gmail.com"

    def delete_Unseen_Emails_and_get_user(self, user, password, IMAP):
        try:
            mail = imaplib.IMAP4_SSL(IMAP)
            mail.login(user, password)
            mail.select("inbox")
            _, data = mail.search(None, 'ALL')
            ids = data[0] # data is a list.
            id_list = ids.split() # ids is a space separated string
            latest_email_id = id_list[-1] # get the latest
 
            _, data = mail.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID
            raw_email = data[0][1].decode('utf-8') 
            email_message = email.message_from_string(raw_email)
            sender = email.utils.parseaddr(email_message['From'])
            subject = email_message['Subject']
            mail.store(latest_email_id, '+FLAGS', r'(\Deleted)')
            mail.expunge()
            mail.close()
            mail.logout()
        except ConnectionError as e:
            print(e)    
            return sender[1],subject

    def check_messages(self, emailaddress,passw):
        try:
            mail = imaplib.IMAP4_SSL(self.imapserver)
            mail.login(emailaddress, passw)
            mail.select("inbox")
            _, data = mail.search(None, 'ALL')
            unseen_messages = len(data[0].split())
        except ConnectionError as e:
            print(e)
            if  unseen_messages > 0:
                mail.expunge()
                mail.close()
                mail.logout()
                return self.delete_Unseen_Emails_and_get_user(self.emailaddress, self.passw, self.imapserver)
            else:
                return 0 , "Error no mail found"


    def send_message(self,recipient,subject,text):
        FROM = self.emailaddress
        TO = recipient if isinstance(recipient, list) else [recipient]
        SUBJECT = subject 
        TEXT = text 
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
        try:
            server = smtplib.SMTP_SSL("smtp.gmail.com")
            server.login(self.emailaddress, self.passw)
            server.sendmail(FROM, TO, message)
            server.close()
        except:
            print("failed to send mail")
