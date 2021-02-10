import random
c=''
num=[str(i) for i in range(1,10)]
while len(c)<3:
    c+=num.pop(random.randrange(0,len(num)))

num=[str(i) for i in range(1,10)]
n=0
while n<10:
    print('Round', n+1)
    while True:
        p=input('숫자를 입력해주세요 : ')
        try:
            if len(set(p))==3 and (123<=int(p)<=987):
                break
        except:
            pass
    s, b = 0, 0
    for pp in p:
        for cc in c:
            if pp==cc:
                if p.index(pp) == c.index(cc):
                    s+=1
                    break
                else:
                    b+=1
                    break
    if s==3:
        print('정답입니다.')
        break
    print('p : ' + p)
    print('s : ' + str(s) + ' b : ' + str(b))
    # print('c :', c, '\n')
    n+=1

print('정답 : ' + c)
