

import speech_recognition
from datetime import date
from datetime import datetime
time = datetime.now()
dt_string = time.strftime("%d/%m/%Y %H:%M:%S")
today = date.today()
d2 = today.strftime("%B %d, %Y")
while True:
    robot_ear = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        print("Im listening: ")
        audio = robot_ear.listen(mic)
    print ("Robot:.....")
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = "Nothing"
    print("You said: " + you)
    
    robot_brain = ""
    if  "hello" in you:
        robot_brain  = "Hello Thịnh"
    elif "name" in you:
        robot_brain = "I'm Johnny"
    elif "who" in you:
        robot_brain = "I'm your vitural assistant"
    elif "today" in you:
        robot_brain = "Today is ", d2 ,"and today you show your project to teacher Trần Khải Thiện"
    elif "time" in you:
        robot_brain = "It is: ",dt_string
    
    elif "from" in you:
        robot_brain = "I from google, created in May 18, 2016"
    elif "bye" in you:
        robot_brain = "Byeeeeeeee,see you again"
        import pyttsx3
        engine = pyttsx3.init()
        engine.say(robot_brain)
        print("Robot:"+str(robot_brain))
        engine.runAndWait()
        break
    else:
        robot_brain = "Please say again, i can't hear you"
    import pyttsx3
    engine = pyttsx3.init()
    engine.say(robot_brain)
    print("Robot:"+str(robot_brain))
    engine.runAndWait()






       