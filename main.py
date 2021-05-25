from cowin import find_vaccine
from telegram import toTelegram
import time
import datetime

if __name__ == '__main__':
	district_id="314" #314 for indore
	date="26-05-2021"
	while True:
		find_vaccine(district_id,date)
		print(datetime.datetime.now())
		time.sleep(4)


		