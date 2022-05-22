class SelectionSort:
    def __init__(self, array):
        self.input = array.copy()
        self.temp = array.copy()
        self.pointer = 0

    def sort(self):
        for i in range(len(self.input)-1):
            mn = min(range(i, len(self.input)), key=self.input.__getitem__)  # find and assign idnex of minimum value to mn
            self.input[i], self.input[mn] = self.input[mn], self.input[i]  # replace pointer element with minimum element

    def next(self):
        if self.pointer < len(self.temp):
            mn = min(range(self.pointer, len(self.temp)), key=self.temp.__getitem__)  # find and assign idnex of minimum value to mn
            self.temp[self.pointer], self.temp[mn] = self.temp[mn], self.temp[self.pointer]  # replace pointer element with minimum element
            self.pointer += 1
            return self.temp
        else:
            raise IndexError("Already Finished Sorting")
if __name__ == "__main__":
    array = [1, 6, 7, 3, 4, 10]

    selectionSort = SelectionSort(array)
    i = 0
    try:
        while i < 10:
           print(selectionSort.next())
           i += 1
    except:
        print('Finish')
