# Install Courier SDK: pip install trycourier
from trycourier import Courier

client = Courier(auth_token="pk_prod_25DJ5KZ8TYMYHCHX5HXBN0G5R0XG")

class Contacts:

  def __init__(self, name, email, msg):
    self.__name = name
    self.__email = email
    self.__msg = msg
  
  def send_email(self):
    resp = client.send_message(
    message={
      "to": {
      "email": 'Philip1805061@miuegypt.edu.eg'
    },
      "content": {
      "title": "Auto Correction Website",
      "body": '''
      Dear Philip,\n
      There is an inquiry from {}\nEmail: {}\nMessage: {}
      '''
      .format(self.__name, self.__email, self.__msg)

    },
  }  
)
    print("Response = ", resp)






