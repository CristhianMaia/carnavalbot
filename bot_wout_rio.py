import tweepy
import threading, time
import datetime
from random import randrange

auth = tweepy.OAuthHandler("wGICCGqGvMx1ly1eJ77KKQl96", "XhwmaXE3C0MkMyv681vIhabXtL5WPzRLMVZrihyRejKsgylluX")
auth.set_access_token("1211319258103156737-uxvnb3DNqR0ZB6Cd615mSV7lugFtLN", "SMx8PBA7zuyIonQeJtymX52mzvlW5pkFU7fRnIRawHXRE")

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)


def bot():
  dtnow = datetime.datetime.now()

  print("")
  print(carnaval)
  print(dtnow)

  daysleft = str((carnaval - dtnow).days+1)

  final = ''
  for n in range(len(daysleft)):
    number = int(daysleft[n])
    final += str(number_emoji[number])

  emojis = ''
  for n in range(3):
    random = randrange(4)
    try:
      emojis += emoji[n][random]
    except IndexError:
      emojis = emojis

  if emojis == "":
    print("vazio")
    emojis = emoji[1][1]

  texto = "Faltam {} dias para o carnaval de 2020! {}".format(final, emojis)

  print(texto)
  try:
    print("postando no try")
    api.update_status(status=texto)
  finally:
    last_post = dtnow
    print("Postou! no horario:")
    print(last_post)
    print("")
    print("------------------------------FIM------------------------------")
    time.sleep(20)

def inicial():
  while True:
    date_now = datetime.datetime.now()
    next_post = datetime.datetime.now().replace(hour=9, minute=6, second=0, microsecond=0)
    if date_now>next_post:
      next_post += datetime.timedelta(days=1)

    diferenca = (next_post - date_now).seconds
    print("------------------------------INICIO------------------------------")
    global qtd
    qtd += 1
    print("Execução nº")
    print(qtd)
    print("")
    print("----------------------------")
    print("Horario atual do bot")
    print(date_now)
    print("")
    print("Proximo post")
    print(next_post)
    print("")
    print("Diferença para setar o sleep")
    print(diferenca)
    print("")
    print("----------------------------")
    print("Sleep Setado")
    print(datetime.datetime.now())
    time.sleep(diferenca)
    print("Irá Postar")
    print(datetime.datetime.now())
    print("")
    print("----------------------------")
    bot()
 
number_emoji = ['0️⃣', '1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣']
emoji = [['💃', '🌈', '🎆'], ['🎉', '🎉🎊'], ['🎭']]
carnaval = datetime.datetime(2020,2,21)
qtd = 0
inicial()
