from threading import Thread, Condition


class MutableInt:
    def __init__(self):
        self._value = 0

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: int):
        if not isinstance(value, int):
            raise TypeError()
        self._value = value

class Worker(Thread):

    _condition = Condition()

    def __init__(self, my_offset: int, jump_size: int, current_offset: MutableInt):
        super().__init__()
        self.my_offset = my_offset
        self.jump_size = jump_size
        self.current_offset = current_offset


    def run(self):
        current_value = self.my_offset
        while current_value < 1000:
            with self._condition:
                while self.current_offset.value != self.my_offset:
                    self._condition.wait()
                print(current_value)
                current_value += self.jump_size
                next_offset = (self.current_offset.value + 1) % self.jump_size
                self.current_offset.value = next_offset
                self._condition.notifyAll()


def main():
    n = 10
    current_offset = MutableInt()
    for i in range(n):
        worker = Worker(i, n, current_offset)
        worker.start()


if __name__ == '__main__':
    main()
