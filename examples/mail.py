import imaplib
import email

emailaddress = "blidohuset@gmail.com"
passw = "koppen123"
imapserver = "imap.gmail.com"

def delete_Unseen_Emails_and_get_user(user, password, IMAP):
    mail = imaplib.IMAP4_SSL(IMAP)
    mail.login(user, password)
    mail.select("inbox")
    typ, data = mail.search(None, 'ALL')
    ids = data[0] # data is a list.
    id_list = ids.split() # ids is a space separated string
    latest_email_id = id_list[-1] # get the latest
 
    result, data = mail.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID
    print('Getting user')
    raw_email = data[0][1].decode('utf-8') # here's the body, which is raw text of the whole email
    # including headers and alternate payloads
    # print(raw_email)
    email_message = email.message_from_string(raw_email)
    sender = email.utils.parseaddr(email_message['From'])
    print(sender)
    # if isinstance(data, tuple):
    #     msg = email.message_from_string(data)
    #     varFrom = msg['from']
    # varFrom = varFrom.replace('<', '')
    # varFrom = varFrom.replace('>', '')
    # if len( varSubject ) > 35:
    #     varSubject = varSubject[0:32] + '...'
    # print(varSubject)
    # for response_part in data:
    #   if isinstance(response_part, tuple):
    #       msg = email.message_from_string(response_part[1])s
    #       varSubject = msg['subject']
    #       varFrom = msg['from']

    # #remove the brackets around the sender email address
    # varFrom = varFrom.replace('<', '')
    # varFrom = varFrom.replace('>', '')

    # #add ellipsis (...) if subject length is greater than 35 characters
    # if len( varSubject ) > 35:
    #       varSubject = varSubject[0:32] + '...'

    # print('[' + varFrom.split()[-1] + '] ' + varSubject)
    
    # for num in data[0].split():
    mail.store(latest_email_id, '+FLAGS', r'(\Deleted)')
    mail.expunge()
    mail.close()
    mail.logout()

def check_messages(emailaddress,passw):
    mail = imaplib.IMAP4_SSL(imapserver)
    mail.login(emailaddress, passw)
    mail.select("inbox")
    typ, data = mail.search(None, 'ALL')
    unseen_messages = len(data[0].split())
    print(unseen_messages)
    if  unseen_messages > 0:
        mail.expunge()
        mail.close()
        mail.logout()
        delete_Unseen_Emails_and_get_user(emailaddress, passw, imapserver)
print('Trying')
check_messages(emailaddress,passw)
