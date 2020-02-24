import auth
import tweepy

bot1 = auth.main()


def main():
  op = input("id or user")
  friends = tweepy.Cursor(bot1.followers, id="csdotmaia")
  ids = []
  count = 0
  max_followers = [0, 0]
  for friend in friends.items():
    location = friend.location.split(',')
    locationh = friend.location.split(' - ')
    count += 1
    if location[0] == "pvai" or location[0] == 'Paranavaí'or locationh[0] == "Paranavaí - PR": 
      if friend.followers_count >= max_followers[1]:
        max_followers[0] = friend.id
        max_followers[1] = friend.followers_count
        print("mais seguidores é do usuario abaixo [{}]; {} seguidores".format(max_followers[0], max_followers[1]))
      print("{}({}) em {} seguidores: {}".format(friend.name, friend.id, friend.location, friend.followers_count))
      ids.append(id)
      print("")
  print("")
  print("{} ids encontrados em Paranavai de {} seguidores.".format(len(ids), count))
  a = input("Seguir?")

  #   for id in ids:
  #     bot1.create_friendship(id=id)

  # for i in results:
  #   user = bot1.get_user(i)
  #   print(location)

  print("O proximo usuario seria, em teoria o usuario de id {} com {} seguidores.".format(max_followers[0]), max_followers[1])


main()