import os, subprocess, tkinter, time, json
from twitchio.ext import commands
from dotenv import load_dotenv
from pyautogui import press, typewrite, hotkey
from ahk import AHK
from pathlib import Path

script_dir = Path( __file__ ).parent.absolute()

ahk = AHK()

root = tkinter.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

load_dotenv()

token = os.getenv("tmi_token")
client_id = os.getenv("client_id")
nick = os.getenv("nickname")
prefix = os.getenv("bot_prefix")
initial_channels = os.getenv("channel")

class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        super().__init__(token=token, prefix=prefix, initial_channels=[initial_channels])
        self.last_command = None

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')
        for channel in bot.connected_channels:
            await channel.send(f'/me has landed')
    
    @commands.command(aliases=['h'])
    async def help(self, ctx: commands.Context):
        self.last_command = "help"
        
        await ctx.send('The commands you can use are: !random !oldest !egg !gen !zone !panning !zoom in !zoom out !brain !biology !genes !stats !rename !place `name of bibite` !information !alias !thanos')
    
    @commands.command()
    async def alias(self, ctx: commands.Context):
        self.last_command = "alias"
        
        await ctx.send('The commands you can use are: !r !o !e !g !z !k !+ !- !bio !gene !stat !info')

    @commands.command(aliases=['r'])
    async def random(self, ctx: commands.Context):

        self.last_command = "random"
        
        hotkey('ctrl', 'r')
        await ctx.send(f'{ctx.author.name} selected a random bibite')
    
    @commands.command(aliases=['o'])
    async def oldest(self, ctx: commands.Context):
        self.last_command = "oldest"
        
        hotkey('ctrl', 'o')
        await ctx.send(f'{ctx.author.name} selected the oldest bibite')
    
    @commands.command(aliases=['e'])
    async def egg(self, ctx: commands.Context):
        self.last_command = "egg"
        
        hotkey('ctrl', 'e')
        await ctx.send(f'{ctx.author.name} selected a random egg')
    
    @commands.command(aliases=['g'])
    async def gen(self, ctx: commands.Context):
        self.last_command = "gen"
        
        hotkey('ctrl', 'g')
        await ctx.send(f'{ctx.author.name} selected the bibite with the highest generation count')
    
    @commands.command(aliases=['z'])
    async def zone(self, ctx: commands.Context):
        self.last_command = "zone"
        
        press('z')
        await ctx.send(f'{ctx.author.name} selected a random zone')
    
    @commands.command(aliases=['k'])
    async def panning(self, ctx: commands.Context):
        self.last_command = "panning"
        
        press('k')
        await ctx.send(f'{ctx.author.name} turned on autopanning')
    
    @commands.command(aliases=['+'])
    async def zoompluss(self, ctx: commands.Context):
        self.last_command = "zoom"

        press('+')
        await ctx.send(f'{ctx.author.name} zoomed in')
    
    @commands.command(aliases=['-'])
    async def zoomminus(self, ctx: commands.Context):
        self.last_command = "zoom"
        
        press('-')
        await ctx.send(f'{ctx.author.name} zoomed out')

    @commands.command(aliases=['+', '-'])
    async def zoom(self, ctx: commands.Context, inorout : str = "None"):
        self.last_command = "zoom"
        
        if inorout == "out":
            press('-')
            await ctx.send(f'{ctx.author.name} zoomed out')

        elif inorout == "in":
            press('+')
            await ctx.send(f'{ctx.author.name} zoomed in')
    
    @commands.command()
    async def restart(self, ctx: commands.Context):
        if ctx.author.name == "melting__diamond":
            await ctx.send(f'Restarting the bot...')
            
            # Start the new instance of the bot
            process = subprocess.Popen(["start", "Start.bat"], shell=True)
            
            # Wait for the subprocess to finish
            process.wait()
            
            # Close the current bot instance
            await self.close()
        else:
            await ctx.send(f'Only admin can restart the bot')
    
    @commands.command()
    async def brain(self, ctx: commands.Context):
        self.last_command = "brain"
        
        ahk.mouse_move(screen_width/7.5, screen_height/21, speed=1, relative=False)
        ahk.click()

        await ctx.send(f'{ctx.author.name} swapped to the brain panel')
    
    @commands.command(aliases=['bio'])
    async def biology(self, ctx: commands.Context):
        self.last_command = "biology"
        
        ahk.mouse_move(screen_width/10, screen_height/21, speed=1, relative=False)
        ahk.click()

        await ctx.send(f'{ctx.author.name} swapped to the biology panel')
    
    @commands.command(aliases=['gene'])
    async def genes(self, ctx: commands.Context):
        self.last_command = "genes"
        
        ahk.mouse_move(screen_width/16, screen_height/21, speed=1, relative=False)
        ahk.click()

        await ctx.send(f'{ctx.author.name} swapped to the genes panel')
    
    @commands.command(aliases=['stat'])
    async def stats(self, ctx: commands.Context):
        self.last_command = "stats"
        
        ahk.mouse_move(screen_width/40, screen_height/21, speed=1, relative=False)
        ahk.click()

        await ctx.send(f'{ctx.author.name} swapped to the stats panel')
    
    @commands.command(aliases=['info'])
    async def information(self, ctx: commands.Context):
        self.last_command = "info"
        
        ahk.mouse_move(screen_width/1.1, screen_height/21, speed=1, relative=False)
        ahk.click()

        await ctx.send(f'{ctx.author.name} swapped to the information and statistics panel')

    @commands.command()
    async def rename(self, ctx: commands.Context, name : str = None):
        self.last_command = "rename"
        
        if name == None:
            name = ctx.author.name
        
        if self.last_command != "stats" or self.last_command != "rename":
            ahk.mouse_move(screen_width/40, screen_height/21, speed=1, relative=False)
            ahk.click()
            time.sleep(0.2)
        ahk.mouse_move(screen_width/4.5, screen_height/9.5, speed=1, relative=False)
        ahk.click()
        time.sleep(0.2)
        typewrite(name, interval=0.05)
        press("enter")

        await ctx.send(f'{ctx.author.name} changed the name of the bibite to {name}')
    
    @commands.command()
    async def place(self, ctx: commands.Context, bibite : str = "None"):
        self.last_command = "place"

        with open(f"{script_dir}/Bibites", "r") as file:
            Bibites_dict = json.load(file)
        
        Bibites_list = list(Bibites_dict.values())

        Bibites_list = [value for value in Bibites_list if value != "None"]

        if bibite == "None":
            await ctx.send(f'The bibites you can place are: {Bibites_list}')
            return
            
        bibite = bibite.lower()

        ahk.mouse_move(screen_width/41, screen_height/1.02, speed=1, relative=False) # Go to petri dish icon
        time.sleep(0.1)
        ahk.click()

        time.sleep(0.2)
        ahk.mouse_move(screen_width/41, screen_height/1.08, speed=1, relative=False) # Go to place bibite
        time.sleep(0.1)
        ahk.click()

        if bibite == Bibites_dict["Bibite1_template"]:
            time.sleep(0.2)
            ahk.mouse_move(screen_width/10, screen_height/4.05, speed=1, relative=False) # Choose first bibite from the template
            time.sleep(0.1)
            ahk.click()
        elif bibite == Bibites_dict["Bibite2_template"]:
            time.sleep(0.2)
            ahk.mouse_move(screen_width/10, screen_height/3.5, speed=1, relative=False) # Choose second bibite from the template
            time.sleep(0.1)
            ahk.click()
        elif bibite == Bibites_dict["Bibite3_template"]:
            time.sleep(0.2)
            ahk.mouse_move(screen_width/10, screen_height/3, speed=1, relative=False) # Choose the third bibite from the template
            time.sleep(0.1)
            ahk.click()
        elif bibite == Bibites_dict["Bibite4_template"]:
            time.sleep(0.2)
            ahk.mouse_move(screen_width/10, screen_height/2.7, speed=1, relative=False) # Choose the forth bibite from the template
            time.sleep(0.1)
            ahk.click()
        elif bibite == Bibites_dict["Bibite5_template"]:
            time.sleep(0.2)
            ahk.mouse_move(screen_width/10, screen_height/2.4, speed=1, relative=False) # Choose the fifth bibite from the template
            time.sleep(0.1)
            ahk.click()
        elif bibite == Bibites_dict["Bibite6_template"]:
            time.sleep(0.2)
            ahk.mouse_move(screen_width/10, screen_height/2.2, speed=1, relative=False) # Choose the sixth bibite from the template
            time.sleep(0.1)
            ahk.click()
        elif bibite == Bibites_dict["Bibite7_template"]:
            time.sleep(0.2)
            ahk.mouse_move(screen_width/10, screen_height/2, speed=1, relative=False) # Choose the seventh bibite from the template
            time.sleep(0.1)
            ahk.click()
        elif bibite == Bibites_dict["Bibite8_template"]:
            time.sleep(0.2)
            ahk.mouse_move(screen_width/10, screen_height/1.8, speed=1, relative=False) # Choose the eighth bibite from the template
            time.sleep(0.1)
            ahk.click()
        elif bibite == Bibites_dict["Bibite9_template"]:
            time.sleep(0.2)
            ahk.mouse_move(screen_width/10, screen_height/1.7, speed=1, relative=False) # Choose the nineth bibite from the template
            time.sleep(0.1)
            ahk.click()
        elif bibite == Bibites_dict["Bibite1_saved"]:
            time.sleep(0.2)
            ahk.mouse_move(screen_width/10, screen_height/21, speed=1, relative=False) # Click saved bibite
            time.sleep(0.1)
            ahk.click()

            time.sleep(0.2)
            ahk.mouse_move(screen_width/10, screen_height/4.05, speed=1, relative=False) # Choose the first bibite from the saved bibites
            time.sleep(0.1)
            ahk.click()
        elif bibite == Bibites_dict["Bibite2_saved"]:
            time.sleep(0.2)
            ahk.mouse_move(screen_width/10, screen_height/21, speed=1, relative=False) # Click saved bibite
            time.sleep(0.1)
            ahk.click()

            time.sleep(0.2)
            ahk.mouse_move(screen_width/10, screen_height/3.5, speed=1, relative=False) # Choose second bibite from the saved bibites
            time.sleep(0.1)
            ahk.click()
        elif bibite == Bibites_dict["Bibite3_saved"]:
            time.sleep(0.2)
            ahk.mouse_move(screen_width/10, screen_height/21, speed=1, relative=False) # Click saved bibite
            time.sleep(0.1)
            ahk.click()

            time.sleep(0.2)
            ahk.mouse_move(screen_width/10, screen_height/3, speed=1, relative=False) # Choose the third bibite from the saved bibites
            time.sleep(0.1)
            ahk.click()
        elif bibite == Bibites_dict["Bibite4_saved"]:
            time.sleep(0.2)
            ahk.mouse_move(screen_width/10, screen_height/21, speed=1, relative=False) # Click saved bibite
            time.sleep(0.1)
            ahk.click()

            time.sleep(0.2)
            ahk.mouse_move(screen_width/10, screen_height/2.7, speed=1, relative=False) # Choose the forth bibite from the saved bibites
            time.sleep(0.1)
            ahk.click()
        elif bibite == Bibites_dict["Bibite5_saved"]:
            time.sleep(0.2)
            ahk.mouse_move(screen_width/10, screen_height/21, speed=1, relative=False) # Click saved bibite
            time.sleep(0.1)
            ahk.click()

            time.sleep(0.2)
            ahk.mouse_move(screen_width/10, screen_height/2.4, speed=1, relative=False) # Choose the fifth bibite from the saved bibites
            time.sleep(0.1)
            ahk.click()
        elif bibite == Bibites_dict["Bibite6_saved"]:
            time.sleep(0.2)
            ahk.mouse_move(screen_width/10, screen_height/21, speed=1, relative=False) # Click saved bibite
            time.sleep(0.1)
            ahk.click()

            time.sleep(0.2)
            ahk.mouse_move(screen_width/10, screen_height/2.2, speed=1, relative=False) # Choose the sixth bibite from the saved bibites
            time.sleep(0.1)
            ahk.click()
        elif bibite == Bibites_dict["Bibite7_saved"]:
            time.sleep(0.2)
            ahk.mouse_move(screen_width/10, screen_height/21, speed=1, relative=False) # Click saved bibite
            time.sleep(0.1)
            ahk.click()

            time.sleep(0.2)
            ahk.mouse_move(screen_width/10, screen_height/2, speed=1, relative=False) # Choose the seventh bibite from the saved bibites
            time.sleep(0.1)
            ahk.click()
        elif bibite == Bibites_dict["Bibite8_saved"]:
            time.sleep(0.2)
            ahk.mouse_move(screen_width/10, screen_height/21, speed=1, relative=False) # Click saved bibite
            time.sleep(0.1)
            ahk.click()

            time.sleep(0.2)
            ahk.mouse_move(screen_width/10, screen_height/1.8, speed=1, relative=False) # Choose the eighth bibite from the saved bibites
            time.sleep(0.1)
            ahk.click()
        elif bibite == Bibites_dict["Bibite9_saved"]:
            time.sleep(0.2)
            ahk.mouse_move(screen_width/10, screen_height/21, speed=1, relative=False) # Click saved bibite
            time.sleep(0.1)
            ahk.click()

            time.sleep(0.2)
            ahk.mouse_move(screen_width/10, screen_height/1.7, speed=1, relative=False) # Choose the nineth bibite from the saved bibites
            time.sleep(0.1)
            ahk.click()
        elif bibite == Bibites_dict["Bibite10_saved"]:
            time.sleep(0.2)
            ahk.mouse_move(screen_width/10, screen_height/21, speed=1, relative=False) # Click saved bibite
            time.sleep(0.1)
            ahk.click()

            time.sleep(0.2)
            ahk.mouse_move(screen_width/10, screen_height/1.6, speed=1, relative=False) # Choose the tenth bibite from the saved bibites
            time.sleep(0.1)
            ahk.click()
        else:
            await ctx.send(f'You misspelled the name, the bibites you can place are: {Bibites_list}')
            return

        time.sleep(0.2)
        ahk.mouse_move(screen_width/1.1, screen_height/1.1, speed=1, relative=False) # Click confirm
        time.sleep(0.1)
        ahk.click()

        time.sleep(0.2)
        ahk.mouse_move(screen_width/7, screen_height/1.11, speed=1, relative=False) # Turn on tags
        time.sleep(0.2)
        ahk.click()

        time.sleep(0.2)
        ahk.mouse_move(screen_width/7, screen_height/1.05, speed=1, relative=False) # Click basic tag
        time.sleep(0.2)
        ahk.click()

        time.sleep(0.2)
        ahk.mouse_move(screen_width/3, screen_height/1.5, speed=1, relative=False) # Place bibite
        time.sleep(0.2)
        ahk.click()

        time.sleep(0.2)
        ahk.mouse_move(screen_width/4.9, screen_height/1.21, speed=1, relative=False) # Close placing panel
        time.sleep(0.1)
        ahk.click()

        await ctx.send(f'{ctx.author.name} placed {bibite}')
    
    @commands.command()
    async def thanos(self, ctx: commands.Context, name : str = None):
        self.last_command = "thanos"
        
        time.sleep(0.1)
        ahk.mouse_move(screen_width/20, screen_height/1.02, speed=1, relative=False) # Go to petri dish icon
        time.sleep(0.1)
        ahk.click()

        time.sleep(0.1)
        ahk.mouse_move(screen_width/20, screen_height/1.1, speed=1, relative=False) # Go to petri dish icon
        time.sleep(0.1)
        ahk.click()

        time.sleep(0.1)
        ahk.mouse_move(screen_width/1.7, screen_height/1.8, speed=1, relative=False) # Go to petri dish icon
        time.sleep(0.1)
        ahk.click()

        await ctx.send(f'{ctx.author.name} snaped half the population away')

bot = Bot()
bot.run()