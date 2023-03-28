import random
from replit import clear

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
def logo():
  print("███████  ██████  ██████   ██████  █████  ")
  print("██      ██    ██ ██   ██ ██      ██   ██ ")
  print("█████   ██    ██ ██████  ██      ███████ ")
  print("██      ██    ██ ██   ██ ██      ██   ██ ")
  print("██       ██████  ██   ██  ██████ ██   ██ ")

logo()
print("Descubra o animal em inglês!")

animal_list = ['aardvark', 'alligator', 'alpaca', 'anaconda', 'ant', 'anteater', 'antelope', 'ape', 'armadillo', 'baboon', 'badger', 'bat', 
'beagle', 'bear', 'beaver', 'bee', 'beetle', 'bison', 'blackbird', 'boa', 'boar', 'bobcat', 'buffalo', 'butterfly', 'camel', 'canary', 'capybara', 'caribou', 'cat', 'caterpillar', 'chameleon', 'cheetah', 'chicken', 'chimpanzee', 'chinchilla', 'chipmunk', 'cobra', 'cockroach', 'cod', 'condor', 'cougar', 'cow', 'coyote', 'crab', 'crane', 'cricket', 'crocodile', 'crow', 'deer', 'dingo', 'dolphin', 'donkey', 'dove', 'dragon', 'dragonfly', 'duck', 'eagle', 'eel', 'elephant', 'elk', 'emu', 'falcon', 'ferret', 'finch', 'fish', 'flamingo', 'flea', 'fly', 'fox', 'frog', 'gazelle', 'gecko', 'gerbil', 'gibbon', 'giraffe', 'goat', 'goose', 'gorilla', 'grasshopper', 'greyhound', 'grizzly', 'hamster', 'hare', 'hawk', 'hedgehog', 'heron', 'hippopotamus', 'hornet', 'horse', 'hound', 'hyena', 'ibex', 'iguana', 'impala', 'jackal', 'jaguar', 'jellyfish', 'kangaroo', 'koala', 'kookaburra', 'ladybird', 'lark', 'lemming', 'lemur', 'leopard', 'lion', 'lizard', 'llama', 'lobster', 'locust', 'loris', 'louse', 'lynx', 'macaw', 'magpie', 'mallard', 'mammoth', 'manatee', 'mandrill', 'marten', 'meerkat', 'mink', 'mole', 'mongoose', 'monkey', 'moose', 'mosquito', 'mouse', 'mule', 'muskrat', 'narwhal', 'newt', 'nightingale', 'octopus', 'okapi', 'opossum', 'orangutan', 'orca', 'ostrich', 'otter', 'owl', 'ox', 'oyster', 'panther', 'parakeet', 'parrot', 'partridge', 'peacock', 'pelican', 'penguin', 'pheasant', 'pig', 'pigeon', 'platypus', 'pony', 'porcupine', 'possum', 'puma', 'python', 'quail', 'rabbit', 'raccoon', 'ram', 'rat', 'raven', 'reindeer', 'rhinoceros', 'robin', 'rooster', 'salamander', 'salmon', 'sandpiper', 'sardine', 'scorpion', 'seagull', 'seahorse', 'seal', 'shark', 'sheep', 'shrew', 'skunk', 'sloth', 'slug', 'smelt', 'snail', 'snake', 'snipe', 'sole', 'sparrow', 'spider', 'spiny anteater', 'sponge', 'squid', 'squirrel', 'starfish', 'stingray', 'stinkbug', 'stork', 'swallow', 'swan', 'swordfish', 'tadpole', 'tarantula', 'tarsier', 'termite', 'tiger', 'toucan', 'trout', 'tuna', 'turkey', 'turtle', 'vulture', 'walrus', 'wasp', 'weasel', 'whale', 'whippet', 'whitefish', 'wildcat', 'wolf', 'wolverine', 'wombat', 'woodpecker', 'worm', 'wren', 'yak', 'yellow perch', 'zebra']

# Escolhe um palavra aleatória da lista de animais.
chosen_word = random.choice(animal_list)
chosen_word_answer = chosen_word.capitalize()

display = []
word_lenght = len(chosen_word)

for _ in range(len(chosen_word)):
    display += "_"
print(stages[6])
print(display)

end_of_game = False
lives = 6

# Looping do jogo, enquanto a condição end_of_game for falsa, o jogo continua rodando.
while not end_of_game:
    guess = input("Advinhe uma letra: ").lower()

    clear()

    # Verificar a letra escolhida
    # Se a letra estiver certa a "_" no display é substituida pela letra
    for position in range(word_lenght):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Caso a letra não for correta, o jogador perde uma vida
    if guess not in chosen_word:
        lives -= 1

    # Os estagios do boneco são contados a partir das vidas restantes
    print(stages[lives])      

    # O display atualizado com as letra é printado na tela.
    print(display)

    # Número de vidas chega a zero, jogo acaba.
    if lives == 0:
        print("Você perdeu!")
        print(f"A palavra era {chosen_word_answer}")
        end_of_game = True

    # Quando não houver mais "_" no display, significa que o jogador venceu.
    if "_" not in display:
        end_of_game = True
        print("Você venceu!")
        print(f"A palavra era {chosen_word_answer}")
