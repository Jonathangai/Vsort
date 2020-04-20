from matplotlib import pyplot as plt
from matplotlib import animation
import math


class Sort:

    def __init__(self, length):
        self.value = [i + 1 for i in range(length)]
        self.data_length = length
        self.data = {}
        self.data["insert"] = self.insert()
        self.data["bubble"] = self.bubble()
        self.data["merge"] = self.merge()
        self.sort_length = len(self.data)
        self.time_length = max([len(self.data[item]) for item in self.data])

    def insert(self):
        li = self.value[:]
        data = [li[:]]
        for i in range(1, len(li)):
            key = li[i]
            j = i-1
            for j in reversed(range(0, i)):
                if key > li[j]:
                    li[j + 1], li[j] = li[j], key
                    data.append(li[:])
        return data

    def bubble(self):
        li = self.value[:]
        data = [li[:]]
        for i in reversed(range(0, len(li))):
            for j in range(0, i):
                if li[j + 1] > li[j]:
                    li[j + 1], li[j] = li[j], li[j + 1]
                    data.append(li[:])
        return data

    def merge(self):
        # Weird argument for the ease of visualization.
        def mergeSort(li, pos):
            if len(li) > 1:
                left = li[:len(li) // 2]
                right = li[len(li) // 2:]
                mergeSort(left, [*pos, 0])
                mergeSort(right, [*pos, 1])
                i = 0
                j = 0
                while (i < len(left)) and (j < len(right)):
                    if left[i] > right[j]:
                        li[i + j] = left[i]
                        temp[position(pos) + i + j] = left[i]
                        data.append(temp[:])
                        i = i + 1
                    else:
                        li[i + j] = right[j]
                        temp[position(pos) + i + j] = right[j]
                        data.append(temp[:])
                        j = j + 1
                while i < len(left):
                    li[i + j] = left[i]
                    temp[position(pos) + i + j] = left[i]
                    data.append(temp[:])
                    i = i + 1
                while j < len(right):
                    li[i + j] = right[j]
                    temp[position(pos) + i + j] = right[j]
                    data.append(temp[:])
                    j = j + 1

        def position(pos):
            t = self.data_length
            sum = 0
            for item in pos:
                if item == 1:
                    sum = sum + t // 2
                    t = math.ceil(t / 2)
                else:
                    t = t // 2
            return sum

        li = self.value[:]
        temp = self.value[:]
        data = []
        mergeSort(li, [])
        return data

    def draw(self):
        def ani(time):
            for idx, item in enumerate(self.data):
                ax[idx].clear()
                ax[idx].bar([i for i in range(self.data_length)],
                            [i for i in self.data[item][time]])

        fig, ax = plt.subplots(self.sort_length)
        anim = animation.FuncAnimation(fig, ani,
                                       frames=range(self.time_length),
                                       interval=1, repeat=False)
        anim.save('vsort.mp4', fps=30)
        plt.show()


sort = Sort(30)
sort.draw()
