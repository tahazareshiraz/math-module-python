def lcg_random(seed, a=1103515245, c=12345, m=2 ** 31):
    return (a * seed + c) % m



def lcg_sequence(seed, n, a=1103515245, c=12345, m=2 ** 31):
    seq = []
    x = seed
    for _ in range(n):
        x = lcg_random(x, a, c, m)
        seq.append(x)
    return seq

