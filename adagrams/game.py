from random import randint

def draw_letters():
    # Letter distribution as per the provided table
    LETTER_DISTRIBUTION = {
        'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1, 'K': 1,
        'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4, 'V': 2,
        'W': 2, 'X': 1, 'Y': 2, 'Z': 1
    }

    # Create a pool of letters based on their frequency
    LETTER_POOL = []
    for letter, count in LETTER_DISTRIBUTION.items():
        LETTER_POOL.extend([letter] * count)
    """Draws 10 random letters from the letter pool."""
    hand = []
    for _ in range(10):
        index = randint(0, len(LETTER_POOL) - 1)  # Random index within the pool
        hand.append(LETTER_POOL[index])  # Pick the letter at the random index
    return hand

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass