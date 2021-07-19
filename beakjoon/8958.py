input_count = int(input(''))
for i in range(input_count):
    score = 0
    combo = 0
    oxScore_list = list(input(''))
    for ox_list in oxScore_list:
        if ox_list == 'O':
            combo += 1
            score += combo
        elif ox_list == 'X':
            combo = 0
    print(score)

