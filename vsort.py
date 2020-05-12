from matplotlib import pyplot as plt
from matplotlib import animation
import math
import random
import sys
import getopt


class Sort:
    """ This is a class for animation of the sorting algorithms.

    Attributes:
        value         (list): The unsorted list.
        data_length    (int): The length of the unsorted list.
        data          (dict): The data of steps of each sorting algorithms.
        sort_length    (int): The number of sorting algorithms.
        time_length    (int): The maximum number of steps needed using
                              different sorting algorithms.
        anim (FuncAnimation): A matplotlib.animation.FuncAnimation object
                              that is the animation of sorting algorithms.
    """

    def __init__(self, unsorted):
        """
        Initiates the Sort class

        Parameters:
            unsorted  (list): The unsorted list.
        """

        self.value = unsorted
        self.data_length = len(unsorted)
        self.data = {}
        self.data["insert"] = self.insert()
        self.data["bubble"] = self.bubble()
        self.data["merge"] = self.merge()
        self.data["quick"], self.data["randomized quick"] = self.quick()
        self.sort_length = len(self.data)
        self.time_length = max([len(self.data[item]) for item in self.data])
        self.equalLength()

    def insert(self) -> list:
        """The method to return the steps to sort with insert sort."""

        li = self.value[:]
        data = [li[:]]
        for i in range(1, len(li)):
            key = li[i]
            for j in reversed(range(0, i)):
                if key > li[j]:
                    li[j + 1], li[j] = li[j], key
                    data.append(li[:])
        return data

    def bubble(self) -> list:
        """The method to return the steps to sort with bubble sort."""

        li = self.value[:]
        data = [li[:]]
        for i in reversed(range(0, len(li))):
            for j in range(0, i):
                if li[j + 1] > li[j]:
                    li[j + 1], li[j] = li[j], li[j + 1]
                    data.append(li[:])
        return data

    def merge(self) -> list:
        """The method to return the steps to sort with merge sort."""

        # Weird argument for the ease of visualization.
        def mergeSort(li, pos):
            """The function that sorts the list recursively."""

            if len(li) > 1:
                left, right = li[:len(li) // 2], li[len(li) // 2:]
                mergeSort(left, [*pos, 0])
                mergeSort(right, [*pos, 1])
                i, j = 0, 0
                while (i < len(left)) and (j < len(right)):
                    if left[i] > right[j]:
                        li[i + j] = left[i]
                        temp[position(pos) + i + j] = left[i]
                        data.append(temp[:])
                        i += 1
                    else:
                        li[i + j] = right[j]
                        temp[position(pos) + i + j] = right[j]
                        data.append(temp[:])
                        j += 1
                while i < len(left):
                    li[i + j] = left[i]
                    temp[position(pos) + i + j] = left[i]
                    data.append(temp[:])
                    i += 1
                while j < len(right):
                    li[i + j] = right[j]
                    temp[position(pos) + i + j] = right[j]
                    data.append(temp[:])
                    j += 1

        def position(pos) -> int:
            """
            The function that returns position of the element based on the
            list of numbers.
            """

            t = self.data_length
            real_position = 0
            for item in pos:
                if item == 1:
                    real_position = real_position + t // 2
                    t = math.ceil(t / 2)
                else:
                    t = t // 2
            return real_position

        temp = self.value[:]
        li = self.value[:]
        data = []
        mergeSort(li, [])
        return data

    def quick(self) -> list:
        """
        The method to return the steps to sort with quick sort and quick
        quick with random pivots.
        """

        def partition(li, p, r, data):
            """The function that partitions the list by a pivot"""

            x = li[r]
            i = p - 1
            for j in range(p, r):
                if li[j] >= x:
                    i += 1
                    li[i], li[j], = li[j], li[i]
                data.append(li[:])
            li[i + 1], li[r] = li[r], li[i + 1]
            data.append(li[:])
            return i + 1

        def quickSort(li, p, r, data):
            """
            The function that recursively sorts the list using partition
            function recursively.
            """

            if p < r:
                q = partition(li, p, r, data)
                quickSort(li, p, q - 1, data)
                quickSort(li, q + 1, r, data)

        def randomPartition(li, p, r, data):
            """The function that partitions the list by a random pivot"""

            i = random.randint(p, r)
            li[r], li[i] = li[i], li[r]
            return partition(li, p, r, data)

        def randomQuickSort(li, p, r, data):
            """
            The function that recursively sorts the list using random
            partition function recursively.
            """

            if p < r:
                q = randomPartition(li, p, r, data)
                randomQuickSort(li, p, q - 1, data)
                randomQuickSort(li, q + 1, r, data)

        li = self.value[:]
        data = []
        quickSort(li, 0, len(li) - 1, data)
        li = self.value[:]
        random_data = []
        randomQuickSort(li, 0, len(li) - 1, random_data)
        return data, random_data

    def equalLength(self):
        """
        The method adds sorted list to the end of data, so each of the
        entries would have the same number of steps.
        """

        for item in self.data:
            while len(self.data[item]) < self.time_length:
                self.data[item].append(self.data[item][-1])

    def draw(self, inter=10, show=True):
        """
        The method draws the animation of sorting algorithms using
        matplotlib.

        Parameters:
            inter (int): The number of milliseconds between each frame
                         in the animation.
            show (bool): A boolean value that determines if the animation
                         is shown.
        """

        if not float(inter).is_integer() or inter < 0:
            inter = 10

        def update(time):
            """The function that updates each frame."""

            for idx, item in enumerate(self.data):
                for id1, rect in enumerate(rects[idx]):
                    rect.set_height(self.data[item][time][id1])

        self.equalLength()
        fig, ax = plt.subplots(self.sort_length)
        fig.tight_layout(rect=[0, 0.03, 1, 0.95])
        rects = [0 for i in range(self.sort_length)]
        for idx, item in enumerate(self.data):
            ax[idx].set_title(item)
            ax[idx].axis("off")
            rects[idx] = ax[idx].bar([i for i in range(self.data_length)],
                                     [i for i in self.data[item][0]])
        anim = animation.FuncAnimation(fig, update,
                                       frames=range(self.time_length),
                                       interval=inter, repeat=False)
        anim._start()
        self.anim = anim
        if show:
            plt.show()

    def save(self):
        """The method that saves the animation as an MP4 file."""

        self.draw(1, show=False)
        self.anim.save("vsort.mp4", fps=60)


def main(argv):
    """
    The main function that creates a animation based on the command line
    arguments.

    Parameters:
        argv: The list of strings of the command line options.
    """

    def help():
        """The function that prints the help message."""

        print("Usage: vsort.py [-shr] [-i <interval>]")
        print()
        print("Sort 50 bars from largest to smallest using different")
        print()
        print("optional arguments:")
        print("  -h    show this help message and exit")
        print("  -r    the bars are reversed instead of randomized")
        print("  -s    save the animation as a MP4 file")
        print("  -i    takes an integer input that is the length "
              "between each frame (default: 10)")
        sys.exit()

    unsorted = [random.randint(1, 100) for _ in range(50)]
    interval = 10
    try:
        opts, args = getopt.getopt(argv, "shi:r")
    except getopt.GetoptError:
        help()
    for opt, arg in opts:
        if opt == "-h":
            help()
        if opt == "-i":
            interval = int(arg)
    op = [item[0] for item in opts]
    if "-r" in op:
        unsorted = list(range(0, 50))
    sort = Sort(unsorted)
    sort.draw(interval)
    if "-s" in op:
        sort.save()


if __name__ == "__main__":
    main(sys.argv[1:])
