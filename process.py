log_file = open("um-server-01.txt") #opening and renaming the txt file


def sales_reports(log_file): #declaring a function
    for line in log_file: #start of actions, "for every line in the file"
        line = line.rstrip() #this is removing and whitespace at the end of the line.
        day = line[0:3] #creating a variable for a portion or word in each line
        if day == "Mon": #checking for a certain value of that portion
            print(line) #print the line if the condition is met


sales_reports(log_file)
