#MAIN FUNCTION
def add_time(start, duration, starting_day = None):
  
#START VARIABLES
    min_start = 0
    hours_start = 0
    daytime = ''
    days_passed = 0

#ACCUMULATIVE VARIABLES
    min_sum = 0
    hours_sum = 0
    daytime_sum = 0

#GET THE STARTING DATA AND TURN INTO NUMBERS
  
    temp1 = start.split(' ')
    daytime = temp1[1]

    temp2 = temp1[0].split(':')
    min_start = int(temp2[1])
    hours_start = int(temp2[0])

#GET THE ADDING DATA AND TURN INTO NUMBERS

    temp3 = duration.split(':')
    min_sum += int(temp3[1])
    hours_sum += int(temp3[0])
    
#ADD HOURS AND MINUTES
