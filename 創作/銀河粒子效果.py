#銀河粒子效果
import pygame
import random
import math

pygame.init()

# =========================================================
# 基本設定
# =========================================================

WIDTH = 1280
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cinematic Black Hole Galaxy")

clock = pygame.time.Clock()

CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2


# =========================================================
# 顏色
# =========================================================

SPACE = (2, 3, 10)


# =========================================================
# 星星
# =========================================================

stars = []

for i in range(450):

    stars.append({
        "x": random.randrange(WIDTH),
        "y": random.randrange(HEIGHT),
        "size": random.choice([1, 1, 1, 1, 2]),
        "brightness": random.randint(70, 220),
        "phase": random.uniform(0, math.pi * 2),
        "speed": random.uniform(0.5, 2.0)
    })


# =========================================================
# 背景星雲粒子
# =========================================================

nebula = []

for i in range(500):

    angle = random.uniform(0, math.pi * 2)

    radius = random.uniform(150, 700)

    x = CENTER_X + math.cos(angle) * radius
    y = CENTER_Y + math.sin(angle) * radius * 0.55

    nebula.append({
        "x": x,
        "y": y,
        "size": random.uniform(1, 5),
        "alpha": random.randint(10, 35),
        "phase": random.uniform(0, math.pi * 2)
    })


# =========================================================
# 吸積盤粒子
# =========================================================

particles = []

PARTICLE_COUNT = 1600


for i in range(PARTICLE_COUNT):

    angle = random.uniform(0, math.pi * 2)

    # 大量粒子分布在外圈
    radius = random.uniform(100, 520)

    # 銀河盤的厚度
    height = random.uniform(0.18, 0.42)

    # 讓粒子有一點螺旋偏移
    spiral = radius * 0.012

    angle += spiral

    x = CENTER_X + math.cos(angle) * radius
    y = CENTER_Y + math.sin(angle) * radius * height

    particles.append({
        "angle": angle,
        "radius": radius,
        "height": height,

        "speed": random.uniform(0.002, 0.009),

        "size": random.choice([1, 1, 1, 2, 2, 3]),

        "heat": random.random(),

        "x": x,
        "y": y,

        "old_x": x,
        "old_y": y
    })


# =========================================================
# 光暈 Surface
# =========================================================

glow_surface = pygame.Surface(
    (700, 700),
    pygame.SRCALPHA
)


# =========================================================
# 黑洞光暈
# =========================================================

def draw_black_hole_glow():

    glow_surface.fill((0, 0, 0, 0))

    center = 350

    # 藍紫色外部光暈

    for radius in range(280, 80, -8):

        alpha = int(
            1 + (280 - radius) * 0.025
        )

        pygame.draw.circle(
            glow_surface,
            (70, 80, 255, alpha),
            (center, center),
            radius
        )

    # 橘紅色內部光暈

    for radius in range(100, 35, -3):

        alpha = int(
            3 + (100 - radius) * 0.04
        )

        pygame.draw.circle(
            glow_surface,
            (255, 100, 25, alpha),
            (center, center),
            radius
        )

    screen.blit(
        glow_surface,
        (
            CENTER_X - 350,
            CENTER_Y - 350
        )
    )


# =========================================================
# 畫星雲
# =========================================================

def draw_nebula():

    nebula_surface = pygame.Surface(
        (WIDTH, HEIGHT),
        pygame.SRCALPHA
    )

    for cloud in nebula:

        pulse = math.sin(
            pygame.time.get_ticks() * 0.0005
            + cloud["phase"]
        )

        alpha = int(
            cloud["alpha"] + pulse * 5
        )

        # 不同區域使用不同色調

        if cloud["x"] < CENTER_X:

            color = (
                70,
                60,
                150,
                alpha
            )

        else:

            color = (
                130,
                45,
                90,
                alpha
            )

        pygame.draw.circle(
            nebula_surface,
            color,
            (
                int(cloud["x"]),
                int(cloud["y"])
            ),
            int(cloud["size"])
        )

    screen.blit(
        nebula_surface,
        (0, 0)
    )


# =========================================================
# 畫星星
# =========================================================

def draw_stars():

    current_time = pygame.time.get_ticks()

    for star in stars:

        flicker = math.sin(
            current_time * 0.001
            * star["speed"]
            + star["phase"]
        )

        brightness = int(
            star["brightness"]
            + flicker * 30
        )

        brightness = max(
            30,
            min(255, brightness)
        )

        pygame.draw.circle(
            screen,
            (
                brightness,
                brightness,
                min(255, brightness + 15)
            ),
            (
                star["x"],
                star["y"]
            ),
            star["size"]
        )


# =========================================================
# 畫吸積盤
# =========================================================

def draw_accretion_disk():

    # 使用獨立透明圖層
    disk_surface = pygame.Surface(
        (WIDTH, HEIGHT),
        pygame.SRCALPHA
    )

    for particle in particles:

        x = particle["x"]
        y = particle["y"]

        radius = particle["radius"]

        # 越靠近黑洞越熱
        heat = max(
            0,
            min(
                1,
                1 - radius / 500
            )
        )

        # 遠處偏藍
        # 靠近黑洞變橘白

        red = int(
            100 + heat * 155
        )

        green = int(
            120 + heat * 100
        )

        blue = int(
            255 - heat * 180
        )

        # 透明度
        alpha = int(
            80 + heat * 160
        )

        color = (
            red,
            green,
            blue,
            alpha
        )

        # 粒子大小
        size = particle["size"]

        pygame.draw.circle(
            disk_surface,
            color,
            (
                int(x),
                int(y)
            ),
            size
        )

    screen.blit(
        disk_surface,
        (0, 0)
    )


# =========================================================
# 更新吸積盤
# =========================================================

def update_particles():

    for particle in particles:

        particle["old_x"] = particle["x"]
        particle["old_y"] = particle["y"]

        radius = particle["radius"]


        # -----------------------------------------
        # 基本旋轉速度
        # -----------------------------------------

        speed = particle["speed"]


        # -----------------------------------------
        # 越靠近黑洞旋轉越快
        # -----------------------------------------

        if radius < 300:

            speed *= 1.5

        if radius < 200:

            speed *= 2.5

        if radius < 120:

            speed *= 5

        if radius < 70:

            speed *= 8


        particle["angle"] += speed


        # -----------------------------------------
        # 重力吸入
        # -----------------------------------------

        if radius < 450:

            gravity = (
                (450 - radius)
                / 450
            )

            particle["radius"] -= (
                gravity * 0.18
            )


        # -----------------------------------------
        # 事件視界附近
        # -----------------------------------------

        if radius < 120:

            particle["radius"] -= 0.8


        if radius < 70:

            particle["radius"] -= 2.5


        # -----------------------------------------
        # 計算位置
        # -----------------------------------------

        # 螺旋扭曲
        spiral = (
            0.015
            * particle["radius"]
        )

        final_angle = (
            particle["angle"]
            + spiral
        )

        particle["x"] = (
            CENTER_X
            + math.cos(final_angle)
            * particle["radius"]
        )

        particle["y"] = (
            CENTER_Y
            + math.sin(final_angle)
            * particle["radius"]
            * particle["height"]
        )


        # -----------------------------------------
        # 被黑洞吞掉
        # -----------------------------------------

        if particle["radius"] < 25:

            particle["angle"] = random.uniform(
                0,
                math.pi * 2
            )

            particle["radius"] = random.uniform(
                350,
                550
            )

            particle["height"] = random.uniform(
                0.18,
                0.42
            )

            particle["speed"] = random.uniform(
                0.002,
                0.009
            )


# =========================================================
# 畫粒子拖尾
# =========================================================

def draw_particle_trails():

    trail_surface = pygame.Surface(
        (WIDTH, HEIGHT),
        pygame.SRCALPHA
    )

    for particle in particles:

        radius = particle["radius"]

        if radius > 350:
            continue

        # 越靠近黑洞拖尾越長

        if radius < 100:

            alpha = 180
            width = 3

        elif radius < 200:

            alpha = 120
            width = 2

        else:

            alpha = 60
            width = 1


        # 顏色

        heat = max(
            0,
            min(
                1,
                1 - radius / 400
            )
        )

        color = (
            150 + int(105 * heat),
            160 + int(70 * heat),
            255 - int(160 * heat),
            alpha
        )


        pygame.draw.line(
            trail_surface,
            color,
            (
                int(particle["old_x"]),
                int(particle["old_y"])
            ),
            (
                int(particle["x"]),
                int(particle["y"])
            ),
            width
        )

    screen.blit(
        trail_surface,
        (0, 0)
    )


# =========================================================
# 黑洞事件視界
# =========================================================

def draw_event_horizon():

    # 光環
    pygame.draw.circle(
        screen,
        (255, 210, 130),
        (
            CENTER_X,
            CENTER_Y
        ),
        32,
        2
    )

    # 熱光圈
    pygame.draw.circle(
        screen,
        (255, 120, 40),
        (
            CENTER_X,
            CENTER_Y
        ),
        27,
        3
    )

    # 真正的黑洞
    pygame.draw.circle(
        screen,
        (0, 0, 0),
        (
            CENTER_X,
            CENTER_Y
        ),
        24
    )

    # 黑洞內部
    pygame.draw.circle(
        screen,
        (1, 1, 3),
        (
            CENTER_X,
            CENTER_Y
        ),
        20
    )


# =========================================================
# 主程式
# =========================================================

running = True

while running:

    clock.tick(60)


    # -----------------------------------------
    # 事件
    # -----------------------------------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False


    # -----------------------------------------
    # 背景
    # -----------------------------------------

    screen.fill(SPACE)


    # -----------------------------------------
    # 星雲
    # -----------------------------------------

    draw_nebula()


    # -----------------------------------------
    # 星星
    # -----------------------------------------

    draw_stars()


    # -----------------------------------------
    # 黑洞光暈
    # -----------------------------------------

    draw_black_hole_glow()


    # -----------------------------------------
    # 更新粒子
    # -----------------------------------------

    update_particles()


    # -----------------------------------------
    # 粒子拖尾
    # -----------------------------------------

    draw_particle_trails()


    # -----------------------------------------
    # 吸積盤
    # -----------------------------------------

    draw_accretion_disk()


    # -----------------------------------------
    # 黑洞
    # -----------------------------------------

    draw_event_horizon()


    pygame.display.flip()


pygame.quit()