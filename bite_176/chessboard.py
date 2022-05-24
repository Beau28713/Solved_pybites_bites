WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
   for x in range(size):
      if x % 2 == 0:
         print(" #" *(size // 2))
      else:
         print("# " *(size // 2))