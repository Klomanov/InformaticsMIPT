FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
TANK_COLOR = 0x47A76A


WIDTH = 800
HEIGHT = 600

GUN_SPAWN = (WIDTH/2, HEIGHT - 30)
BOMBER_SPAWN_Y = 20

TARGET_SPAWN_DELAY = 2
RED_DURATION = 0.2
INVINCIBLE_DURATION = 1
INSTRUCTIONS_DURATION = 9

USUAL_TYPE = 0
UNUSUAL_TYPE = 1

MIN_R_TARGET = 5
MAX_R_TARGET = 15

BIG_BULLETS_R = 13
SMALL_BULLETS_R = 5

BIG_BULLETS_POWER = 0.7
SMALL_BULLETS_POWER = 1.3

k = 0.3
g = 9.81 * k
FLEX = 0.5  # Упругость шарика.

INSTRUCTIONS_TEXT = """На Землю напал НЛО, поэтому бравому танкисту следует ее защитить!
        ЛКМ - маленький быстрый снаряд
        ПКМ - большой тяжелый снаряд
        Попадание по снарядам НЛО дает очки
        Попадение снарядов НЛО по тебе отнимает очки 
        Цель: набрать наибольшее количество очков!
        Удачи!"""