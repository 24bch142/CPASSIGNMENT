string = "programming"

char_freq = {char: string.count(char) for char in set(string)}

print("Character Frequency:", char_freq)
