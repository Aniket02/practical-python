# bounce.py
#
# Exercise 1.5
height = 100.0
bounce_factor = 0.6
for i in range(1, 11):
    new_height = height * 0.6
    print(f'{i} {round(new_height, 4)}')
    height = new_height