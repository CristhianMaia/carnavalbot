import auth
import threading, time
import datetime
from random import randrange

api = auth.main()

def bot():
  dtnow = datetime.datetime.now()

  print("")
  print(carnaval)
  print(carnaval_rio)
  print(dtnow)

  daysleft = str((carnaval - dtnow).days+1)
  daysleft_rio = str((carnaval_rio - dtnow).days+1)

  final = ''
  for n in range(len(daysleft)):
    number = int(daysleft[n])
    final += str(number_emoji[number])

  final_rio = ''
  for n in range(len(daysleft_rio)):
    number = int(daysleft_rio[n])
    final_rio += str(number_emoji[number])

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
  texto_rio = "E {} dias para os 50 dias de carnaval no RJ.".format(final_rio)
  print(texto_rio)
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

def main():
  while True:
    date_now = datetime.datetime.now()
    next_post = datetime.datetime.now().replace(hour=9, minute=0, second=0, microsecond=0)
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
    time.sleep(diferenca+5)
    print("Irá Postar")
    print(datetime.datetime.now())
    print("")
    print("----------------------------")
    bot()
 
number_emoji = ['0️⃣', '1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣']
emoji = [['💃', '🌈', '🎆'], ['🎉', '🎉🎊'], ['🎭']]
carnaval = datetime.datetime(2020,2,21)
carnaval_rio = datetime.datetime(2020,1,12)
qtd = 0
main()
