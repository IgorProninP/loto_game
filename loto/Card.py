import random


class Create_cards:

    def __init__(self):
        self.card = self.create_card()

    def create_row(self):
        self.row = []
        self.row.append(random.randint(1, 90))
        while len(self.row) < 15:
            self.num = random.randint(1, 90)
            if self.num not in self.row:
                check = 0
                for j in self.row:
                    if self.num // 10 == j // 10:
                        check += 1
                if check < 3:
                    self.row.append(self.num)
                else:
                    continue
        return sorted(self.row)

    def create_card(self):
        self.row = self.create_row()
        self.a = [[' '] * 9 for i in range(3)]
        self.d = 0
        for i in self.row:
            if self.d == 0:
                self.a[0][i // 10] = i
                self.d += 1
                continue
            elif self.d == 1:
                self.a[1][i // 10] = i
                self.d += 2
                continue
            else:
                if i != 90:
                    self.a[2][i // 10] = i
                    self.d = 0
                else:
                    self.a[2][(i // 10) - 1] = i
                continue
        # b = [a[random.shuffle((0, 1, 2))] for i in range(3)]
        random.shuffle(self.a)
        return self.a

    def __getitem__(self, item):
        return self.card


