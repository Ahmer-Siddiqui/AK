def apply_heuristic(graph, opt1, opt2, goodscore, badScore):
    for key, value in graph.items():
        if len(value) < 2:
            print(f"Skipping {key} because it doesn't have two options: {value}")
            continue
        print(f"For {key}, choose between:")
        print(f"1: {opt1}")
        print(f"2: {opt2}")

        while True:
            choice = input("Select 1 or 2: ").strip()
            if choice in ['1', '2']:
                break
            print("Invalid input. Please enter 1 or 2.")

        chosen_value = value[0] if choice == '1' else value[1]
        max_value = max(value[0], value[1])
        min_value = min(value[0], value[1])

        if chosen_value == max_value:
            goodscore += 1
            print("Good choice! +1 to goodscore.")
        elif chosen_value == min_value:
            badScore -= 1
            print("Bad choice! -1 to badScore.")
        print(f"Current Scores: goodscore={goodscore}, badScore={badScore}\n")

    print("Final Scores:")
    print(f"goodscore = {goodscore}")
    print(f"badScore = {badScore}")

    return goodscore, badScore

graph = {
    'A': [5, 21], 'B': [13, 23], 'C': [10, 3], 'D': [24, 8],
    'E': [7, 1], 'F': [], 'G': [9], 'H': [7, 8], 'I': [15, 3], 'J': [5, 12],
}

opt1 = "Option 1"
opt2 = "Option 2"
goodScore = 0
badScore = 0

apply_heuristic(graph, opt1, opt2, goodScore, badScore)