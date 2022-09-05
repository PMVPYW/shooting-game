from Identity import Identity


def colide(id1: Identity, id2: Identity):
    if id1.x >= id2.x-id2.width and id1.x <= id2.x+id2.width:
        return