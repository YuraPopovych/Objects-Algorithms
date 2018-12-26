class FibSeq:
    def __init__(self):
        self.back1 = 1
        self.back2 = 0
    def next_number(self):
        result = self.back1 + self.back2
        self.back2 = self.back1
        self.back1 = result
        return result

newFib = FibSeq()
print(newFib.next_number())
print(newFib.next_number())
print(newFib.next_number())
print(newFib.next_number())
print(newFib.next_number())


