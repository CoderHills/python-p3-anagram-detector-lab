# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # normalize to lowercase for case-insensitive matching

    def match(self, candidates):
        matches = []
        # Sort letters of the target word once for efficiency
        sorted_word = sorted(self.word)

        for candidate in candidates:
            # Compare lowercase versions to ignore case
            if candidate.lower() != self.word and sorted(candidate.lower()) == sorted_word:
                matches.append(candidate)

        return matches
