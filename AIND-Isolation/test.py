#https://discussions.udacity.com/t/test-case-2-functionality-of-minimaxplayer-minimax/252984
player1 = RandomPlayer()
player2 = GreedyPlayer()
player3 = MinimaxPlayer()
player4 = MinimaxPlayer()
player5 = AlphaBetaPlayer()

game = Board(player4, player5)
game.apply_move((2, 3))
game.apply_move((0, 5))
player5.alphabeta(game,2)


game.apply_move((2, 3))
game.apply_move((0, 5))
print(game.to_string())
assert(player1 == game.active_player)
minValue(game.forecast_move((3,1)),4,0)