### Rock Paper Scissors

## Input params
# First column
# A = Rock
# B = Scissors
# C = Home

# Second column
# x - Rock
# y - Scissors
# z - Paper

## Scoring
# total score is sum of scores for each round
# single round score is score of shape (R=1, P=2, S=3), plus outcome (0 for loss, 3 for draw, 6 for win)

def readInput():
    all_rounds = []
    with open('day2Input.txt') as f:
        lines = f.readlines()
        for line in lines:
            round_moves = []
            split_line = line.strip('\n').split(' ')
            for move in split_line:
                if move =='A':
                    round_moves.append('R')
                elif move == 'B':
                    round_moves.append('P')
                elif move == 'C':
                    round_moves.append('S')
                else:
                    round_moves.append(move)
            all_rounds.append(round_moves)
    return all_rounds

def get_round_score(opponentMove, ourMove):
    throw_scores = {'R': 1, 'P': 2, 'S':3}
    round_score = 0

    if opponentMove == ourMove:
        round_score = 3
    elif opponentMove == 'R':
        if ourMove == 'S':
            round_score = 0 
        elif ourMove == 'P': 
            round_score = 6
    elif opponentMove == 'S':
        if ourMove == 'R':
            round_score = 6
        elif ourMove == 'P':
            round_score = 0
    elif opponentMove == 'P':
        if ourMove == 'R':
            round_score = 0
        elif ourMove == 'S': 
            round_score = 6
    return round_score + throw_scores[ourMove]

def get_round_score_2(opponentMove, ourMove):
    throw_scores = {'R': 1, 'P': 2, 'S': 3}

    if ourMove == 'X':
        # need to lose
        if opponentMove == 'R':
            return throw_scores['S'] + 0
        elif opponentMove == 'S':
            return throw_scores['P'] + 0
        elif opponentMove == 'P':
            return throw_scores['R'] + 0
    elif ourMove == 'Y':
        # need to draw
        return throw_scores[opponentMove] + 3
    elif ourMove == 'Z':
        # need to win
        if opponentMove == 'R':
            return throw_scores['P'] + 6
        elif opponentMove == 'S':
            return throw_scores['R'] + 6
        elif opponentMove == 'P':
            return throw_scores['S'] + 6

if __name__ == "__main__":
    total_score = 0
    all_round_moves = readInput()
    # print(all_round_moves)
    ## iterate through all rounds and calculate scores'
    for r in all_round_moves:
        round_score = get_round_score_2(r[0], r[1])
        total_score = total_score + round_score
    print("total score:", total_score)
