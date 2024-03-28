#import the library for the popen command
import os

#define the pingMe function
def pingMe():
     
    #type out the ping command
    pingCommand = "ping -c 1 "
    
    #load the user input IP into a variable
    userIP = input("Please enter the IP address: ")
    
    #run ping command with the userIP address variable and save results to variable
    results = os.popen(pingCommand + str(userIP)).read()
    
    #print results to the screen
    print(results)
    
    #find the string "ttl" in the results variable
    found = str(results.find("ttl"))
        
    #check the answer by printing to the screen
    print("The found variable contains the string: " + found) 
    
    #use an if / else statement and check if the found variable is "-1"
    if found == "-1":
        #if found is -1 then print "host not found"!
        print("Host not found!")
        
    else:
        #if found is any other number then print "ping successful!"
        print("Ping successful!")

#make sure to call the pingMe function
pingMe()

#test with 10.0.0.1, ping should fail
#test with google.com, ping should be successful