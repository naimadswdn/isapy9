# Number of level is linear function of # amount
# i   #
# 0   1
# 1   3
# 2   5
# 3   7
#
# y=ax+b
# i=1/2#-1/2
# #=2i+1


def pyramid_draw():
    """Script to draw a pyramid consist of #, witch given height."""
    while True:
        height = input('Please provide height of the pyramid: ')
        try:
            height = int(height)
            break
        except:
            print('Please provide integer number!')
            continue

    width = 2 * height + 1

    for i in range(height):
        a = 2 * i + 1
        line = '#'*a
        print(line.center(width))


pyramid_draw()
