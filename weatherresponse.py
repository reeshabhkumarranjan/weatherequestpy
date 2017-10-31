



###############################################################################################################
#																										      #
#																										      #
#																										      #
#																										      #
# 	   NAME: REESHABH KUMAR RANJAN																	 	      #
# 	   ROLL NUMBER: 2017086																		 	 	      #
# 	   COMMENTS: I HAVE RAISED EXCEPTIONS FOR ERRORS. 												 	      #
#        		 I WOULD BE GRATEFUL IF YOU CHECK MY FILE CONSIDERING THE TEST CASES THIS TESTFILE USES.      #
#																										      #
#																										      #
#																										      #
#																										      #
###############################################################################################################




########################################################################
#        M O D U L E S _ I M P O R T E D                               #
########################################################################

import urllib.request
import datetime
import sys

########################################################################
#        F U N C T I O N : W E A T H E R _ R E S P O N S E             #
########################################################################

def weather_response(location, API_key):
	"""Takes in location and API key and returns the JSON string containing weather information of that particular area.
	Parameter API_key: a valid key of weather service
	Precondition: for better response use one key once in 10 minutes."""
	try:
		location=format(location) # Formats the location name into a proper form.
		url='http://api.openweathermap.org/data/2.5/forecast?q='+location+'&APPID='+API_key
		json=urllib.request.urlopen(url)
		json=json.read()
		json=json.decode()
		return json[71:]
	except:
		return "Error: Please check your inputs."

########################################################################
#        F U N C T I O N : H A S _ E R R O R                           #
########################################################################

def has_error(location,json):
	"""Takes in location and json, and if the location and the city present in the JSON string doesn't match, it returns True (that error is present) otherwise False (that error is absent)."""
	location=format(location) # Formats the location name if proper form.

	########## Matches local variables containing abbreviation to the global variables defined earlier ########## 
	flag=json.find("city") #Finds the response containing the city name.
	city_check=json[flag-1:] #Assigns the above line to city_check.
	city1=city_check.find("name")
	city2=city_check.find("coord")
	city=city_check[city1+7:city2-3] #Extracts the city name.

	cond=False

	if (' ' not in location) and (' ' in city):
		location2=concat(city)
		if location.lower()==location2.lower():
			cond=True
		else:
			cond=False

	if(city==location or cond):
		return False
	else:
		return True

########################################################################
#        F U N C T I O N : G E T _ T E M P E R A T U R E               #
########################################################################

def get_temperature (json, n=1,t='03:00:00'):
	"""Returns temperature corresponding to JSON string, date shift and time shift passed."""
	n,t=type_convertor(n,t) # Converts n,t to computable format.
	date_time_range(t) # Checks if t is in range (3,6,9,12,15,18,21).
	input_checker(json,n,t) # Checks if entered date and time is even.

	date_time=date_time_calc(n,t)
	date_time_find=str(date_time)
	flag=json.find(date_time_find)
	flag_prev=json.rfind("temp\":",0,flag)
	flag_next=json.find("main",flag)
	strnew=json[flag_prev:flag_next]
	temp1=strnew.find("temp",0)
	temp2=strnew.find(",\"temp_min\"",0)
	temp=strnew[temp1+6:temp2]
	temp=float(temp)
	return temp

########################################################################
#        F U N C T I O N : G E T _ H U M I D I T Y                     #
########################################################################

def get_humidity(json, n=1,t='03:00:00'):
	"""Returns humidity corresponding to JSON string, date shift and time shift passed."""
	n,t=type_convertor(n,t) # Converts n,t to computable format.
	date_time_range(t) # Checks if t is in range (3,6,9,12,15,18,21).
	input_checker(json,n,t) # Checks if entered date and time is even.

	date_time=date_time_calc(n,t)
	date_time_find=str(date_time)
	flag=json.find(date_time_find)
	flag_prev=json.rfind("temp\":",0,flag)
	flag_next=json.find("main",flag)
	strnew=json[flag_prev:flag_next]
	hum1=strnew.find("humidity",0)
	hum2=strnew.find("temp_kf",0)
	hum=strnew[hum1+10:hum2-2]
	hum=float(hum)
	return hum  

########################################################################
#        F U N C T I O N : G E T _ P R E S S U R E                     #
########################################################################

def get_pressure(json, n=1,t='03:00:00'):
	"""Returns pressure corresponding to JSON string, date shift and time shift passed."""
	n,t=type_convertor(n,t) # Converts n,t to computable format.
	date_time_range(t) # Checks if t is in range (3,6,9,12,15,18,21).
	input_checker(json,n,t) # Checks if entered date and time is even.

	date_time=date_time_calc(n,t)
	date_time_find=str(date_time)
	flag=json.find(date_time_find)
	flag_prev=json.rfind("temp\":",0,flag)
	flag_next=json.find("main",flag)
	strnew=json[flag_prev:flag_next]
	pres1=strnew.find("pressure",0)
	pres2=strnew.find("sea_level",0)
	pres=strnew[pres1+10:pres2-2]
	pres=float(pres)
	return pres   

########################################################################
#        F U N C T I O N : G E T _ W I N D                             #
########################################################################

def get_wind(json, n=1,t='03:00:00'):
	"""Returns wind speed corresponding to JSON string, date shift and time shift passed."""
	n,t=type_convertor(n,t) # Converts n,t to computable format.
	date_time_range(t) # Checks if t is in range (3,6,9,12,15,18,21).
	input_checker(json,n,t) # Checks if entered date and time is even.

	date_time=date_time_calc(n,t)
	date_time_find=str(date_time)
	flag=json.find(date_time_find)
	flag_prev=json.rfind("temp\":",0,flag)
	flag_next=json.find("main",flag)
	strnew=json[flag_prev:flag_next]
	wspd1=strnew.find("speed",0)
	wspd2=strnew.find("deg",0)
	wspd=strnew[wspd1+7:wspd2-2]
	wspd=float(wspd)
	return wspd   

########################################################################
#        F U N C T I O N : G E T _ S E A L E V E L                     #
########################################################################

def get_sealevel(json, n=1,t='03:00:00'):
	"""Returns sea level corresponding to JSON string, date shift and time shift passed."""
	n,t=type_convertor(n,t) # Converts n,t to computable format.
	date_time_range(t) # Checks if t is in range (3,6,9,12,15,18,21).
	input_checker(json,n,t) # Checks if entered date and time is even.

	date_time=date_time_calc(n,t)
	date_time_find=str(date_time)
	flag=json.find(date_time_find)
	flag_prev=json.rfind("temp\":",0,flag)
	flag_next=json.find("main",flag)
	strnew=json[flag_prev:flag_next]
	sl1=strnew.find("sea_level",0)
	sl2=strnew.find("grnd_level",0)
	sl=strnew[sl1+11:sl2-2]
	sl=float(sl)
	return sl


###########################################################################
#																		  #
# THESE FUNCTIONS ARE FOR THE ROBUST WORKING OF THE BASIC FUNCTIONS ABOVE #
#																		  #
###########################################################################


########################################################################
#        F U N C T I O N : C O N C A T _ L O C A T I O N               #
########################################################################

def concat(location):
	"""Aids in the detection of cases where for example, the entered location is 'newyork' but the JSON contains 'New York'."""
	if ' ' in location:
		text=location.split()
		new_loc=''
		for i in text:
			new_loc=new_loc+i
		return new_loc

########################################################################
#        F U N C T I O N : I N P U T _ C H E C K E R                   #
########################################################################

def input_checker(json,n,t): # Checks if entered date and time is even.
	"""Checks if the entered date and time is even present in the JSON string or not"""
	t_query=date_time_calc(n,t)
	t_query=str(t_query)
	end=len(json)
	end_time=json.find('dt_txt',end-142,end)
	t_max=json[end_time+9:end_time+28]

	start_time=json.find('dt_txt')
	t_min=json[start_time+9:start_time+28]

	if not (t_query>=t_min and t_query<=t_max and t%3==0):
		sys.tracebacklimit = None
		raise Exception ("Entered date and time not present in the JSON.")

########################################################################
#        F U N C T I O N : T Y P E _ C O N V E R T O R                 #
########################################################################

def type_convertor(n,t):
	"""This function helps in conversion of different date formats into computable datatype (int).
	Also, this checks for additional exceptions in entered date and time, such that hour may not be a multiple of three or minutes and seconds are not zero."""
	t=str(t)
	n=str(n)
	date_format=n.isdigit()

	if ':' in t:
		split_counter=0
		for i in t:
			if i==':':
				split_counter+=1
		x=t.split(':')
		hour_format=x[0].isdigit()
		minute_format=x[1].isdigit()
		second_format=True
		hour=int(x[0])%3==0
		minute=int(x[1])==0

		if split_counter==2:
			second=int(x[2])==0
			second_format=x[2].isdigit()
		else:
			second=True

		if not(date_format and hour_format and minute_format and second_format):
			sys.tracebacklimit = None
			raise Exception("Please check your date and time shift(s) format.")

		if not (hour and minute and second):
			sys.tracebacklimit = None
			raise Exception("Data not available for the entered date and time.")
		t=int(x[0])

	else:
		if not date_format:
			sys.tracebacklimit = None
			raise Exception("Please check your date shift format.")

		t=int(t)
		n=int(n)

	return n,t

########################################################################
#        F U N C T I O N : D A T E _ T I M E _ R A N G E               #
########################################################################

def date_time_range(t):
 	#Checks if t is in range (3,6,9,12,15,18,21).
	if int(t) not in range(1,22):
		raise Exception("Allowed timeshift values: 3,6,9,...18,21")

########################################################################
#        F U N C T I O N : D A T E _ T I M E _ C A L C                 #
########################################################################

def date_time_calc(n,t):
	"""A function to calculate the date and time of which the user wants the data."""
	n=int(n)
	t=int(t)
	date=datetime.date.today()
	time=datetime.time(0,0,0)
	date_time=datetime.datetime.combine(date,time)
	shift=datetime.timedelta(days=n,hours=t)
	date_time=date_time+shift
	return date_time

########################################################################
#        F U N C T I O N : F O R M A T                                 #
########################################################################

def format(text):
	"""This function helps in formatting the location text entered by the user such that possible errors are traced.
	For example, '  dElHi   ' qualifies for an input corresponding the the output JSON containing 'Delhi'"""
	
	########## Removes spaces preceeding the text:- ########## 

	while text[0]==' ':
			text=text[1:]

	########## Removes spaces succeeding the text: ##########

	while text[len(text)-1]==' ':
		text=text[:len(text)-1]

	########## Removes multiple spaces which are adjacent (if present): ##########

	if ' ' in text:
		text=text.split()
		i=0
		tempo=''
		for i in range(0,len(text)):
			text[i]=text[i].lower()
			text[i]=text[i][0].upper()+text[i][1:]
			tempo=tempo+' '+text[i]
		text=tempo[1:]

	########## Other wise just capitalises the first character (if not a digit): ##########

	else:
		if(not text[0].isdigit()):
			text=text.lower()
			text=text[0].upper()+text[1:]
	
	########## Prepares abbreviated location names (if present): ##########

	if(' ' in text and len(text)==3):
		text=text.split()
		text0=text[0].lower()
		text0=text0[0].upper()+text0[1:]
		text1=text[1].lower()
		text1=text1[0].upper()+text1[1:]
		text=text0+text1

	return text

###########################################################################