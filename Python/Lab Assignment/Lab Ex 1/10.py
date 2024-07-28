monthsWith31Days = [
    "January", "March","May", 
    "July", "August", "October", "December"
]

monthsWith30Days = [
   "April", "June", 
     "September", "November"
]
SpecailCase = [
    "February"
]

input_Month = input("Enter Month")
input_year = int(input("Enter The Year"))
isLeapYear = 0

if (input_year % 4 ==0 and input_Month in SpecailCase):
    print("No of days 29")
if (input_Month in SpecailCase):
    print("No of days 28")
if( input_Month in monthsWith30Days):
    print("No of days 30")
if( input_Month in monthsWith31Days ):
    print("No of days 31")