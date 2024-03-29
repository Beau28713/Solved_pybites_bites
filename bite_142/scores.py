from collections import namedtuple

MIN_SCORE = 4
DICE_VALUES = range(1, 7)

Player = namedtuple('Player', 'name scores')


def calculate_score(scores:list[int])-> int:
    """Based on a list of score ints (dice roll), calculate the
       total score only taking into account >= MIN_SCORE
       (= eyes of the dice roll).

       If one of the scores is not a valid dice roll (1-6)
       raise a ValueError.

       Returns int of the sum of the scores.
    """
    score = 0
    for ele in scores:
        if ele not in DICE_VALUES:
            raise ValueError
        elif ele < MIN_SCORE:
            continue
        else:
            score += ele
    
    return score
            



def get_winner(players: list[namedtuple])-> namedtuple:
    """Given a list of Player namedtuples return the player
       with the highest score using calculate_score.

       If the length of the scores lists of the players passed in
       don't match up raise a ValueError.

       Returns a Player namedtuple of the winner.
       You can assume there is only one winner.

       For example - input:
         Player(name='player 1', scores=[1, 3, 2, 5])
         Player(name='player 2', scores=[1, 1, 1, 1])
         Player(name='player 3', scores=[4, 5, 1, 2])

       output:
         Player(name='player 3', scores=[4, 5, 1, 2])
    """
    
    largest_score = 0
    score_length = [len(x.scores) for x in players]
    
    if not all(t == score_length[0] for t in score_length):
        raise ValueError
    
    else:
        for player in players:
            score = calculate_score(player.scores)
            if score > largest_score:
                largest_score = score
                result = (player.name, player.scores)

    return result