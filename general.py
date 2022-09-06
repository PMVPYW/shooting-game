from Bullet import Bullet
from Identity import Identity


def colision(id1: Identity, bullet: Bullet):
    if id1.lastId == bullet.id:
        return False

    if (id1.x+id1.width >= bullet.x) and (id1.x <= bullet.x+bullet.width):
        if (id1.y <= bullet.y) and (id1.y + id1.height >= bullet.y):
            return True
    return False
