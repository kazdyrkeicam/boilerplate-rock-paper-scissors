import random
from collections import defaultdict


def player(prev_play,
           opponent_history=[],
           transition_counts=defaultdict(lambda: defaultdict(int))):
    
    if prev_play:
        opponent_history.append(prev_play)
    
    if len(opponent_history) < 4:
        return random.choice(['R', 'P', 'S'])
    
    last_four_moves = tuple(opponent_history[-5:-1])
    current_move = opponent_history[-1]
    transition_counts[last_four_moves][current_move] += 1

    last_four_moves = tuple(opponent_history[-4:])
    if last_four_moves in transition_counts and transition_counts[last_four_moves]:
        next_move_prediction = max(transition_counts[last_four_moves], key=transition_counts[last_four_moves].get)
    else:
        next_move_prediction = random.choice(['R', 'P', 'S'])
    
    ideal_response = {'R': 'P', 'P': 'S', 'S': 'R'}
    return ideal_response[next_move_prediction]