import datetime
import calendar

def get_calendar():
	date = datetime.datetime.now() # Hozirgi aniq vaqt va sanani olish uchun
	day = date.day # bugungi aniq kunni oladi
	year = date.year # ylini qaytaradi
	month = date.month # oyni qaytaradi
	print('Today>>>',day,'\n',calendar.month(year,month)) #natija 
get_calendar()