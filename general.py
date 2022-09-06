from Identity import Identity


def colision(id1: Identity, id2: Identity):
    if id1.x + id1.xDeslocation >= id2.x + id2.xDeslocation and id1.x + id1.xDeslocation + id1.width <= id2.x:
        if id1.y + id1.yDeslocation + id1.height >= id2.y + id2.yDeslocation + id2.height and id1.y + id1.yDeslocation <= id2.y+ id1.yDeslocation:
            return True
        return False