from .numtheory_core import gcd
from .numbertheory import is_prime, mod_pow, mod_inverse, extended_gcd, sieve_of_eratosthenes


def caesar_encrypt(text, shift):
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return "".join(result)


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


def caesar_bruteforce(text):
    return [(shift, caesar_decrypt(text, shift)) for shift in range(26)]


def vigenere_encrypt(text, key):
    key = key.upper()
    result = []
    ki = 0
    for ch in text:
        if ch.isalpha():
            shift = ord(key[ki % len(key)]) - ord('A')
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
            ki += 1
        else:
            result.append(ch)
    return "".join(result)


def vigenere_decrypt(text, key):
    key = key.upper()
    result = []
    ki = 0
    for ch in text:
        if ch.isalpha():
            shift = ord(key[ki % len(key)]) - ord('A')
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base - shift) % 26 + base))
            ki += 1
        else:
            result.append(ch)
    return "".join(result)


def atbash_encrypt(text):
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr(base + 25 - (ord(ch) - base)))
        else:
            result.append(ch)
    return "".join(result)


def atbash_decrypt(text):
    return atbash_encrypt(text)


def rot13(text):
    return caesar_encrypt(text, 13)


def affine_encrypt(text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("a must be coprime with 26")
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            x = ord(ch) - base
            result.append(chr((a * x + b) % 26 + base))
        else:
            result.append(ch)
    return "".join(result)


def affine_decrypt(text, a, b):
    a_inv = mod_inverse(a, 26)
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            x = ord(ch) - base
            result.append(chr((a_inv * (x - b)) % 26 + base))
        else:
            result.append(ch)
    return "".join(result)


def rail_fence_encrypt(text, rails):
    fence = [[] for _ in range(rails)]
    rail = 0
    going_down = True
    for ch in text:
        fence[rail].append(ch)
        if rail == 0:
            going_down = True
        elif rail == rails - 1:
            going_down = False
        rail += 1 if going_down else -1
    return "".join("".join(r) for r in fence)


def rail_fence_decrypt(text, rails):
    n = len(text)
    pattern = []
    rail = 0
    going_down = True
    for i in range(n):
        pattern.append(rail)
        if rail == 0:
            going_down = True
        elif rail == rails - 1:
            going_down = False
        rail += 1 if going_down else -1
    indices = sorted(range(n), key=lambda i: pattern[i])
    result = [''] * n
    for i, idx in enumerate(indices):
        result[idx] = text[i]
    return "".join(result)


def columnar_encrypt(text, key):
    key_order = sorted(range(len(key)), key=lambda i: key[i])
    num_cols = len(key)
    padded = text + '_' * ((-len(text)) % num_cols)
    rows = [padded[i:i + num_cols] for i in range(0, len(padded), num_cols)]
    return "".join("".join(row[col] for row in rows) for col in key_order)


def simple_substitution_encrypt(text, alphabet_map):
    return "".join(alphabet_map.get(ch, ch) for ch in text)


def simple_substitution_decrypt(text, alphabet_map):
    rev = {v: k for k, v in alphabet_map.items()}
    return "".join(rev.get(ch, ch) for ch in text)


def _miller_rabin(n, a):
    if n % a == 0:
        return n == a
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    x = mod_pow(a, d, n)
    if x == 1 or x == n - 1:
        return True
    for _ in range(r - 1):
        x = (x * x) % n
        if x == n - 1:
            return True
    return False


def is_prime_miller_rabin(n, witnesses=None):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    if witnesses is None:
        witnesses = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    return all(_miller_rabin(n, a) for a in witnesses if a < n)


def rsa_generate_keys(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("p and q must be prime")
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    if gcd(e, phi) != 1:
        e = 3
        while gcd(e, phi) != 1:
            e += 2
    d = mod_inverse(e, phi)
    return (e, n), (d, n)


def rsa_encrypt(message, public_key):
    e, n = public_key
    if isinstance(message, str):
        return [mod_pow(ord(ch), e, n) for ch in message]
    return mod_pow(message, e, n)


def rsa_decrypt(ciphertext, private_key):
    d, n = private_key
    if isinstance(ciphertext, list):
        return "".join(chr(mod_pow(c, d, n)) for c in ciphertext)
    return mod_pow(ciphertext, d, n)


def diffie_hellman_keypair(p, g, private_key):
    return mod_pow(g, private_key, p)


def diffie_hellman_shared_secret(public_other, private_self, p):
    return mod_pow(public_other, private_self, p)


def xor_cipher(data, key):
    if isinstance(data, str):
        return "".join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))


def text_to_bits(text):
    bits = []
    for ch in text:
        b = bin(ord(ch))[2:].zfill(8)
        bits.extend(int(bit) for bit in b)
    return bits


def bits_to_text(bits):
    chars = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i + 8]
        chars.append(chr(int("".join(str(b) for b in byte), 2)))
    return "".join(chars)


def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("strings must be the same length")
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))


def checksum_sum(data):
    return sum(ord(c) if isinstance(c, str) else c for c in data) % 256


def checksum_xor(data):
    result = 0
    for c in data:
        result ^= ord(c) if isinstance(c, str) else c
    return result


def luhn_check(number):
    digits = [int(d) for d in str(number)]
    digits.reverse()
    total = 0
    for i, d in enumerate(digits):
        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0


def luhn_generate(partial):
    partial = str(partial)
    for check_digit in range(10):
        if luhn_check(int(partial + str(check_digit))):
            return int(partial + str(check_digit))
    raise ValueError("no valid check digit found")


def mod_hash(text, m=997):
    h = 0
    for ch in text:
        h = (h * 31 + ord(ch)) % m
    return h


def rolling_hash(text, window, base=31, mod=10 ** 9 + 7):
    if window > len(text):
        return []
    h = 0
    power = 1
    for i in range(window):
        h = (h * base + ord(text[i])) % mod
        if i > 0:
            power = (power * base) % mod
    hashes = [h]
    for i in range(window, len(text)):
        h = (h - ord(text[i - window]) * power) % mod
        h = (h * base + ord(text[i])) % mod
        hashes.append(h)
    return hashes


def string_similarity_coefficient(s1, s2):
    set1 = set(s1)
    set2 = set(s2)
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    return intersection / union if union > 0 else 1.0
