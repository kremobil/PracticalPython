gird = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', '0', '0', '.', '.', '.'],
    ['0', '0', '0', '0', '.', '.'],
    ['0', '0', '0', '0', '0', '.'],
    ['.', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '.'],
    ['0', '0', '0', '0', '.', '.'],
    ['.', '0', '0', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
]

def draw_gird(gird):
    result = ''
    for i in range(len(gird[0])):
        row = [character[i] for character in gird]
        result += ''.join(row)
        result += '\n'
    return result

print(draw_gird(gird))