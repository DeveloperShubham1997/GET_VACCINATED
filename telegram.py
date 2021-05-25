import requests

def toTelegram(msg):
	token = "" #your telegram token
	chatID = "" #your group id
	textToSend = msg
	telegramURL= "https://api.telegram.org/bot"
	temp=telegramURL+token+"/sendMessage?chat_id="+chatID+"&text="+textToSend
	requests.get(temp)


