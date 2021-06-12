# This entrypoint file to be used in development. Start by reading README.md
from RPS_game import play, mrugesh, abbey, quincy, kris, human, random_player
from RPS import player
from unittest import main

#play(player, quincy, 10)
#play(player, abbey, 100, verbose = True)
#play(player, kris, 10, verbose = True)
# play(player, mrugesh, 100, verbose = True)

# Uncomment line below to play interactively against a bot:
#play(player, abbey, 1000, verbose=True)

# Uncomment line below to play against a bot that plays randomly:
#play(human, abbey, 1000, verbose = True)



# Uncomment line below to run unit tests automatically
main(module='test_module', exit=False)