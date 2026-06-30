class TahaRandom:
    def __init__(self, seed=12345):
        self.state = seed & 0xFFFFFFFFFFFF
        self._a = 25214903917
        self._c = 11
        self._m = 2 ** 48

    def _next(self):
        self.state = (self._a * self.state + self._c) % self._m
        return self.state

    def random(self):
        return self._next() / self._m

    def uniform(self, a, b):
        return a + (b - a) * self.random()

    def randint(self, a, b):
        if a > b:
            raise ValueError("a must be less than or equal to b")
        span = b - a + 1
        return a + int(self.random() * span)

    def choice(self, sequence):
        if not sequence:
            raise ValueError("sequence is empty")
        idx = self.randint(0, len(sequence) - 1)
        return sequence[idx]

    def shuffle(self, sequence):
        items = list(sequence)
        for i in range(len(items) - 1, 0, -1):
            j = self.randint(0, i)
            items[i], items[j] = items[j], items[i]
        return items

    def sample(self, sequence, k):
        items = list(sequence)
        if k > len(items):
            raise ValueError("sample larger than population")
        shuffled = self.shuffle(items)
        return shuffled[:k]

    def gauss(self, mu=0.0, sigma=1.0):
        from .power import sqrt, log
        from .trigonometry import cos
        from .constants import TAU
        u1 = self.random()
        u2 = self.random()
        if u1 <= 0:
            u1 = 1e-12
        z0 = sqrt(-2.0 * log(u1)) * cos(TAU * u2)
        return mu + z0 * sigma

    def random_bits(self, n):
        return self._next() % (2 ** n)

    def random_string(self, length, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"):
        return "".join(self.choice(alphabet) for _ in range(length))

    def weighted_choice(self, items, weights):
        total = sum(weights)
        if total == 0:
            raise ValueError("sum of weights must not be zero")
        r = self.random() * total
        cumulative = 0.0
        for item, weight in zip(items, weights):
            cumulative += weight
            if r <= cumulative:
                return item
        return items[-1]

    def random_walk(self, steps, step_size=1.0):
        position = 0.0
        path = [position]
        for _ in range(steps):
            position += step_size if self.random() < 0.5 else -step_size
            path.append(position)
        return path

    def dice_roll(self, sides=6, count=1):
        return [self.randint(1, sides) for _ in range(count)]

    def coin_flip(self):
        return self.random() < 0.5

    def seed(self, value):
        self.state = value & 0xFFFFFFFFFFFF


_default_random = TahaRandom()


def random():
    return _default_random.random()


def randint(a, b):
    return _default_random.randint(a, b)


def uniform(a, b):
    return _default_random.uniform(a, b)


def choice(sequence):
    return _default_random.choice(sequence)


def shuffle(sequence):
    return _default_random.shuffle(sequence)


def gauss(mu=0.0, sigma=1.0):
    return _default_random.gauss(mu, sigma)
