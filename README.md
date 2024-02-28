# Twitch-Bibites-Bot
This is my twitch bot for controlling the game from the chat.

## Install instructions:
1. Download the entire repository to a folder on the device you are going to be running The bibites on and streaming to Twitch.
2. You need an application registrered to the account you want the bot to run on, so head over to [https://dev.twitch.tv/console](https://dev.twitch.tv/console) loggin whith the acount you want run the bot with. Register your application if do not have one yet.
3. Once you have an application you need to fill in some variables in the .env file.
   * Copy the Client ID and past it in client_id = "Client ID here"
   * Go to [https://twitchtokengenerator.com/](https://twitchtokengenerator.com/) and get your access token and place it after oauth: in tmi_token = "oauth:access token here"
   * nickname is the name of the account running the bot, place the name in nickname = "nickname here"
   * bot_prefix is the prefix of the prefix that will be used to run commands in Twitch chatbot_prefix = "!"
   * channel is the channel where the bot will respond in (make sure to keep the #), add all the channels where you will be streaming The Bibites channel = "#Your channel name here"
   * Save and close the .env file.
4. Now open The bibites in fullscreen and your prefered streaming software (OBS is a good choise with a lot of tutorials on YouTube) and start the stream
5. Before you start the bot you want to open a simulation.
6. Then either run the [Install.bat](/Install.bat) to install everything you need to run the bot, or run the [Install and Start.bat](/Install-and-Start.bat)(might not start the bot) to install everything you need and start the bot.
   _ If you chose to run [Install.bat](/Install.bat) you need to run the [Start.bat](/Start.bat) file to start the bot.
   Make sure that The Bibites is in the foreground so it wont mess thing up on your device.
7. Head over to Twitch and test the commands run the help command to see what commands you can use (help).
8.  Next time you want to run the bot, start a simulation then run the [Start.bat](/Start.bat)

## Changing settings and commands
For now the only thing you can change is the names of the bibites to place. (!place `Bibite name`)
Open the file Bibites, there you can change the name of the bibites (Try to keep them short so people don't need to write so much) they are sorted like they are in game.
Bibite1_template is the first bibite in the list of templates, Bibite2_template is the second one and so one. The same for the Bibite1_saved, but this time it is for user saved bibites
To change the name "Bibite1_template": "change name here", if you do not have 10 user saved bibites or you do not want to be able to place a template just change the name to "None" ("Bibite1_template": "None")

### Problems you might encounter
This is unfinished, head over to [the unofficial bibites discord server](https://discord.gg/rNDMdNjQ2R) and ask in [Twitch Bibites Bot (simulation)](https://discord.com/channels/1059654549650034748/1203723252350844988). If no one answers you can ping @melting_diamond in the unofficial bibites server.

[Install and Start.bat](/Install-and-Start.bat) This might not start the bot, if it doesnt just run [Start.bat](/Start.bat) to start the bot.
