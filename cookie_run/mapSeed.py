from object import Fence, Jelly, Olive, Fork, ForkS1, ForkS2, Poision
from item import Energy
import game_world

global max_num
max_num = 5

def create_map(n, depth):

    if n == 0: # 게임 시작 시 map1 초기화
        fences = [Fence(i * 100 + 50) for i in range(0, 8)]
        game_world.add_objects(fences, depth)
    elif n == 1:
        fences = [Fence(i * 100 + 800 + 50) for i in range(0, 8)]
        poisions = [Poision(x + 850, y) for x, y in [(200, 200), (400, 300), (500,300), (700, 120)]]
        jellys = [Jelly(100 * i + 800 + 50, j) for i, j in [(0, 120), (1,120), (2,120), (3, 135),
                                                           (4, 150), (5, 150), (6, 170), (7, 200)]]
        game_world.add_objects(fences, depth)
        game_world.add_objects(poisions, depth)
        for poison in poisions:
            game_world.add_collision_pairs('cookie:obstacle', None, poison)
        game_world.add_objects(jellys, depth)
        for jelly in jellys:
            game_world.add_collision_pairs('cookie:jelly', None, jelly)
    elif n == 2:
        fences = [Fence(i * 100 + 800 + 50) for i in range(0, 8)]
        olives = [Olive(i) for i in [850, 1050, 1450]]
        forkS2s = [ForkS2(i) for i in [1250]]
        jellys = [Jelly(100 * i + 800 + 50, j) for i, j in [(0, 200), (1, 120), (2, 200), (3, 120),
                                                           (4, 110), (5, 120), (6, 200), (7, 120)]]
        game_world.add_objects(fences, depth)
        game_world.add_objects(olives, depth)
        game_world.add_objects(forkS2s, depth)
        game_world.add_objects(jellys, depth)

        for olive in olives:
            game_world.add_collision_pairs('cookie:obstacle', None, olive)
        for forkS2 in forkS2s:
            game_world.add_collision_pairs('cookie:obstacle', None, forkS2)
        for jelly in jellys:
            game_world.add_collision_pairs('cookie:jelly', None, jelly)
    elif n == 3:
        fences = [Fence(i * 100 + 800 + 50) for i in range(0, 8)]
        forkS2s = [ForkS2(i) for i in [950, 1050, 1350, 1450]]
        jellys = [Jelly(100 * i + 800 + 50, j) for i, j in [(0, 150), (1, 110), (2, 110), (3, 150),
                                                           (4, 150), (5, 110), (6, 110), (7, 150)]]
        game_world.add_objects(fences, depth)
        game_world.add_objects(forkS2s, depth)
        game_world.add_objects(jellys, depth)

        for forkS2 in forkS2s:
            game_world.add_collision_pairs('cookie:obstacle', None, forkS2)
        for jelly in jellys:
            game_world.add_collision_pairs('cookie:jelly', None, jelly)
    elif n == 4:
        fences = [Fence(i * 100 + 800 + 50) for i in range(0, 8)]
        forks = [Fork(400 * i + 800 + 150) for i in range(0, 1)]
        forkS1s = [ForkS1(400* i + 800 + 350) for i in range(0, 1)]
        forkS2s = [ForkS2(1400)]
        jellys = [Jelly(100 * i + 800 + 50, j) for i, j in [(0, 120), (1, 200), (2, 250), (3, 300),
                                                           (4, 200), (5, 110), (6, 110), (7, 110)]]
        game_world.add_objects(fences, depth)
        game_world.add_objects(forks, depth)
        game_world.add_objects(forkS1s, depth)
        game_world.add_objects(forkS2s, depth)
        game_world.add_objects(jellys, depth)

        for fork in forks:
            game_world.add_collision_pairs('cookie:obstacle', None, fork)
        for forkS1 in forkS1s:
            game_world.add_collision_pairs('cookie:obstacle', None, forkS1)
        for forkS2 in forkS2s:
            game_world.add_collision_pairs('cookie:obstacle', None, forkS2)
        for jelly in jellys:
            game_world.add_collision_pairs('cookie:jelly', None, jelly)
    elif n == 5:
        fences = [Fence(i * 100 + 800 + 50) for i in range(0, 8)]
        olives = [Olive(400 * i + 800 + 150) for i in range(0, 2)]
        forkS1s = [ForkS1(400 * i + 800 + 250) for i in range(0,2)]
        jellys = [Jelly(100 * i + 800 + 50, j) for i, j in [(0, 120), (1, 200), (2, 300), (3, 200),
                                                           (4, 120), (5, 200), (6, 300), (7, 200)]]
        game_world.add_objects(fences, depth)
        game_world.add_objects(forkS1s, depth)
        game_world.add_objects(olives, depth)
        game_world.add_objects(jellys, depth)

        for olive in olives:
            game_world.add_collision_pairs('cookie:obstacle', None, olive)
        for forkS1 in forkS1s:
            game_world.add_collision_pairs('cookie:obstacle', None, forkS1)
        for jelly in jellys:
            game_world.add_collision_pairs('cookie:jelly', None, jelly)

def create_energy_map(n, depth):

    if n == 0: # 게임 시작 시 map1 초기화
        energy = Energy(1200, 300)
        fences = [Fence(i * 100 + 800 + 50) for i in range(0, 8)]
        game_world.add_objects(fences, depth)
        game_world.add_object(energy, depth)
        game_world.add_collision_pairs('cookie:energy', None, energy)
    elif n == 1:
        fences = [Fence(i * 100 + 800 + 50) for i in range(0, 8)]
        poisions = [Poision(x + 850, y) for x, y in [(200, 200), (400, 300), (500,300), (700, 120)]]
        jellys = [Jelly(100 * i + 800 + 50, j) for i, j in [(0, 120), (1,120), (2,120), (3, 135),
                                                           (4, 150), (5, 150), (6, 170), (7, 200)]]
        game_world.add_objects(fences, depth)
        game_world.add_objects(poisions, depth)
        for poison in poisions:
            game_world.add_collision_pairs('cookie:obstacle', None, poison)
        game_world.add_objects(jellys, depth)
        for jelly in jellys:
            game_world.add_collision_pairs('cookie:jelly', None, jelly)
    elif n == 2:
        fences = [Fence(i * 100 + 800 + 50) for i in range(0, 8)]
        olives = [Olive(i) for i in [850, 1050, 1450]]
        forkS2s = [ForkS2(i) for i in [1250]]
        jellys = [Jelly(100 * i + 800 + 50, j) for i, j in [(0, 200), (1, 120), (2, 200), (3, 120),
                                                           (4, 110), (5, 120), (6, 200), (7, 120)]]
        game_world.add_objects(fences, depth)
        game_world.add_objects(olives, depth)
        game_world.add_objects(forkS2s, depth)
        game_world.add_objects(jellys, depth)

        for olive in olives:
            game_world.add_collision_pairs('cookie:obstacle', None, olive)
        for forkS2 in forkS2s:
            game_world.add_collision_pairs('cookie:obstacle', None, forkS2)
        for jelly in jellys:
            game_world.add_collision_pairs('cookie:jelly', None, jelly)
    elif n == 3:
        fences = [Fence(i * 100 + 800 + 50) for i in range(0, 8)]
        forkS2s = [ForkS2(i) for i in [950, 1050, 1350, 1450]]
        jellys = [Jelly(100 * i + 800 + 50, j) for i, j in [(0, 150), (1, 110), (2, 110), (3, 150),
                                                           (4, 150), (5, 110), (6, 110), (7, 150)]]
        game_world.add_objects(fences, depth)
        game_world.add_objects(forkS2s, depth)
        game_world.add_objects(jellys, depth)

        for forkS2 in forkS2s:
            game_world.add_collision_pairs('cookie:obstacle', None, forkS2)
        for jelly in jellys:
            game_world.add_collision_pairs('cookie:jelly', None, jelly)
    elif n == 4:
        fences = [Fence(i * 100 + 800 + 50) for i in range(0, 8)]
        forks = [Fork(400 * i + 800 + 150) for i in range(0, 1)]
        forkS1s = [ForkS1(400* i + 800 + 350) for i in range(0, 1)]
        forkS2s = [ForkS2(1400)]
        jellys = [Jelly(100 * i + 800 + 50, j) for i, j in [(0, 120), (1, 200), (2, 250), (3, 300),
                                                           (4, 200), (5, 110), (6, 110), (7, 110)]]
        game_world.add_objects(fences, depth)
        game_world.add_objects(forks, depth)
        game_world.add_objects(forkS1s, depth)
        game_world.add_objects(forkS2s, depth)
        game_world.add_objects(jellys, depth)

        for fork in forks:
            game_world.add_collision_pairs('cookie:obstacle', None, fork)
        for forkS1 in forkS1s:
            game_world.add_collision_pairs('cookie:obstacle', None, forkS1)
        for forkS2 in forkS2s:
            game_world.add_collision_pairs('cookie:obstacle', None, forkS2)
        for jelly in jellys:
            game_world.add_collision_pairs('cookie:jelly', None, jelly)
    elif n == 5:
        fences = [Fence(i * 100 + 800 + 50) for i in range(0, 8)]
        olives = [Olive(400 * i + 800 + 150) for i in range(0, 2)]
        forkS1s = [ForkS1(400 * i + 800 + 250) for i in range(0,2)]
        jellys = [Jelly(100 * i + 800 + 50, j) for i, j in [(0, 120), (1, 200), (2, 300), (3, 200),
                                                           (4, 120), (5, 200), (6, 300), (7, 200)]]
        game_world.add_objects(fences, depth)
        game_world.add_objects(forkS1s, depth)
        game_world.add_objects(olives, depth)
        game_world.add_objects(jellys, depth)

        for olive in olives:
            game_world.add_collision_pairs('cookie:obstacle', None, olive)
        for forkS1 in forkS1s:
            game_world.add_collision_pairs('cookie:obstacle', None, forkS1)
        for jelly in jellys:
            game_world.add_collision_pairs('cookie:jelly', None, jelly)
