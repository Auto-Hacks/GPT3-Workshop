import os
import discord
import openai

TOKEN = os.getenv('DISCORD_TOKEN')
openai.api_key = os.getenv("OPENAI_API_KEY")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print(message.content)
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=f"Classify each text message into a Question, or not a question.\nMessage: Are you free today\nClassification: Question\nMessage: Im not feeling well today\nClassification: Not a question\nMessage: {message.content}\nClassification:",
      temperature=0,
      max_tokens=256,
      top_p=0,
      frequency_penalty=0,
      presence_penalty=0,
      stop=["\\n"]
    )
    classification = response.choices[0].text
    print(classification)
    if classification != " Question":
        return
    prompt=f"Marv is a rude and unhelpful person that answers questions with sarcastic responses. Below is a conversation between a character in a movie and Marv.\nYou: How are you doing?\nMarv: How you are not\nYou: What does HTML stand for? \nMarv: What CSS doesn't stand for\nYou: When did the first airplane fly? \nMarv: When the first helicopter didn't\nYou: What is the meaning of life? \nMarv: What the meaning of pigeon isn't\nYou: Who is Captain America?\nMarv: Who Iron Man isn't\nYou: {message.content}\nMarv:",
    response = openai.Completion.create(
      model="text-davinci-003",
      temperature=1,
      max_tokens=256,
      prompt=prompt,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
      stop=["\\n"]
    )
    reply = response.choices[0].text[1:]
    await message.reply(reply)


client.run(TOKEN)
