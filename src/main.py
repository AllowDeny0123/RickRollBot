import discord
import asyncio
import os

voice_client = None

def main():
    token = os.environ.get("token")
    class aclient(discord.Client):
        def __init__(self):
            super().__init__(intents=discord.Intents.all())
            self.synced = False
            self.config = []

        async def on_ready(self):
            if not self.synced:
                await tree.sync()
                self.synced = True
            print("Ready for use as {0.user}".format(client))

    client = aclient()
    tree = discord.app_commands.CommandTree(client)

    
    @client.event
    async def on_voice_state_update(m,b,a):
            if a.channel != None and m.id!=client.user.id:
                voice_channel = a.channel
                global voice_client
                voice_client = await voice_channel.connect()
                voice_client.play(discord.FFmpegPCMAudio("./assets/1.mp3"))
                while voice_client.is_playing():
                    await asyncio.sleep(1)
                await voice_client.disconnect()
            if a.channel == None and m.id!=client.user.id:
                voice_client.stop()
                await voice_client.disconnect()


    client.run(token)


if __name__ == "__main__":
    main()
    