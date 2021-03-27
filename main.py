
import conf
import discord

client = discord.Client()






@client.event
async def on_message(message):

    # <Message
    # id=825339039036866580 
    # channel=<TextChannel id=822806350886207542 name='флудильня' position=0 nsfw=False news=False category_id=822806350886207539> 
    # type=<MessageType.default: 0> 
    # author=<Member id=470783610241155072 name='T1mAd' discriminator='4671' bot=False nick=None guild=<Guild id=822806350886207538 name='Bots' shard_id=None chunked=False member_count=29>>
    # flags=<MessageFlags value=0>>






#Проверка на дурка №1 - Отправитель бот
    if message.author == client.user:
        return




#Проверка на дурака №2 - Отправитель чужой бот

    if message.author.bot:
        return
    #Задаем каналы для бота
    if message.channel.id == 825309073595170866:
        print(message)
        #Ответ пользователю в формате "Hello, {user.name} - your message {user.content}"
        msg = None

    # 'Hello, {message.author.name}! - your message {message.content}'
    #     await message.channel.send(msg)

    if message.content == "/hello":
        msg = f"Hello, {message.author.name}. I am {client.user.name}"
    elif message.content == "/about_me":
        msg = f"Your name is {message.author.name}, your id is {message.author.id}"
        if message.author.nick:
            msg = "and your nickname is {author.user.nick}"




# Отправляем сообщение если оно есть
    if msg != None:
        await message.channel.send(msg)


#1. /Hello - just a message
#2. /about_me - сообщение пользователя по его параметрам id/name (усли есть ник то добавить "Твой ник nick")
#3. /repeat [] - повторить за пользователем





client.run(conf.bot_token)



















# from discord_webhook import DiscordWebhook, DiscordEmbed
# import conf
# #Генерация вебхука
# webhook = DiscordWebhook(url=conf.webhook_URL)
# #Заполняем вебхук
# webhook.set_content("Hello 2")
# #Гененрируем вкладыши вебхука
# embed_0 = DiscordEmbed()
# embed_0.set_author(
#     name = "Timofey",
#     icon_url = "https://i.pinimg.com/originals/4e/40/dd/4e40ddd11beb9ba671a0b59948861afb.png"
# )
# embed_0.set_title("Title ftom T1mAd")
# embed_0.set_color("3d4cd4")
# embed_0.set_description("Коть")
# #----------------------------------------------#
# embed_1 = DiscordEmbed()
# embed_1.set_video(
#     url = "https://www.youtube.com/watch?v=t-PmaY6ivaU",
#     height = "100",
#     width = "200"
# )

# #Добавляем вкладыш
# webhook.add_embed(embed_0)
# webhook.add_embed(embed_1)
# #Отправляем вебхук
# webhook.execute()