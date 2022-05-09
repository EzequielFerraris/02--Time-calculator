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

    min_sum += min_start
    hours_sum += hours_start

#CONVERT MIN TO HOURS IF > 60 AND HOURS TO 12 CLOCK

    while min_sum > 60:
        min_sum -= 60
        hours_sum += 1

    while hours_sum > 12:
        hours_sum -= 12
        daytime_sum += 1
    if hours_sum == 12:
        daytime_sum += 1
      
#GIVE FORMAT TO MINUTES "07"
    min_format = str(min_sum)
    if len(min_format) == 1:
        min_format = '0' + min_format
      
#DETERMINE THE DAYTIME   
    daytime_new = daytime
    if daytime_new == 'AM' and (daytime_sum % 2 == 1):
        daytime_new = 'PM'
    elif daytime_new == 'PM' and (daytime_sum % 2 == 1):
        daytime_new = 'AM'

#CALCULATE THE PASSAGE OF DAYS
    
    count1 = daytime_sum
    if daytime == 'AM' and count1 >= 2:
      while count1 >= 2:
            count1 -= 2
            days_passed += 1
    if daytime == 'PM' and count1 >= 1:
      count1 -=1
      days_passed += 1
      while count1 >= 2:
          count1 -= 2
          days_passed += 1
      
#PASSAGE OF DAYS' FORMAT AND OUTPUT
        
    days_passed_output = ''

    if days_passed == 1:
        days_passed_output = '(next day)'
    if days_passed >= 2:
        days_passed_output = '('+str(days_passed)+' '+'days later)'

#RESULTS
  #NO DAYS PASSED
    result1 = (str(hours_sum)+':'+min_format+' '+daytime_new)
    if days_passed == 0 and starting_day == None:
        return result1

  #DAY OF THE WEEK SPECIFIED
      
    weeks_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    if starting_day != None:
        week_starting_day = starting_day.lower()
        sum_days = weeks_days.index(week_starting_day)
        sum_days += days_passed
        while sum_days >=7 :
            sum_days -= 7
        result_day = weeks_days[sum_days]
        result_day = ', ' + result_day[0].upper() + result_day[1:]
        result_day = result_day.rstrip()
      
        if days_passed == 0:
          return (str(hours_sum)+':'+min_format+' ' +daytime_new +str(result_day))

          
        if days_passed >=1:
          return (str(hours_sum)+':'+min_format+' ' +daytime_new +str(result_day)+' '+days_passed_output.rstrip())
      
  #ONE OR MORE DAYS PASSED
      
    result2 = (str(hours_sum)+':'+min_format+' '+daytime_new+' '+days_passed_output)
    if days_passed >= 1:
        return result2

 

   
