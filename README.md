# Rambo

 Rambo, a discord bot who interacts with the users and recommends songs and inspirational quotes depending on the user's emotions using Sentimental Analysis.


## **Stack** 
- Is coded in Python
- Uses 
  - Last.fm API for song recommendations using method tag.gettoptracks
  - Zenquotes.io API for inspiritaional quotes
  - Text Blob to perform sentiment ananlysis

  
## **APIs**
-  [Last.fm](https://www.last.fm/api)
-  [Zenquotes.io](https://zenquotes.io/api)

## **Setting up Discord**
-  Create a Discord bot
  
  1 Go to [https://discord.com/developers/applications](https://discord.com/developers/applications) Create an application </br>
  2 Build a discord Bot under the application</br>
  3 Get the token from bot setting</br>
  4 Store the token to TOKEN in main.py</br>
  5 Create text channel </br>
  6 Invite Bot to your Server</br>
  7 Invite your bot to your server via OAuth2 URL Generator</br>
 ![dd](https://user-images.githubusercontent.com/120661612/208284779-6021a987-8d41-4348-b7b2-be8369bf5a8c.png)


## **Installation**
-   python -m pip install requests
-   pip install -U textblob
-   python -m textblob.download_corpora


## **Modules and Libraries used**
-   random
-   json
-   requests
-   textblob
## **Features**
-   The user can get inspirational quotes by giving the command '$inspire'</br>![hack](https://user-images.githubusercontent.com/120661612/208284746-cfbe457e-c2e9-4469-a437-eaada17a00d4.png)

-   Rambo detects the user's emotions by interacting with them and analyze their moods using textblob Sentiment Analysis. And recommends music according to their moods.</br>![2](https://user-images.githubusercontent.com/120661612/208284798-6770114f-ff17-4d2e-a3ad-6f4aa75faa90.png)
</br>![3](https://user-images.githubusercontent.com/120661612/208284810-67727b2d-bee6-455f-b920-d9c9b1f9af64.png)

-   There is also a provision to get uplifting messages from Rambo when the user is not in a good mood.</br>![6](https://user-images.githubusercontent.com/120661612/208284824-61ac997b-5467-4799-8d38-0de645877e50.png)

