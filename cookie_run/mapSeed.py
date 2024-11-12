from object import Fence, Jelly, Olive, Fork, ForkS1, ForkS2, Poision

global max_num
max_num = 5

def create_map(n):
    map = []

    if n == 0: # 게임 시작 시 map1 초기화
        fences = [Fence(i * 100 + 50) for i in range(0, 8)]
        map += fences
    elif n == 1:
        fences = [Fence(i * 100 + 800 + 50) for i in range(0, 8)]
        poision = [Poision(x + 850, y) for x, y in [(200, 200), (400, 300), (500,300), (700, 120)]]
        jelly = [Jelly(100 * i + 800 + 50, j) for i, j in [(0, 120), (1,120), (2,120), (3, 135),
                                                           (4, 150), (5, 150), (6, 170), (7, 200)]]
        map += fences
        map += poision
        map += jelly
    elif n == 2:
        fences = [Fence(i * 100 + 800 + 50) for i in range(0, 8)]
        olive = [Olive(i) for i in [850, 1050, 1450]]
        forkS2 = [ForkS2(i) for i in [1250]]
        jelly = [Jelly(100 * i + 800 + 50, j) for i, j in [(0, 200), (1, 120), (2, 200), (3, 120),
                                                           (4, 110), (5, 120), (6, 200), (7, 120)]]
        map += fences
        map += olive
        map += forkS2
        map += jelly
    elif n == 3:
        fences = [Fence(i * 100 + 800 + 50) for i in range(0, 8)]
        forkS2 = [ForkS2(i) for i in [950, 1050, 1350, 1450]]
        jelly = [Jelly(100 * i + 800 + 50, j) for i, j in [(0, 150), (1, 110), (2, 110), (3, 150),
                                                           (4, 150), (5, 110), (6, 110), (7, 150)]]
        map += fences
        map += forkS2
        map += jelly
    elif n == 4:
        fences = [Fence(i * 100 + 800 + 50) for i in range(0, 8)]
        fork = [Fork(400 * i + 800 + 150) for i in range(0, 1)]
        forkS1 = [ForkS1(400* i + 800 + 350) for i in range(0, 1)]
        forkS2 = [ForkS2(1400)]
        jelly = [Jelly(100 * i + 800 + 50, j) for i, j in [(0, 120), (1, 200), (2, 250), (3, 300),
                                                           (4, 200), (5, 110), (6, 110), (7, 110)]]
        map += fences
        map += fork
        map += forkS1
        map += forkS2
        map += jelly
    elif n == 5:
        fences = [Fence(i * 100 + 800 + 50) for i in range(0, 8)]
        map += fences
        olive = [Olive(400 * i + 800 + 250) for i in range(0, 2)]
        forkS1 = [ForkS1(400 * i + 800 + 350) for i in range(0,2)]
        map += forkS1
        map += olive

    return map
