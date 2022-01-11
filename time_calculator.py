#TIME CALCULATOR
#Project for py4e Certificate
#https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator

def add_time(start, duration, day = False):
  
# splitting the starting time
  start_1 = start.split(":")[0]
  start_2 = start.split(":")[1]
  start_3 = start_2.split(" ")[1]
  start_2 = start_2.split(" ")[0]
  
  start_h = int(start_1)
  start_m = int(start_2)
  start_str = str(start_3)
  #print("\nSTART \n", start_h, start_m, start_str)


# splitting the duration time
  dur_h = int(duration.split(":")[0])
  dur_m = int(duration.split(":")[1])
  #print("DURATION \n", dur_h, dur_m)

# adding start and duration
# MINUTES 
  new_h = 0
  all_m = start_m + dur_m
  if all_m < 60:
    sum_m = all_m
    #print("SUM_M", sum_m)
  else:
    sum_m = all_m - 60
    #print("MORE THAN 60 MINUTES!")
    #print("SUM_M", sum_m)
    new_h += 1
    #print("NEW_H", new_h)


  # HOURS & DAYS
  all_h = new_h + start_h + dur_h
  #print("ALL_HOURS", all_h)
  days_later = 0
  sum_d = all_h / 24
  remaining_h = 0
  new_time = ""
  next_day = "(next day)"

  #print("SUM_DAYS", sum_d)
  if sum_d >= 1.0:
    days_later = round(sum_d)
    #print("DAYS LATER", days_later)
    remaining_h = all_h % 24
    #print("REMAINING_HOURS", remaining_h)
  else:
    remaining_h = all_h
    #print("REMAINING_HOURS", remaining_h)
 
  # AM/PM SWITCH
  #no switch!
  if remaining_h < 12:
    sum_h = remaining_h
    if days_later == 1:
      new_time = (f"{sum_h}:{sum_m:02} {start_str} {next_day}")
    else:
      new_time = (f"{sum_h}:{sum_m:02} {start_str}")
    #print("SUM_H", sum_h)
    
  #yes switch!
  else:
    sum_h = remaining_h - 12
    if sum_h == 0:
      sum_h = 12
    #print("SWITCH AM/PM!\n", "SUM_H", sum_h)
    #crossing noon --> AM-PM switch!
    if start_str == "AM":
      start_str = "PM"
      #print ("NEW STRING", start_str)
      if days_later < 1:
        new_time = (f"{sum_h}:{sum_m:02} {start_str}")
      else:
        new_time = (f"{sum_h}:{sum_m:02} {start_str} ({days_later} days later)" )
    #crossing midnight --> PM-AM switch! 
    else:
      start_str = "AM"
      #print ("NEW STRING", start_str)
      if days_later <= 1:
        new_time = (f"{sum_h}:{sum_m:02} {start_str} {next_day}")
      else:
        new_time = (f"{sum_h}:{sum_m:02} {start_str} ({days_later} days later)")
  #print(new_time)


#************** WITH WEEKDAY ****************#
 
  week = {"monday": 1, "tuesday": 2, "wednesday": 3, "thursday": 4, "Friday": 5, "saturday": 6, "sunday": 7}

  week_r = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}

  if day:
    day = str((day).lower())
    pos_d = week[day]
    new_d = pos_d
    #print("POSITION DAY", pos_d)

    # AM/PM SWITCH
    #no switch!
    if remaining_h < 12:
      sum_h = remaining_h
      if days_later == 1:
        new_time = (f"{sum_h}:{sum_m:02} {start_str}, {week_r[pos_d+1]} {next_day}")
      else:
        new_time = (f"{sum_h}:{sum_m:02} {start_str}, {week_r[pos_d+days_later]}")
      
    #DO NOT SWITCH AGAIN!
    else:
      sum_h = remaining_h - 12
      if sum_h == 0:
        sum_h = 12
    
      if start_str == "AM":
        #print ("NEW STRING", start_str)
        if days_later < 1:
          new_time = (f"{sum_h}:{sum_m:02} {start_str}, {week_r[pos_d]}")
        else:
          if pos_d+days_later > 7:
            new_d = (pos_d+days_later) % 7
          else: 
            new_d = (pos_d+days_later)
          new_time = (f"{sum_h}:{sum_m:02} {start_str}, {week_r[new_d]} ({days_later} days later)")
 
      else:
        #print ("NEW STRING", start_str)
        if days_later <= 1:
          new_time = (f"{sum_h}:{sum_m:02} {start_str}, {week_r[pos_d+1]} {next_day}")
        else:
          if pos_d+days_later > 7:
            new_d = (pos_d+days_later) % 7
          else: 
            new_d = (pos_d+days_later)
          new_time = (f"{sum_h}:{sum_m:02} {start_str}, {week_r[new_d]} ({days_later} days later)")
    
  return new_time