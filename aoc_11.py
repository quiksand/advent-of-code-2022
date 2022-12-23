

DAY = 11


class Monkey:
    all = []
    mod = 1

    @classmethod
    def reset(cls):
        cls.all = []
        cls.mod = 1

    @classmethod
    def add(cls, monkey):
        cls.mod *= monkey.div_by
        cls.all.append(monkey)

    @classmethod
    def get(cls, monkey_number):
        return cls.all[monkey_number]

    @classmethod
    def play_round(cls, boredom):
        for monkey in cls.all:
            monkey.process(boredom)
    
    def __init__(self, number, true_monkey_number, false_monkey_number, div_by, starting_items, inspect_func):
        self.number = number
        self.true_monkey_number = true_monkey_number
        self.false_monkey_number = false_monkey_number
        self.div_by = div_by
        self.items = starting_items
        self.inspect_func = inspect_func
        self.inspection_count = 0
        Monkey.add(self)

    def next_monkey(self, item):
        test = item % self.div_by == 0
        return self.true_monkey_number if test else self.false_monkey_number

    def inspect(self, item):
        self.inspection_count += 1
        return self.inspect_func(item)

    def throw(self, to_monkey_number, item):
        Monkey.get(to_monkey_number).items.append(item)

    def get_bored(self, item):
        return item // 3

    def process(self, boredom):
        for item in self.items:
            worry = self.inspect(item)
            if boredom:
                worry = self.get_bored(worry)
            else:
                worry = worry % Monkey.mod
            throw_to = self.next_monkey(worry)
            self.throw(throw_to, worry)
        self.items = []

def get_monkeys():
    Monkey.reset()
    Monkey(0, 6, 5, 11, [73, 77], lambda x: x * 5)
    Monkey(1, 6, 0, 19, [57, 88, 80], lambda x: x + 5)
    Monkey(2, 3, 1, 5, [61, 81, 84, 69, 77, 88], lambda x: x * 19)
    Monkey(3, 1, 0, 3, [78, 89, 71, 60, 81, 84, 87, 75], lambda x: x + 7)
    Monkey(4, 2, 7, 13, [60, 76, 90, 63, 86, 87, 89], lambda x: x + 2)
    Monkey(5, 4, 7, 17, [88], lambda x: x + 1)
    Monkey(6, 5, 4, 7, [84, 98, 78, 85], lambda x: x * x)
    Monkey(7, 3, 2, 2, [98, 89, 78, 73, 71], lambda x: x + 4)

def get_test_monkeys():
    Monkey.reset()
    Monkey(0, 2, 3, 23, [79, 98], lambda x: x * 19)
    Monkey(1, 2, 0, 19, [54, 65, 75, 74], lambda x: x + 6)
    Monkey(2, 1, 3, 13, [79, 60, 97], lambda x: x * x)
    Monkey(3, 0, 1, 17, [74], lambda x: x + 3)

def play_n_rounds(n, boredom=True):
    for _ in range(n):
        Monkey.play_round(boredom)

def solve_part_1():
    # get_test_monkeys()
    get_monkeys()
    play_n_rounds(20)
    inspected_items = sorted(monkey.inspection_count for monkey in Monkey.all)
    return inspected_items[-1] * inspected_items[-2]

def solve_part_2():
    # get_test_monkeys()
    get_monkeys()
    play_n_rounds(10000, boredom=False)
    inspected_items = sorted(monkey.inspection_count for monkey in Monkey.all)
    return inspected_items[-1] * inspected_items[-2]

if __name__ == '__main__':
    answer_part_1 = solve_part_1()
    print(f'The answer for part 1 is {answer_part_1}')
    answer_part_2 = solve_part_2()
    print(f'The answer for part 2 is {answer_part_2}')
