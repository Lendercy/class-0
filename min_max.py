# Function to get 10 test scores from the user
def get_scores():
    scores = []
    for i in range(5):
        score = float(input(f"Enter score {i+1}: "))
        scores.append(score)
    return scores

# Function to print the highest and lowest scores
def print_highest_lowest(scores):
    print(f"Highest score: {max(scores)}")
    print(f"Lowest score: {min(scores)}")

# Function to print the average of the scores
def print_average(scores):
    average = sum(scores) / len(scores)
    print(f"Average score: {average}")

# Function to print the second largest score
def print_second_largest(scores):
    unique_scores = list(set(scores))
    unique_scores.sort(reverse=True)
    if len(unique_scores) > 1:
        print(f"Second largest score: {unique_scores[1]}")
    else:
        print("Not enough unique scores to determine the second largest.")

# Function to check for scores greater than 100
def check_scores_over_100(scores):
    if any(score > 100 for score in scores):
        print("Warning: A value over 100 has been entered.")

# Function to drop the two lowest scores and print the average of the rest
def drop_two_lowest_and_average(scores):
    sorted_scores = sorted(scores)
    remaining_scores = sorted_scores[2:]
    average = sum(remaining_scores) / len(remaining_scores)
    print(f"Average after dropping the two lowest scores: {average}")

# Main function to execute the tasks
def main():
    scores = get_scores()
    print_highest_lowest(scores)
    print_average(scores)
    print_second_largest(scores)
    check_scores_over_100(scores)
    drop_two_lowest_and_average(scores)

if __name__ == "__main__":
    main()
