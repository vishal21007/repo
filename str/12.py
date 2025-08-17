# input string user and print each word in reverse. String should be printed as formated.
# input : hello world
# Output : olleh dlrow

str = 'input string user and print each word in reverse. String should be printed as formated'

for words in str.split() :
    print(words[::-1], end=' ')