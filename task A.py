from datetime import datetime

def time_diff(t1, t2):
   # format_str = '%d %m %Y %H:%M:%S %z'
    format_str = '%a %d %b %Y %H:%M:%S %z'
    time1 = datetime.strptime(t1, format_str)
    time2 = datetime.strptime(t2, format_str)
    diff = abs((time1 - time2).total_seconds())
    return int(diff)

# Read the number of test cases
T = 2

for _ in range(1):
    # Read the individual parts of the first timestamp
    #day1 = input("Enter day for timestamp 1: ")
   # month1 = input("Enter month for timestamp 1: ")
   # year1 = input("Enter year for timestamp 1: ")
   # hour1 = input("Enter hour for timestamp 1: ")
    #minute1 = input("Enter minute for timestamp 1: ")
   # second1 = input("Enter second for timestamp 1: ")
    #timezone1 = input("Enter timezone for timestamp 1: ")

    # Read the individual parts of the second timestamp
    #day2 = input("Enter day for timestamp 2: ")
    #month2 = input("Enter month for timestamp 2: ")
   # year2 = input("Enter year for timestamp 2: ")
    #hour2 = input("Enter hour for timestamp 2: ")
    #minute2 = input("Enter minute for timestamp 2: ")
    #second2 = input("Enter second for timestamp 2: ")
   # timezone2 = input("Enter timezone for timestamp 2: ")

    # Create the timestamp strings
  # t1 = f"{day1} {month1} {year1} {hour1}:{minute1}:{second1} {timezone1}"
   # t2 = f"{day2} {month2} {year2} {hour2}:{minute2}:{second2} {timezone2}"

    t1 = "Sun 10 May 2015 13:54:36 -0700"
    t2 = "Sun 10 May 2015 13:54:36 -0000"
    t3 ="Sat 02 May 2015 19:54:36 +0530"
    t4="Fri 01 May 2015 13:54:36 -0000"
    # Calculate the time difference
    diff = time_diff(t1, t2)
    diff2 = time_diff(t3, t4)

    # Print the result
    print("the timestamps that you entered are " , t1,t2,t3,t4)
    print("Sample timestamp used as t1 is ->" , t1)
    print("Sample timestamp used as t2 is ->" , t2)
    print("Sample timestamp used as t3 is ->" , t3)
    print("Sample timestamp used as t4 is ->" , t4)
    print("The absolute difference in seconds is for t1 and t2 is :", diff)
    print("The absolute difference in seconds is for t3 and t4 is :", diff2)
