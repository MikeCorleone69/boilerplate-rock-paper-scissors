# RPS.py

def player(prev_play, opponent_history=[]):
    """
    A Rock-Paper-Scissors strategy function that attempts to predict
    the opponent's next move using a Markov chain approach (pattern detection).

    Arguments:
    - prev_play (str): Opponent's previous move ('R', 'P', or 'S'), or '' if first move of a match.
    - opponent_history (list): Tracks the entire history of opponent's moves. Retained across calls.

    Returns:
    - (str): 'R', 'P', or 'S', indicating our move.
    """

    # Number of previous moves to use in the pattern (you can adjust 3 -> 2 or 4, etc.)
    pattern_length = 3

    # This dict will map a string of length `pattern_length` to a dict of move counts,
    # e.g., pattern_counts["RPS"] = {"R": 5, "P": 3, "S": 2}
    # meaning: after "RPS", the opponent played R 5 times, P 3 times, S 2 times.
    # We store it in a default argument so it persists between calls:
    if not hasattr(player, "pattern_counts"):
        player.pattern_counts = {}

    # If prev_play == "", it signals a new match is starting
    # so we should reset everything:
    if prev_play == "":
        opponent_history.clear()
        player.pattern_counts.clear()

    # Helper function: returns the move that beats the input
    def beat_move(move):
        if move == "R":
            return "P"
        elif move == "P":
            return "S"
        else:  # move == "S"
            return "R"

    # Update opponent_history
    if prev_play:
        opponent_history.append(prev_play)

    # If not enough history yet, just throw out "R" (or any move):
    if len(opponent_history) < pattern_length:
        return "R"

    # Build the key for the last 'pattern_length' moves in opponent_history
    recent_sequence = "".join(opponent_history[-pattern_length:])

    # --- Update pattern_counts from the entire known history --- #
    # For each index in opponent_history where a full pattern (length=pattern_length+1) is possible:
    # We build the substring of length `pattern_length` and then increment the count of what followed it.
    player.pattern_counts.clear()
    for i in range(len(opponent_history) - pattern_length):
        seq = "".join(opponent_history[i : i + pattern_length])
        next_move = opponent_history[i + pattern_length]
        if seq not in player.pattern_counts:
            player.pattern_counts[seq] = {"R": 0, "P": 0, "S": 0}
        player.pattern_counts[seq][next_move] += 1
    # ---------------------------------------------------------- #

    # Predict the opponent's next move by looking at how they've continued from 'recent_sequence'
    if recent_sequence in player.pattern_counts:
        # pick the next move that occurs most frequently
        next_move_stats = player.pattern_counts[recent_sequence]
        predicted_move = max(next_move_stats, key=next_move_stats.get)
    else:
        # fallback if we have no info about this sequence
        predicted_move = "R"

    # We play the move that beats the predicted move
    return beat_move(predicted_move)
