import random


def choose_options():
  options = ('piedra', 'papel', 'tijera')
  user_option = input('Piedra 🪨, Papel 📄 o Tijera ✂️ => ')
  user_option = user_option.lower()

  if not user_option in options:
    print('Esa opcion no es valida!')
    # continue
    return None, None

  computer_option = random.choice(options)

  print('User option =>', user_option)
  print('Computer option =>', computer_option)
  return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print('Empate!')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('🪨 Piedra gana a Tijera ✂️')
      print('🙋 User Gano!!')
      user_wins += 1
    else:
      print('📄 Papel gana a Piedra 🪨')
      print('Computer Gano!!')
      computer_wins += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('📄 Papel gana a Piedra 🪨')
      print('🙋 User Gano!!')
      user_wins += 1
    else:
      print('✂️ Tijera gana a Papel 📄')
      print('🤖 Computer Gano!!')
      computer_wins += 1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('✂️ Tijera gana a Papel 📄')
      print('🙋 User Gano!!')
      user_wins += 1
    else:
      print('🪨 Piedra gana a Tijera ✂️')
      print('🤖 Computer Gano!!')
      computer_wins += 1
  return user_wins, computer_wins

def run_game():
  computer_wins = 0
  user_wins = 0  
  rounds = 1
  while True:
    print('*'*25)
    print('ROUND',rounds)
    print('*'*25)

    print('Computer Points: ', computer_wins)
    print('User Points: ', user_wins)
    rounds += 1

    user_option, computer_option = choose_options()
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

    if computer_wins == 2:
      print('#'*35)
      print('¡¡¡🎖️ Ganó el Computador 🎖️!!!')
      print('#'*35)
      break

    if user_wins == 2:
      print('#'*35)
      print('¡¡¡🎖️ Ganó el User 🎖️!!!')
      print('#'*35)
      break

run_game()