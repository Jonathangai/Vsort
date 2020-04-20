from matplotlib import pyplot as plt
from matplotlib import animation


class Sort:

    def __init__(self, length):
        self.value = [i + 1 for i in range(length)]
        self.data = {}
        self.data["insert"] = self.insert()
        self.data["bubble"] = self.bubble()
        self.data_length = length
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

    def draw(self):
        def ani(time):
            for idx, item in enumerate(self.data):
                ax[idx].clear()
                ax[idx].bar([i for i in range(self.data_length)],
                            [i for i in self.data[item][time]])

        fig, ax = plt.subplots(2)
        anim = animation.FuncAnimation(fig, ani,
                                       frames=range(self.time_length),
                                       interval=1, repeat=False)
        anim.save('vsort.mp4', fps=30)
        plt.show()


sort = Sort(30)
sort.draw()
