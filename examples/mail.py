import imaplib

email = "blidohuset@gmail.com"
passw = "koppen123"
imapserver = "imap.gmail.com"

def delete_Unseen_Emails_and_get_user(user, password, IMAP):
    mail = imaplib.IMAP4_SSL(IMAP)
    mail.login(user, password)
    mail.select("inbox")
    typ, data = mail.search(None, 'UNSEEN')
    # ids = data[0]
    # id_list = ids.split()
    # latest_email_id = int( id_list[-1] )
    # for i in range( latest_email_id, latest_email_id-15, -1 ):
    # data = mail.fetch( i, '(RFC822)' )

    # for response_part in data:
    #   if isinstance(response_part, tuple):
    #       msg = email.message_from_string(response_part[1])
    #       varSubject = msg['subject']
    #       varFrom = msg['from']

    # #remove the brackets around the sender email address
    # varFrom = varFrom.replace('<', '')
    # varFrom = varFrom.replace('>', '')

    # #add ellipsis (...) if subject length is greater than 35 characters
    # if len( varSubject ) > 35:
    #       varSubject = varSubject[0:32] + '...'

    # print('[' + varFrom.split()[-1] + '] ' + varSubject)
    
    for num in data[0].split():
        mail.store(num, '+FLAGS', r'(\Deleted)')
    mail.expunge()
    mail.close()
    mail.logout()

def check_messages(email,passw):
    mail = imaplib.IMAP4_SSL(imapserver)
    mail.login(email, passw)
    mail.select("inbox")
    typ, data = mail.search(None, 'UNSEEN')
    if len(data[0].split()) > 0:
        mail.expunge()
        mail.close()
        mail.logout()
        delete_Unseen_Emails_and_get_user(email, passw, imapserver)
check_messages(email,passw)
