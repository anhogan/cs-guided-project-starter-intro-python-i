"""
List Comprehensions
"""
# creates a new list based on another list,
# in a single, readable line

# 1.
# # WITHOUT LIST COMPREHENSIONS
# sentence = "the quick brown fox jumps over the lazy dog"
# words = sentence.split()
# word_lengths = []
# for word in words:
#       if word != "the":
#           word_lengths.append(len(word))
# print(words)
# print(word_lengths)

# # WITH LIST COMPREHENSIONS
# sentence = "the quick brown fox jumps over the lazy dog"
# words = sentence.split()
# word_lengths = [len(word) for word in words if word != "the"]
# print(words)
# print(word_lengths)


"""
YOU DO
3 minute timer
"""
# Use a list comprehension to create a new list
# that has only names that start with the letter s
# and make sure all the names are properly
# capitalized in the new list.

names = ["Sarah", "jorge", "sam", "frank", "bob", "sandy", "shawn"]
sNames = [name.capitalize() for name in names if name.startswith('s') or name.startswith('S')]
print(sNames)