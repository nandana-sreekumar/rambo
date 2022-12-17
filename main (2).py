import os
my_secret = os.environ['TOKEN']
import discord
import requests
import json
import random
from replit import db
from keep_alive import keep_alive
from textblob import TextBlob
intents = discord.Intents().all()
client = discord.Client(intents=intents);
emo=[]
msg = ""
blob =""
indx = 0
#q_index=0
#p_in=0
#n_in=0

questions = [
     ["Hey, How was your day?","Hola! How's the day been so far"," how has life been treating you this fine day"],
     ["How are you feeling?", "What about you how are you?","Are you kk bro?"],
     ["What do you think about life?", "What is your opinion on the world?","What are your thoughts on love?"],
     ["What do you think about me?", "What's your opinion on me?"],

    ]
op=questions
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
    

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person / rambo!"
]

if "responding" not in db.keys():
  db["responding"] = True
async def q1_response(msg,blob,message,index):
      print(index)
      if blob.polarity > 0:
          
          a=p_answers        
          emo.append("P")
          if (index < len(a)):
            await message.channel.send(random.choice(a[index]))
          #p_in+=1
          #q_index+=1
          if (index+1 < len(op)):
            await message.channel.send(random.choice(op[index+1]))
          else:
            await message.channel.send("Qusetions Over. :( Type 'hello' to start over!")
          
        
      elif blob.polarity==0:
         await message.channel.send('😊')
         await message.channel.send(random.choice(op[index+1]))
      else:  
            b=n_answers
            if (index < len(b)):
              await message.channel.send(random.choice(b[index]))
            #p_in+=1
            #q_index+=1
            if (index+1 < len(op)):
              await message.channel.send(random.choice(op[index+1]))
            else:
              await message.channel.send("Qusetions Over. :( Type 'hello' to start over!")
        
            emo.append("N")
      # q2_response(msg,blob,message)
  
async def q2_response(msg,blob,message):
  if blob.polarity > 0:
      
      a=p_answers        
      emo.append("P")
      await message.channel.send(random.choice(a[2]))
      #p_in+=1
      #q_index+=1
      await message.channel.send(random.choice(op[3]))
      
    
  elif blob.polarity==0:
    await message.channel.send('😊')
    await message.channel.send(random.choice(op[3]))
  else:  
        b=n_answers
        await message.channel.send(random.choice(b[2]))
        
        # n_in+=1
        # q_index+=1
        await message.channel.send(random.choice(op[3]))
    
        emo.append("N")
  q3_response(msg,blob,message)
async def q3_response(msg,blob,message):
  if blob.polarity > 0:
      
      a=p_answers        
      emo.append("P")
      await message.channel.send(random.choice(a[3]))
      #p_in+=1
      #q_index+=1
      # await message.channel.send(random.choice(op[3]))
      
    
  elif blob.polarity==0:
     await message.channel.send('😊')
  else:  
        b=n_answers
        await message.channel.send(random.choice(b[3]))
        
        # n_in+=1
        # q_index+=1
        # await message.channel.send(random.choice(op[3]))
    
        emo.append("N")
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragment(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
    db["encouragements"] = encouragements

@client.event

async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    global indx
    if message.author == client.user:
      return
  
    msg = message.content
    # q_index=0
    if msg.startswith('hello'):
      indx = 0
      op=questions
      await message.channel.send(random.choice(op[0]))
      return
      #q_index+=1
        
    if msg.startswith('$inspire'):
      quote = get_quote()
      await message.channel.send(quote)
      
    
    #if msg.startswith('$hi'):
     # return discord.Embed(title="starters",description="hey")
    if db["responding"]:
      options = starter_encouragements
      if "encouragements" in db.keys():
          options.extend(db["encouragements"])
  
      if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(options))
  
    if msg.startswith("$new"):
      encouraging_message = msg.split("$new ",1)[1]
      update_encouragements(encouraging_message)
      await message.channel.send("New encouraging message added.")
  
    if msg.startswith("$del"):
      encouragements = []
      if "encouragements" in db.keys():
        index = int(msg.split("$del",1)[1])
        delete_encouragment(index)
        encouragements = db["encouragements"]
      await message.channel.send(encouragements)
  
    if msg.startswith("$list"):
      encouragements = []
      if "encouragements" in db.keys():
        encouragements = db["encouragements"]
      await message.channel.send(encouragements)
  
    if msg.startswith("$responding"):
      value = msg.split("$responding ",1)[1]
  
      if value.lower() == "true":
        db["responding"] = True
        await message.channel.send("Responding is on.")
      else:
        db["responding"] = False
        await message.channel.send("Responding is off.")
    
    
    blob=TextBlob(msg)
    # n_in=0
    # p_in=0
    await q1_response(msg,blob,message,indx)
    indx += 1
    
    
    
    
      
      
    # if blob.polarity > 0:
      
    #   a=p_answers        
    #   emo.append("P")
    #   await message.channel.send(random.choice(a[0]))
    #   #p_in+=1
    #   #q_index+=1
    #   op=questions
    #   await message.channel.send(random.choice(op[1]))
    #   q1_response(msg,blob,message)
      
      
      
      
    # elif blob.polarity==0:
    #    await message.channel.send('😊')
    # else:  
    #       b=n_answers
    #       await message.channel.send(random.choice(b[0]))
    #       q1_response(msg,blob,message)
    #       #q2_response(msg,blob,message)
    #       #q3_response(msg,blob,message)
    #       # n_in+=1
    #       # q_index+=1
    #       await message.channel.send(random.choice(op[1]))
      
    #       emo.append("N")

keep_alive()
client.run(os.getenv('TOKEN'))
# def q1_response():
#   if blob.polarity > 0:
      
#       a=p_answers        
#       emo.append("P")
#       await message.channel.send(random.choice(a[1]))
#       #p_in+=1
#       #q_index+=1
#       await message.channel.send(random.choice(op[2]))
      
    
#   elif blob.polarity==0:
#      await message.channel.send('😊')
#   else:  
#         b=n_answers
#         await message.channel.send(random.choice(b[1]))
        
#         n_in+=1
#         q_index+=1
#         await message.channel.send(random.choice(op[2]))
    
#         emo.append("N")

# def q2_response():
#   if blob.polarity > 0:
      
#       a=p_answers        
#       emo.append("P")
#       await message.channel.send(random.choice(a[2]))
#       #p_in+=1
#       #q_index+=1
#       await message.channel.send(random.choice(op[3]))
      
    
#   elif blob.polarity==0:
#      await message.channel.send('😊')
#   else:  
#         b=n_answers
#         await message.channel.send(random.choice(b[2]))
        
#         n_in+=1
#         q_index+=1
#         await message.channel.send(random.choice(op[3]))
    
#         emo.append("N")
# def q3_response():
#   if blob.polarity > 0:
      
#       a=p_answers        
#       emo.append("P")
#       await message.channel.send(random.choice(a[3]))
#       #p_in+=1
#       #q_index+=1
#       # await message.channel.send(random.choice(op[3]))
      
    
#   elif blob.polarity==0:
#      await message.channel.send('😊')
#   else:  
#         b=n_answers
#         await message.channel.send(random.choice(b[3]))
        
#         n_in+=1
#         q_index+=1
#         # await message.channel.send(random.choice(op[3]))
    
#         emo.append("N")
