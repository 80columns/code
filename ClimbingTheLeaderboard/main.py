"""
https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
"""

def insertScore(current_ranked_scores, new_score):
    left_index = -1
    right_index = len(current_ranked_scores)
    mid_index = len(current_ranked_scores) // 2
    found_position = False

    while found_position is False:
        if current_ranked_scores[mid_index] == new_score:
            # don't insert, just return where in the array the matching score is
            return mid_index + 1
        elif current_ranked_scores[mid_index] > new_score:
            if mid_index == len(current_ranked_scores) - 1:
                # append the new low score at the end of the list
                current_ranked_scores.append(new_score)

                return len(current_ranked_scores)
            elif current_ranked_scores[mid_index + 1] < new_score:
                current_ranked_scores.insert(mid_index + 1, new_score)

                return mid_index + 2
            else:
                left_index = mid_index
                mid_index += (right_index - mid_index) // 2
        elif current_ranked_scores[mid_index] < new_score:
            if mid_index == 0:
                # insert the new high score at the beginning of the list
                current_ranked_scores.insert(0, new_score)

                return 1
            elif current_ranked_scores[mid_index - 1] > new_score:
                current_ranked_scores.insert(mid_index, new_score)

                return mid_index + 1
            else:
                right_index = mid_index
                mid_index -= (mid_index - left_index) // 2

def climbLeaderboard(current_ranked_scores, new_scores):
    new_score_positions = []

    # remove duplicate scores from the ranking
    current_ranked_scores_set = set(current_ranked_scores)
    current_ranked_scores = sorted(current_ranked_scores_set, reverse=True)

    # insert new scores, storing their position in the leaderboard
    for x in new_scores:
        position = insertScore(current_ranked_scores, x)
        new_score_positions.append(position)

    return new_score_positions

def main():
    # [6 4 2 1]
    print(climbLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))

    # [6 5 4 2 1]
    print(climbLeaderboard([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102]))

if __name__ == "__main__":
    main()