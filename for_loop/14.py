n = 4  # Number of rows for the upper part

# Upper part
for i in range(1, n + 1):
    print(' ' * (n - i + 1) + '* ' * i)

# Lower part
for i in range(n - 1, 0, -1):
    print(' ' * (n - i + 1) + '* ' * i)