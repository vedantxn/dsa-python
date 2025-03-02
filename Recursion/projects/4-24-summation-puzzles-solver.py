from itertools import permutations

'''
Write a program for solving summation puzzles by enumerating and testing all possible configurations. Using your program
'''

def word_to_number(word, mapping):
    """Convert a word to a number based on a given letter-digit mapping."""
    return int("".join(str(mapping[char]) for char in word))

def is_valid_solution(words, result, mapping):
    """Check if the current mapping satisfies the summation equation."""
    sum_value = sum(word_to_number(word, mapping) for word in words)
    return sum_value == word_to_number(result, mapping)

def solve_summation_puzzle(words, result):
    """Brute-force solver for summation puzzles."""
    unique_letters = set("".join(words) + result)  # Extract all unique letters
    
    if len(unique_letters) > 10:
        print("Too many unique letters for digits 0-9")
        return None
    
    for perm in permutations(range(10), len(unique_letters)):  # Try all digit assignments
        mapping = dict(zip(unique_letters, perm))  # Assign digits to letters
        if all(mapping[word[0]] != 0 for word in words + [result]):  # Leading digit check
            if is_valid_solution(words, result, mapping):
                return mapping  # Found a valid solution
    
    return None  # No solution found

# Example Puzzles (from Section 4.4.3)
puzzles = [
    (["SEND", "MORE"], "MONEY"),  # SEND + MORE = MONEY
    (["BASE", "BALL"], "GAMES"),  # BASE + BALL = GAMES
    (["FORTY", "TEN", "TEN"], "SIXTY")  # FORTY + TEN + TEN = SIXTY
]

# Solve puzzles
for words, result in puzzles:
    solution = solve_summation_puzzle(words, result)
    print(f"{words} + {result} → Solution: {solution}")
