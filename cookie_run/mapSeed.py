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
        jelly = [Jelly(100 * i + 800 + 50) for i in range(0, 8)]
        map += fences
        map += poision
        map += jelly
    elif n == 2:
        fences = [Fence(i * 100 + 800 + 50) for i in range(0, 8)]
        olive = [Olive(i) for i in [850, 1050, 1450]]
        forkS2 = [ForkS2(i) for i in [1250]]
        map += fences
        map += olive
        map += forkS2
    elif n == 3:
        fences = [Fence(i * 100 + 800 + 50) for i in range(0, 8)]
        forkS2 = [ForkS2(i) for i in [1050, 1150, 1450, 1550]]
        map += fences
        map += forkS2
    elif n == 4:
        fences = [Fence(i * 100 + 800 + 50) for i in range(0, 8)]
        fork = [Fork(400 * i + 800 + 150) for i in range(0, 1)]
        forkS1 = [ForkS1(400* i + 800 + 350) for i in range(0, 1)]
        forkS2 = [ForkS2(1400)]
        map += fences
        map += fork
        map += forkS1
        map += forkS2
    elif n == 5:
        fences = [Fence(i * 100 + 800 + 50) for i in range(0, 8)]
        map += fences
        olive = [Olive(400 * i + 800 + 250) for i in range(0, 2)]
        forkS1 = [ForkS1(400 * i + 800 + 350) for i in range(0,2)]
        map += forkS1
        map += olive

    return map
