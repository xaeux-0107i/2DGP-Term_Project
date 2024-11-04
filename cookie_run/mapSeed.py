from object import Fence, Jelly, Olive, Fork, ForkS1, ForkS2, Poision

global max_num
max_num = 3

def create_map(n):
    map = []

    if n == 0: # 게임 시작 시 map1 초기화
        fences = [Fence(i * 100 + 50) for i in range(0, 8)]
        #fences2 = [Fence(i * 100 + 800 + 50) for i in range(0, 8)]
        # jelly1 = [Jelly(100 * i + 50) for i in range(0, 16)]
        # jelly2 = [Jelly(100 * i + 850) for i in range(0, 16)]
        # olive1 = [Olive(100 * i + 50) for i in range(0, 8)]
        # fork = [Fork(100 * i + 50) for i in range(0, 8)]
        # forkS1 = [ForkS1(100 * i + 50) for i in range(0, 8)]
        # forkS2 = [ForkS2(100 * i + 50) for i in range(0, 8)]
        # poision1 = [Poision(100 * i + 50) for i in range(0, 8)]
        map += fences
    elif n == 1:
        fences = [Fence(i * 100 + 800 + 50) for i in range(0, 8)]
        poision = [Poision(100 * i + 850) for i in range(0, 8)]
        map += fences
        map += poision
    elif n == 2:
        fences = [Fence(i * 100 + 800 + 50) for i in range(0, 8)]
        olive = [Olive(100 * 2 * i + 800 + 150) for i in range(0, 4)]
        map += fences
        map += olive
    elif n == 3:
        fences = [Fence(i * 100 + 800 + 50) for i in range(0, 8)]
        forkS2 = [ForkS2(i) for i in [1050, 1150, 1450, 1550]]
        map += fences
        map += forkS2
    elif n == 4:
        fences = [Fence(i * 100 + 800 + 50) for i in range(0, 8)]
        fork = [Fork(400 * i + 800 + 150) for i in range(0, 2)]
        forkS1 = [ForkS1(400 * i + 800 + 350) for i in range(0, 2)]
        map += fences
        map += fork
        map += forkS1

    return map
