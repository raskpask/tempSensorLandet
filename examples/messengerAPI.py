from itertools import islice
from fbchat import Client
from fbchat.models import *



class MessengerHandler():
    def __init__(self):  
        self.client = Client("blidohuset@gmail.com", "koppen123")
        print("Own id: {}".format(self.client.uid))

    def sendMessage(self,userID,message):
        self.client.send(Message(text=message), thread_id=userID, thread_type=ThreadType.USER)

    def logout(self):
        self.client.logout()

    def getUsers(self):
        self.users = self.client.fetchAllUsers()
        # print("users' IDs: {}".format([user.uid for user in self.users]))
        userIDs =[]
        for user in self.users:
            userIDs.append(user.uid)
        return userIDs    
    
    def sendWarning(self,userIDs,warningMessage):
        for userID in userIDs:
            self.sendMessage(userID,warningMessage)

    def fetchMessage(self,userIDs):
        for userID in userIDs:
            messages = self.client.fetchThreadMessages(thread_id=userID, limit=1)
            for message in messages:
                command ={
                    'info': "sendInfo",
                    'restart': "restartDevice",
                    'warningON': "warningON",
                    'warningOFF': "warningOFF"
                    # Could send start functions instead like 'off': off
                }
                print(command.get(message.text))


        
msgH = MessengerHandler()
userIDs = msgH.getUsers()
# msgH.sendWarning(userIDs,"The temp is too low")
msgH.fetchMessage(userIDs)
msgH.logout()

