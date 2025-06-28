# print count number of open in the passage in the string.

str = 'Open source software development has transformed the technology landscape by encouraging collaboration, transparency, and innovation. Platforms like GitHub enable developers from around the world to contribute to projects, share ideas, and solve complex problems together. This collaborative approach not only accelerates progress but also helps improve code quality through peer reviews and community-driven feedback. Open source projects are accessible to anyone, allowing beginners to learn from experienced contributors and participate in real-world development. As a result, open source fosters a diverse, inclusive environment where creativity thrives and technology evolves rapidly, benefiting both individuals and organizations across the globe.'
count = 0
for i in str.lower().split():
    if i == 'open':
        count = count + 1
print(count)
