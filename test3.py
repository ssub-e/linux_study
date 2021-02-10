import random
comp = []
play = []
result = []
n = 0
count = [[[0, 0], [0, 0]], [[0, 0], [0, 0]]]
while n < 100:
    # computer #
    if n > 3:
        com = count[play[-2]][play[-1]].index(min(count[play[-2]][play[-1]]))
        if count[play[-2]][play[-1]][0] == count[play[-2]][play[-1]][1]:
            com = random.randint(0, 1)
    else:
        com = random.randint(0, 1)
    comp.append(com)
    # player #
    while True:
        try:
            player = int(input('0 or 1 ?'))
            if int(player) in [0, 1]:
                play.append(int(player))
                if player == com:
                    result.append('w')
                else:
                    result.append('l')
                if n > 1:
                    count[play[-2]][play[-1]][player] += 1
                n += 1
                print('결과 :', result[-1])
                print('승률 :', 1-(result.count('w')/len(result)))
                break
        except:
            pass
print(comp, '\n', play, '\n', result, '\n', count)
print('승률', result.count('l')/len(result))
