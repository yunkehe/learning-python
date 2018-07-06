# /usr/bin

class Settings():
    # 存储外星人入侵的所有设置项
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 3

        # 子弹
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        # 存储所允许的最大子弹数
        self.bullets_allowed = 3

        # 外星人
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # 1 向右移动 -1向左移动
        self.fleet_direction = 1