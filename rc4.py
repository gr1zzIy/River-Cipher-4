def crypt(key: bytes, string: bytes) -> str:
    # Ініціалізація масиву t
    t = list(range(256))
    j = 0
    k = len(key)

    # Ініціалізація t за допомогою ключа
    for i in range(256):
        j = (j + t[i] + key[i % k]) % 256
        t[i], t[j] = t[j], t[i]

    # Генерація потоку шифрування
    a = b = 0
    codes = []

    for i in range(len(string)):
        a = (a + 1) % 256
        b = (b + t[a]) % 256
        t[a], t[b] = t[b], t[a]
        codes.append(f"{string[i] ^ t[(t[a] + t[b]) % 256]:02X}")

    return " ".join(codes)
