import Constants


class ObjectType:
    def __init__(self):
        self.x = None
        self.y = None
        self.vx = None
        self.vy = None
        self.r = None
        self.flex = 1

    def move(self, gravity=True):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.y + self.vy > Constants.HEIGHT - self.r or self.y + self.vy < self.r:
            self.vy = -self.vy * self.flex
        elif gravity:
            self.vy += Constants.g * Constants.k
        if self.x + self.vx > Constants.WIDTH - self.r or self.x + self.vx < self.r:
            self.vx = -self.vx * self.flex
        self.y += self.vy
        self.x += self.vx

    def is_collide(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.

        Единица нужна для более простого попадания))
        """
        return (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (self.r + obj.r) ** 2 + 1

    def draw(self):
        pass
