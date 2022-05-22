class BubbleSort:
    def __init__(self, array):
        self.input = array.copy()

    def sort(self):
        border = len(self.input)-1
        swapped = True
        while border > 0:
            if swapped:
                i = 0
                swapped = False
                while i < border:
                    print(self.input[i], self.input[i+1])
                    if self.input[i] > self.input[i+1]:
                        self.input[i], self.input[i+1] = self.input[i+1], self.input[i]
                        swapped = True
                    i += 1
            else:
                break
            border -= 1


if __name__ == "__main__":
    array = [1, 6, 7, 3, 4, 10]

    bubbleSort = BubbleSort(array)
    bubbleSort.sort()
    print(bubbleSort.input)
