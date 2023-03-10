import random


def choose_options():
  options = ('piedra', 'papel', 'tijera')
  user_option = input('Piedra πͺ¨, Papel π o Tijera βοΈ => ')
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
      print('πͺ¨ Piedra gana a Tijera βοΈ')
      print('π User Gano!!')
      user_wins += 1
    else:
      print('π Papel gana a Piedra πͺ¨')
      print('Computer Gano!!')
      computer_wins += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('π Papel gana a Piedra πͺ¨')
      print('π User Gano!!')
      user_wins += 1
    else:
      print('βοΈ Tijera gana a Papel π')
      print('π€ Computer Gano!!')
      computer_wins += 1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('βοΈ Tijera gana a Papel π')
      print('π User Gano!!')
      user_wins += 1
    else:
      print('πͺ¨ Piedra gana a Tijera βοΈ')
      print('π€ Computer Gano!!')
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
      print('Β‘Β‘Β‘ποΈ GanΓ³ el Computador ποΈ!!!')
      print('#'*35)
      break

    if user_wins == 2:
      print('#'*35)
      print('Β‘Β‘Β‘ποΈ GanΓ³ el User ποΈ!!!')
      print('#'*35)
      break

run_game()