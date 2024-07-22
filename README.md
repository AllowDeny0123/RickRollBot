# Rickrollbot
Discord bot to "Rickroll" people.
USE WITH CAUTION... bc your friends gonna be mad about this\
Try live: https://discord.gg/JbyZHg93Pk
## Run via build
```
git clone https://github.com/AllowDeny0123/RickRollBot.git
cd RickRollBot
docker build -t rickrollbot .
docker run -it -d -e token="*PLACE DISCORD BOT TOKEN HERE*" rickrollbot
```
## Run via Dockerhub
```
docker run -it -d -e token="*PLACE DISCORD BOT TOKEN HERE*" allowdeny/rickrollbot
```
Bot should be able to enter VC and speak w/ voice activation. Also might need some special intents(not tested)
If you not familiar with Discord bot development and etc.
visit: https://discord.com/developers/docs/intro
for more detailed info about bots and apps in Discord.

# Use scenario
- Create empty server
- Make a VC channel
- Create direct invite to VC(should automatically connect to VC on accepting invite)
- Voilà! You rickrolled your (i hope still a) friend
