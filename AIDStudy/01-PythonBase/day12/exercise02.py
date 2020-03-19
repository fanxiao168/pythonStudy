# 玩家（攻击力） 攻击敌人（血量）敌人受伤 （减血）可能死亡（播放动画）
# 敌人攻击玩家  玩家受伤（减血 碎屏） 可能死亡（游戏结束）

# 玩家类
class Player:
    def __init__(self, atk=10, hp=100):
        self.atk = atk
        self.hp = hp

    def attack(self, enemy):
        print('玩家打人啦')
        enemy.damage(self.atk)

    def damage(self, value):
        print('我去')
        self.hp -= value
        if self.hp <= 0:
            print('你真菜，游戏结束')


# 敌人类
class Enemy:
    def __init__(self, hp=100, atk=99):
        self.hp = hp
        self.atk = atk

    def damage(self, value):
        print('啊！')
        # 敌人减血
        self.hp -= value
        # 可能死亡
        if self.hp <= 0:
            print('敌人死亡，播放动画')

    def attack(self, player):
        print('敌人攻击玩家咯')
        player.damage(self.atk)


gb1 = Enemy()
p01 = Player()
p01.attack(gb1)
gb1.attack(p01)
