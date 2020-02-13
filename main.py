class Edge:
    x = None
    y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return ""+str(self.x)+" "+str(self.y)

    def __eq__(self, other):
        if isinstance(other,Edge):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))

def go():
    start = Edge(7, 0)
    end = Edge(0, 7)
    level = {start: 0}

    parent = {start: None}
    frontier = [start]
    f = 1
    flag = False
    temp = []
    while frontier:
        next = []
        for item in frontier:
            if item == end:
                flag = True
                break
            temp = contruct_edges(item)
            for value in temp:
                if value not in level:
                    level[value] = f
                    parent[value] = item
                    next.append(value)
        if flag: break
        frontier = next
        f += 1

    print("minimum steps : {}".format(level[Edge(0,7)]))
    print("the path :")
    shortest_path(parent,start,end)

def shortest_path(parent,src,dest):
    if src == dest : return
    else:
        shortest_path(parent,src,parent[dest])
        print(dest)

def contruct_edges(edge):
    list = []
    x = edge.x
    y = edge.y
    if valid(x - 2, y + 1):   list.append(Edge(x - 2, y + 1))
    if valid(x - 2, y - 1):   list.append(Edge(x - 2, y - 1))
    if valid(x + 2, y + 1):   list.append(Edge(x + 2, y + 1))
    if valid(x + 2, y - 1):   list.append(Edge(x + 2, y - 1))
    if valid(x - 1, y + 2):   list.append(Edge(x - 1, y + 2))
    if valid(x + 1, y + 2):   list.append(Edge(x + 1, y + 2))
    if valid(x - 1, y - 2):   list.append(Edge(x - 1, y - 2))
    if valid(x + 1, y - 2):   list.append(Edge(x + 1, y - 2))

    return list


def valid(x, y):
    return (x < 8) and (x > -1) and (y < 8) and (y > -1)


if __name__ == '__main__':
    go()
