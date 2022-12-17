import random
import json
from textblob import TextBlob
bot_name = "RAMBO"
emo =[]


def askQuestion(q_index):

    questions = [
     ["Hey, How was your day?","Hola! How's the day been so far"," how has life been treating you this fine day"],
     ["How are you feeling?", "What about you how are you?","Are you kk bro?"],
     ["What do you think about life?", "What is your opinion on the world?","What are your thoughts on love?"],
     ["What do you think about me?", "What's your opinion on me?"],

    ]
   
    if q_index>len(questions):
        return "Uhohh thas it! Sorryy."   
    sentence = random.sample(questions[q_index],1)
    return sentence[0]

def getResponse(msge,q_index):  
 
    p_answers = [
        ["That's good to hear","NICEE good for you","Look at you living the life"],
        ["That's great to know!!","SOOO happy for you!!","That's the good stuff"],
        ["Ohh interesting","Ahh I think the same!!","Woww that's deep"],
        ["Hehehe thankss xD","OMG THANKSS!!","You're making me blush!!"],
        
    ]
    n_answers = [
        ["I'm sorry to hear that","Hopefully everything will get better","You'll get through this"],
        ["Oh no I hope you feel better","I'm here for you","The bad stuff will eventually fade"],
        ["Really? that's a unique thought","Wow never thought about it that way!!","Hmm that's an interesting opinion"],
        ["Don't take that tone with me young being","UGGGGHH MOOOMMM","oohhh!!!"],
    ]
    
    blob = TextBlob(msge)
        
        

    if blob.polarity > 0:
        emo.append("P")
        sentence = random.sample(p_answers[q_index],1)
    else:
        sentence = random.sample(n_answers[q_index],1)
        emo.append("N")

    return sentence[0]
