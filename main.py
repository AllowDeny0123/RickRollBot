import discord
import asyncio
from discord.ext import commands


voice_client = None

def main():
    with open("config.ini", "r") as config:
        token = config.read()

    client = commands.Bot(command_prefix = '/')

    @client.event
    async def on_ready():
        temp = client.voice_clients
        print(*temp)
        for cl in temp:
            print(cl)
            cl.disconnect()
        print("Готов к работе!")

    
    @client.event
    async def on_voice_state_update(m,b,a):
            if a.channel != None and m.id!=944922173745799238:
                voice_channel = a.channel
                global voice_client
                voice_client = await voice_channel.connect()
                voice_client.play(discord.FFmpegPCMAudio("1.mp3",executable="C:/ffmpeg-master-latest-win64-gpl/ffmpeg-master-latest-win64-gpl/bin/ffmpeg.exe"))
                while voice_client.is_playing():
                    await asyncio.sleep(1)
                await voice_client.disconnect()
            if a.channel == None and m.id!=944922173745799238:
                voice_client.stop()
                await voice_client.disconnect()


    client.run(token)


if __name__ == "__main__":
    main()
    