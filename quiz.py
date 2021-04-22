from datetime import datetime





week_day = ['Monday', 'Tuesday', 'Wensday', 'Thusday', 'Friday', 'Saturday', 'Sunday']

for day in week_day:
    # and logical operator dont work here 
    if 'S' in day :
        continue
    #print(day)    
        
    else:
        print("\n")
        custom1 = input("Start Working Time  hour:minutes:seconds: ")
        object1 = datetime.strptime(custom1, "%H:%M:%S")

        start_time = "08:00:00"

        custom2 = input("End Working Time  hour:minutes:seconds: ")
        object2 = datetime.strptime(custom2, "%H:%M:%S")
        
        end_time = "17:00:00"

        if  custom1 < start_time and start_time < end_time:
            print("The working time start at  8:00:00")
        else:
            
            total_hrs = object2 - object1
            print(total_hrs.total_seconds())
            print(day)
else:
    print("Finished")       
        
        
        



