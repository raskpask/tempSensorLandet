import imaplib
import email

class Mail_Handler:
    
    def __init__(self):
        self.emailaddress = "blidohuset@gmail.com"
        self.passw = "koppen123"
        self.imapserver = "imap.gmail.com"
    def delete_Unseen_Emails_and_get_user(self, user, password, IMAP):
        mail = imaplib.IMAP4_SSL(IMAP)
        mail.login(user, password)
        mail.select("inbox")
        typ, data = mail.search(None, 'ALL')
        ids = data[0] # data is a list.
        id_list = ids.split() # ids is a space separated string
        latest_email_id = id_list[-1] # get the latest
 
        result, data = mail.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID
        raw_email = data[0][1].decode('utf-8') 
        email_message = email.message_from_string(raw_email)
        sender = email.utils.parseaddr(email_message['From'])
        mail.store(latest_email_id, '+FLAGS', r'(\Deleted)')
        mail.expunge()
        mail.close()
        mail.logout()
        return sender[1]

    def check_messages(self, emailaddress,passw):
        mail = imaplib.IMAP4_SSL(self.imapserver)
        mail.login(emailaddress, passw)
        mail.select("inbox")
        sender = ''
        typ, data = mail.search(None, 'ALL')
        unseen_messages = len(data[0].split())
        if  unseen_messages > 0:
            print('Getting user')
            mail.expunge()
            mail.close()
            mail.logout()
            sender = self.delete_Unseen_Emails_and_get_user(self.emailaddress, self.passw, self.imapserver)
            return sender
        else:
            return 0
