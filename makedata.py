import elliptic_operations as e_i
import numpy as np
import csv

G = e_i.point(3, 6, 7919, 2, 3)
order = G.order


def calcpoint(G, start, end, total_points):
    # load the dataset this is horribly inefficient due to bad implementation of multiply, fix later if issue
    # optimally in the future we can use projective cords to deal with point at infinity, for now labeling it 0,0
    # this will not be a duplicate of an actual point as long as b != 0
    # structure of data: x = [[generator x, generator y, g^i x, g^i y], ...], y = [i, ...]
    x = []
    y = []
    for i in range(start, end):
        temp = G.multiply(i)
        if temp.x is None and temp.y is None:
            x.append([G.x, G.y, G.order, G.a, G.b, 0, 0])
        else:
            x.append([G.x, G.y, G.order, G.a, G.b, temp.x, temp.y])

        temp = list(map(int, [*format(i, '011b')]))

        # for categorical
        '''
        temp = []
        for j in range(total_points):
            if j == i:
                temp.append(1)
            else:
                temp.append(0)
        '''
        y.append(temp)
    return x, y

'''
# figure out what shape data needs to be
x = np.swapaxes(np.array(x), 0, 1)
y = np.swapaxes(np.array(y), 0, 1)
'''

if __name__ == "__main__":
    x, y = calcpoint(G, 0, 500, 1008)
    x = np.array(x)
    y = np.array(y)

    with open('datax', 'w') as f:
        write = csv.writer(f)
        write.writerows(x)
    with open('datay', 'w') as f:
        write = csv.writer(f)
        write.writerows(y)

