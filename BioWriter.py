Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:36:03) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import time
>>> 
>>> def biography():
	name = input("name > ")
	DOB = input("Date of birth > ")
	POB = input("place of birth > ")
	dad_name = input("name of father > ")
	mom_name = input("name of mother > ")
	print("processing...")
	time.sleep(2)
	print(name + " was born on " + DOB + " in " + POB + " to " + dad_name + " and " + mom_name)

	
>>> biography()
name > john
Date of birth > 14th jan, 2004
place of birth > England
name of father > Frank
name of mother > isabel
processing...
john was born on 14th jan, 2004 in England to Frank and isabel
>>> 
