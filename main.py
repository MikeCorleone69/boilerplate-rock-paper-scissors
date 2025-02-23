from RPS_game import play, quincy, abbey, kris, mrugesh
from RPS import player

# Try playing 1000 rounds against each bot with verbose output:
play(player, quincy, 1000, verbose=True)
play(player, abbey, 1000, verbose=True)
play(player, kris, 1000, verbose=True)
play(player, mrugesh, 1000, verbose=True)

# Uncomment this line to run the FCC test suite automatically
# from unittest import main
# main(module='test_module', exit=False)
