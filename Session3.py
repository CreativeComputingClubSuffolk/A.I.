import time
username=""
running=True
userage=0
Test=""

positiveResults = []
with open('positives.txt') as inputfile:
    for line in inputfile:
        positiveResults.append(line.strip().split(','))

negativeResults = []
with open('negatives.txt') as inputfile:
    for line in inputfile:
        negativeResults.append(line.strip().split(','))

def CheckPositive(Response):
    for x in range(0, len(positiveResults)):
        Response=Response.lower();
        if Response==''.join(positiveResults[x]):
            print "Great!"
            return True;

def CheckNegative(Response):
    for x in range(0, len(negativeResults)):
        Response=Response.lower();
        if Response==''.join(negativeResults[x]):
            print "OK"
            return True;
    
def learnNew(Response):
    print " "
    print "Sorry I didn't understand."
    outcome = raw_input ("Is "+Response+" a positive or negative affirmation? Please use POS or NEG.")
    if (outcome=="POS"):
        positiveResults.append( Response );
        learnedNew();
    elif (outcome=="NEG"):
        negativeResults.append( Response );
        learnedNew();

def learnedNew():
    print ('INFORMATION ASSIMILATED')


while (running==True):
    print "Chatbot Version 1"
    print ""
    print "When I ask a question with CAPITAL LETTER ANSWERS included"
    print "Please choose one of those specific answers as it"
    print "helps me learn and understand the world a bit better."
    print ""

    while username=="":
        username =raw_input("Hello, what is your name? ")
        username=username.capitalize()
        
    print "Hello "+username+", pleased to meet you."
    print "My name is Chatbot 1"
    userage =raw_input(username +" How old are you? ")

    try:
        int(userage)
        validAge=1
    except ValueError:
        userage==""
        print "Sorry " +username +" I didn't understand. Please use a Number"
        print ""
    
    curmonth = time.strftime("%m")
    month =raw_input(username +" What month were you born? 01,02,03 etc... ")

    if (month<=curmonth):
        year=2017-int(userage)

    else:
        year=2016-int(userage)


    while Test=="":
        Response = raw_input ("So you were born in "+str(year)+"? ")

        if CheckPositive(Response)==True:
            Test="Complete"

        if CheckNegative(Response)==True:
            GResponse = raw_input ("What year where you born in ? ")
            year=GResponse.lower()
            Test="Complete"
            print year

        if Test=="":
            learnNew(Response)

    running=False
    
