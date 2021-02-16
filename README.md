# Vibe-Bot
Vibe Bot is a discord bot that does many things.

__Vibe Bot is not publically hosted at this time. You will need to host it yourself.__

Commands
=====
* *!vibecheck* **Performs a vibecheck**
* *!meme* **Posts a meme from r/memes or r/dankmemes**
* *!starmeme* **Posts a meme from r/starwarsmemes**
* *!sandstorm* **;)**

Installation
=====
* pip install -r requirements.txt
* Edit the praw.ini file accordingly. [Info](https://asyncpraw.readthedocs.io/en/latest/getting_started/configuration/prawini.html#using-interpolation)
* Edit the DiscordToken.txt file to include your Discord Application's Bot Token

Permissions Needed
=====
* Send Messages
* Attach Files
* Read Message History
* Add Reactions
* Voice Channel Connect
* Voice Channel Speak
* Voice Channel Use Voice Activity

Known Issues
=====
* Currently, vibe bot retrieves the top 15 posts from the "hot" tab of the selected subreddit. It also adds the posted meme's post id to a list and compares the 15 retrieved posts against said list to prevent posting duplicates. If the command has been run 15 times before new posts are made to the subreddit, no meme will be posted until a new post is made on reddit. 

Todo
=====
* Publically host vibe-bot
* Implement more features
* Fix meme command limitation
