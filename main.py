import os
TOKEN = 'Insert your token here'
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


questions = [
     ["Hey, How was your day?","Hola! How's the day been so far"," how has life been treating you this fine day"],
     ["How are you feeling?", "How are you?","Are you ok, bro?"],
     ["What do you think about life?", "What is your opinion on the world?","What are your thoughts on love?"],
     ["What do you think about me?", "What's your opinion on me?"],

    ]
op=questions
API_KEY = '0d9eec3df23c7dbaa2c4c5f2318591fc'
API_SECRET = '993c80c96683071d1423744d9fcd82b9'
USER_AGENT = 'Dataquest'
bot_name = "RAMBO"
i = 1
import requests
headers = {
    'user-agent': USER_AGENT
}
payload = {
    'api_key': API_KEY,
    'method': 'tag.gettoptracks',
    'format': 'json',
    "tracks": 
    {
        "track": [
                  {...},{...}
                 ],
        "@attr": 
        {
            "page": "1",
            "perPage": "5",
            "totalPages": "1",
            "total": "2"
        }
    }
}

def lastfm_get(url,payload):
    response = requests.get(url,headers=headers,params=payload)
    return response



async def getMusic(message): 
  
  
  c = max(emo,key=emo.count)
  check= []

  if c == "P":
    url = 'http://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag=happy&api_key=' + API_KEY + '&format=json'
    r = lastfm_get(url,{'method': 'tag.gettoptracks'})
    #print(r.status_code)
    res = r.json()
    for i in range(10):
      j = random.choice(range(0, 50))
      for k in range(0,len(check)):
        if (check[k]==j):
          j = random.choice(range(0, 50))
          k = 0
      
      await message.channel.send(res['tracks']['track'][j]['name'] + "\n" + res['tracks']['track'][j]['url'] + "\n" + res['tracks']['track'][j]['artist']['name'])
  else:
   url = 'http://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag=sad&api_key=' + API_KEY + '&format=json'
   r = lastfm_get(url,{'method': 'tag.gettoptracks' })
   
   res = r.json()
   for i in range(10):
      j = random.choice(range(0, 50))
      for k in range(0,len(check)):
        if (check[k]==j):
          j = random.choice(range(0, 50))
          k = 0
     
      await message.channel.send(res['tracks']['track'][j]['name'] + "\n" + res['tracks']['track'][j]['url'] + "\n" + res['tracks']['track'][j]['artist']['name'])



p_answers = [
        ["That's good to hear","Nice, good for you","Look at you living the life"],
        ["That's great to know!!","SOOO happy for you!!","That's the good stuff"],
        ["Ohh interesting","Ahh I think the same!!","Woww that's deep"],
        ["Hehehe thankss xD","OMG THANKSS!!","You're making me blush!!"],
        
    ]

n_answers = [
      ["I'm sorry to hear that","Hopefully everything will get better","You'll get through this"],
        ["Oh no I hope you feel better","I'm here for you","The bad stuff will eventually fade"],
        ["Hope it would get better","There's more to explore","We hope you're taking it slow and easy right now"],
        ["Don't take that tone with me young being","oops","oohhh!!!"],
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
          
          if (index+1 < len(op)):
            await message.channel.send(random.choice(op[index+1]))
          else:
            
            msg2=await message.channel.send("Do you want some music :y/n")
            
          
        
      elif blob.polarity==0:
         await message.channel.send('😊')
         if index<len(op):
           await message.channel.send(random.choice(op[index+1]))
      else:  
            b=n_answers
            if (index < len(b)):
              await message.channel.send(random.choice(b[index]))
           
            if (index+1 < len(op)):
              await message.channel.send(random.choice(op[index+1]))
            else:
              
              msg2=await message.channel.send("Do you want some music :y/n")
        
            emo.append("N")
      
  
async def q2_response(msg,blob,message):
  if blob.polarity > 0:
      
      a=p_answers        
      emo.append("P")
      await message.channel.send(random.choice(a[2]))
      
      await message.channel.send(random.choice(op[3]))
      
    
  elif blob.polarity==0:
    await message.channel.send('😊')
    await message.channel.send(random.choice(op[3]))
  else:  
        b=n_answers
        await message.channel.send(random.choice(b[2]))
        
       
        await message.channel.send(random.choice(op[3]))
    
        emo.append("N")
  q3_response(msg,blob,message)
async def q3_response(msg,blob,message):
  if blob.polarity > 0:
      
      a=p_answers        
      emo.append("P")
      await message.channel.send(random.choice(a[3]))
      
      
    
  elif blob.polarity==0:
     await message.channel.send('😊')
  else:  
        b=n_answers
        await message.channel.send(random.choice(b[3]))
        
        
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
    print(message)
    
    if msg.startswith('hello'):
      indx = 0
      op=questions
      await message.channel.send(random.choice(op[0]))
      return
      
        
    if msg.startswith('$inspire'):
      quote = get_quote()
      await message.channel.send(quote)
      
    
    
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
    
    if indx<len(questions): 
      await q1_response(msg,blob,message,indx)
      indx += 1
    if indx == len(questions):
      
      if msg=='y':
            
      
              await getMusic(message)
      elif msg=='n':
        await message.channel.send('Ok bye, see you soon!')
    
keep_alive()
client.run(os.getenv('TOKEN'))
