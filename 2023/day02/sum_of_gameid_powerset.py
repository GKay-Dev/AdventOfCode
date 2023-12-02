# https://adventofcode.com/2023/day/2

with open("input.txt") as f:
    data = f.read().strip()

id_sum = 0
power_set_sum = 0

for line in data.split("\n"):

    games = line.split(':')
    game_id = games[0].split()[-1]
    game_play = games[1].split(';')
    min_red, min_green, min_blue = 0, 0, 0   # Min no of cubes that needs to be loaded in the bag

    for game in game_play:
        red, green, blue = 12, 13, 14    # No of cubes loaded in the bag
        flag = True
        game = game.split(',')

        for color in game:
            color = color.split()
            if color[-1] == 'red':
                if int(color[0]) > min_red:
                    min_red = int(color[0])
                red -= int(color[0])
                if red < 0:
                    flag = False
                    # error_color = 'red'
                    # break
            elif color[-1] == 'green':
                green -= int(color[0])
                if int(color[0]) > min_green:
                    min_green = int(color[0])
                if green < 0:
                    flag = False
                    # error_color = 'green'
                    # break
            else:
                if int(color[0]) > min_blue:
                    min_blue = int(color[0])
                blue -= int(color[0])
                if blue < 0:
                    flag = False
                    # error_color = 'blue'
                    # break
        
        # if flag:
        #     flag = False
        #     print(game_id, error_color)
        #     break
        # else:
        #     flag = True

        power_set = min_red * min_green * min_blue
        # print(game_id, min_red, min_green, min_blue, power_set)
                
    if flag:
        id_sum += int(game_id)
        # print(game_id,id_sum)
    
    power_set_sum += power_set
    # print(game_id, power_set_sum)

print("1.", id_sum)
    
print("2.", power_set_sum)

