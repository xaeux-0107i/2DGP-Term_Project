from pico2d import load_image

global speed
speed = 4


class Fence:
    def __init__(self, x):
        self.image = load_image('oven_fence.png')
        self.x = x #50
        self.dx = 2*speed
        if self.image is None:
            print("펜스 이미지 로드 실패")
    def draw(self):
        self.image.clip_draw(0, 0, 124, 120, self.x, 40, 100, 80)
    def update(self):
        self.x -= self.dx
        # 만약 울타리가 화면 왼쪽 밖으로 이동하면 위치를 오른쪽 끝으로 재설정
        if self.x < -50:  # -50은 울타리 너비에 맞게 조정
            self.x += 900  # fences2의 오른쪽 끝으로 이동
        pass


class Jelly:
    def __init__(self, x):
        self.image = load_image('jelly.png')
        self.x = x #50
        self.dx = 2*speed
        if self.image is None:
            print("젤리 이미지 로드 실패")
    def draw(self):
        self.image.clip_draw(0, 0, 55, 52, self.x, 130, 50, 50)
    def update(self):
        self.x -= self.dx
        # 만약 젤리가 화면 왼쪽 밖으로 이동하면 위치를 오른쪽 끝으로 재설정
        if self.x < -50:  # -50은 울타리 너비에 맞게 조정
            self.x += 900  # jelly2의 오른쪽 끝으로 이동
        pass
