# ==================================================
# CNS EXPERIMENTS - COMBINED FILE
# Experiments 1, 2, 3 and 8
# Plain Python - No external libraries
#
# Each experiment is wrapped in its own function so that
# names (gcd, mod_inverse, p, a, b, G, point_add ...) do not
# clash. Run this file and pick an experiment from the menu.
# ==================================================

import random
import math

# ##################################################
# EXPERIMENT 1: NUMBER THEORY
# ##################################################

def experiment_1():

    # EXPERIMENT 1: NUMBER THEORY
    # Plain Python - No external libraries


    # 1. EUCLIDEAN ALGORITHM

    def gcd(a, b):
        while b != 0:
            a, b = b, a % b

        return abs(a)


    # 2. EXTENDED EUCLIDEAN ALGORITHM

    def extended_gcd(a, b):
        if b == 0:
            return abs(a), (1 if a >= 0 else -1), 0

        g, x1, y1 = extended_gcd(b, a % b)

        x = y1
        y = x1 - (a // b) * y1

        return g, x, y


    # 3. MODULAR INVERSE

    def mod_inverse(a, m):
        g, x, y = extended_gcd(a, m)

        if g != 1:
            return None

        return x % m


    # 4. MODULAR EXPONENTIATION

    def mod_power(a, b, n):
        result = 1
        a = a % n

        while b > 0:
            if b % 2 == 1:
                result = (result * a) % n

            a = (a * a) % n
            b = b // 2

        return result


    # 5. EULER TOTIENT FUNCTION

    def phi(n):
        result = n
        p = 2
        temp = n

        while p * p <= temp:
            if temp % p == 0:
                while temp % p == 0:
                    temp //= p

                result -= result // p

            p += 1

        if temp > 1:
            result -= result // temp

        return result


    # 6. FERMAT PRIMALITY TEST

    def fermat_test(n, a):

        if n <= 1:
            return False

        if n == 2:
            return True

        if n % 2 == 0:
            return False

        if gcd(a, n) != 1:
            return False

        return pow(a, n - 1, n) == 1


    # 7. JACOBI SYMBOL

    def jacobi(a, n):

        if n <= 0 or n % 2 == 0:
            return 0

        a = a % n
        result = 1

        while a != 0:

            while a % 2 == 0:
                a //= 2

                if n % 8 == 3 or n % 8 == 5:
                    result = -result

            a, n = n, a

            if a % 4 == 3 and n % 4 == 3:
                result = -result

            a = a % n

        if n == 1:
            return result

        return 0


    # 8. EULER-JACOBI / SOLOVAY-STRASSEN TEST
    def euler_test(n, a):

        if n <= 1:
            return False

        if n == 2:
            return True

        if n % 2 == 0:
            return False

        if gcd(a, n) != 1:
            return False

        lhs = pow(a, (n - 1) // 2, n)

        if lhs == 1 or lhs == n - 1:
            return True
        else:
            return False


    # 9. MILLER-RABIN PRIMALITY TEST

    def miller_rabin(n, a):

        if n <= 1:
            return False

        if n == 2 or n == 3:
            return True

        if n % 2 == 0:
            return False

        if not (2 <= a <= n - 2):
            return False

        if gcd(a, n) != 1:
            return False

        d = n - 1
        s = 0

        while d % 2 == 0:
            d //= 2
            s += 1

        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            return True

        for i in range(s - 1):
            x = (x * x) % n

            if x == n - 1:
                return True

        return False


    # 10. CHINESE REMAINDER THEOREM

    def crt(remainders, moduli):

        M = 1

        for m in moduli:
            M *= m

        for i in range(len(moduli)):
            for j in range(i + 1, len(moduli)):
                if gcd(moduli[i], moduli[j]) != 1:
                    return None

        result = 0

        for i in range(len(moduli)):

            Mi = M // moduli[i]

            inverse = mod_inverse(Mi, moduli[i])

            if inverse is None:
                return None

            result += remainders[i] * Mi * inverse

        return result % M


    # 11. PRIME FACTORIZATION

    def prime_factors(n):

        factors = []
        divisor = 2

        while divisor * divisor <= n:

            while n % divisor == 0:
                factors.append(divisor)
                n //= divisor

            divisor += 1

        if n > 1:
            factors.append(n)

        return factors


    # 12. DETERMINISTIC PRIME CHECK

    def is_prime(n):

        if n <= 1:
            return False

        if n <= 3:
            return True

        if n % 2 == 0 or n % 3 == 0:
            return False

        i = 5

        while i * i <= n:

            if n % i == 0 or n % (i + 2) == 0:
                return False

            i += 6

        return True


    # 13. COMPARISON OF PRIMALITY TESTS

    def compare_tests(n, bases):

        print("\nNumber:", n)

        for a in bases:

            print("\nBase:", a)

            if not (2 <= a <= n - 2):
                print("Invalid base for this number")
                continue

            print("Fermat:",
                  "Probably Prime" if fermat_test(n, a)
                  else "Composite")

            print("Euler-Jacobi:",
                  "Probably Prime" if euler_test(n, a)
                  else "Composite")

            print("Miller-Rabin:",
                  "Probably Prime" if miller_rabin(n, a)
                  else "Composite")


    # MAIN MENU

    while True:

        print("\n========== NUMBER THEORY MENU ==========")
        print("1. Division Algorithm")
        print("2. GCD")
        print("3. Extended Euclidean Algorithm")
        print("4. Modular Arithmetic")
        print("5. Modular Exponentiation")
        print("6. Modular Inverse")
        print("7. Euler Totient Function")
        print("8. Fermat Primality Test")
        print("9. Euler-Jacobi Test")
        print("10. Miller-Rabin Test")
        print("11. Chinese Remainder Theorem")
        print("12. Prime Factorization")
        print("13. Euler's Theorem")
        print("14. Compare Primality Tests")
        print("15. Basic Prime Check")
        print("0. Exit")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:

            a = int(input("Enter a: "))
            b = int(input("Enter b: "))

            if b == 0:
                print("Division by zero not allowed")
            else:
                q, r = divmod(a, abs(b))

                if b < 0:
                    q = -q

                print("Quotient:", q)
                print("Remainder:", r)
                print("Verification:", a, "=", b, "*", q, "+", r)

        elif choice == 2:

            a = int(input("Enter a: "))
            b = int(input("Enter b: "))

            print("GCD =", gcd(a, b))

        elif choice == 3:

            a = int(input("Enter a: "))
            b = int(input("Enter b: "))

            g, x, y = extended_gcd(a, b)

            print("GCD =", g)
            print("x =", x)
            print("y =", y)
            print("Verification =", a*x + b*y)

        elif choice == 4:

            a = int(input("Enter number: "))
            m = int(input("Enter modulus: "))

            if m <= 0:
                print("Invalid modulus")
            else:
                print("Result =", a % m)

        elif choice == 5:

            a = int(input("Enter base: "))
            b = int(input("Enter exponent: "))
            n = int(input("Enter modulus: "))

            if b < 0 or n <= 0:
                print("Invalid input")
            else:
                print("Result =", mod_power(a, b, n))

        elif choice == 6:

            a = int(input("Enter a: "))
            m = int(input("Enter modulus: "))

            if m <= 0:
                print("Invalid modulus")
            else:
                ans = mod_inverse(a, m)

                if ans is None:
                    print("Inverse does not exist")
                else:
                    print("Modular inverse =", ans)

        elif choice == 7:

            n = int(input("Enter n: "))

            if n <= 0:
                print("Enter a positive integer")
            else:
                print("Phi(n) =", phi(n))

        elif choice == 8:

            n = int(input("Enter number: "))
            a = int(input("Enter base: "))

            if fermat_test(n, a):
                print("Probably Prime")
            else:
                print("Composite")

        elif choice == 9:

            n = int(input("Enter number: "))
            a = int(input("Enter base: "))

            if euler_test(n, a):
                print("Probably Prime")
            else:
                print("Composite")

        elif choice == 10:

            n = int(input("Enter number: "))
            a = int(input("Enter base: "))

            if miller_rabin(n, a):
                print("Probably Prime")
            else:
                print("Composite")

        elif choice == 11:

            count = int(input("Enter number of equations: "))

            remainders = []
            moduli = []

            for i in range(count):
                a = int(input("Enter remainder: "))
                m = int(input("Enter modulus: "))

                if m <= 1:
                    print("Modulus must be greater than 1")
                    break

                remainders.append(a)
                moduli.append(m)

            else:
                ans = crt(remainders, moduli)

                if ans is None:
                    print("Moduli must be pairwise coprime")
                else:
                    print("CRT solution =", ans)

        elif choice == 12:

            n = int(input("Enter number: "))

            if n <= 1:
                print("Enter a number greater than 1")
            else:
                print("Prime factors =", prime_factors(n))

        elif choice == 13:

            a = int(input("Enter a: "))
            n = int(input("Enter n: "))

            if n <= 0:
                print("Invalid modulus")

            elif gcd(a, n) != 1:
                print("Euler's theorem cannot be applied")

            else:
                result = phi(n)

                print("Phi(n) =", result)
                print("a^phi(n) mod n =", pow(a, result, n))

        elif choice == 14:

            n = int(input("Enter number: "))

            bases = list(map(int, input(
                "Enter bases separated by spaces: "
            ).split()))

            compare_tests(n, bases)

        elif choice == 15:

            n = int(input("Enter number: "))

            if is_prime(n):
                print(n, "is prime")
            else:
                print(n, "is composite")

        elif choice == 0:

            print("Program terminated")
            break

        else:

            print("Invalid choice")


# ##################################################
# EXPERIMENT 2: CLASSICAL SYMMETRIC CIPHERS (Caesar, Monoalphabetic, Vigenere, Playfair, Hill)
# ##################################################

def experiment_2():

    # EXPERIMENT 2: CLASSICAL SYMMETRIC CIPHERS
    # Caesar, Monoalphabetic, Vigenere, Playfair and Hill
    # UID-based key generation


    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


    # --------------------------------------------------
    # 1. CAESAR CIPHER
    # --------------------------------------------------

    def caesar_encrypt(text, key):
        result = ""

        for ch in text:
            if ch.isalpha():
                base = ord('A') if ch.isupper() else ord('a')
                result += chr((ord(ch) - base + key) % 26 + base)
            else:
                result += ch

        return result


    def caesar_decrypt(text, key):
        return caesar_encrypt(text, -key)


    def caesar_key(uid):
        total = sum(int(digit) for digit in uid)
        return (total % 25) + 1


    # --------------------------------------------------
    # 2. MONOALPHABETIC SUBSTITUTION CIPHER
    # --------------------------------------------------

    def mono_key(uid):
        random.seed(int(uid))

        letters = list(ALPHABET)
        random.shuffle(letters)

        return ''.join(letters)


    def mono_encrypt(text, key):
        result = ""

        for ch in text:
            if ch.isalpha():
                if ch.isupper():
                    result += key[ord(ch) - ord('A')]
                else:
                    result += key[ord(ch.upper()) - ord('A')].lower()
            else:
                result += ch

        return result


    def mono_decrypt(text, key):
        result = ""

        for ch in text:
            if ch.isalpha():
                if ch.isupper():
                    result += ALPHABET[key.index(ch)]
                else:
                    result += ALPHABET[key.upper().index(ch.upper())].lower()
            else:
                result += ch

        return result


    # --------------------------------------------------
    # 3. VIGENERE CIPHER
    # --------------------------------------------------

    def vigenere_key(uid):
        groups = [uid[i:i+2] for i in range(0, 10, 2)]

        keyword = ""

        for group in groups:
            value = int(group) % 26
            keyword += chr(value + ord('A'))

        return keyword


    def vigenere_encrypt(text, key):
        result = ""
        j = 0

        for ch in text:
            if ch.isalpha():
                shift = ord(key[j % len(key)]) - ord('A')

                if ch.isupper():
                    result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
                else:
                    result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))

                j += 1
            else:
                result += ch

        return result


    def vigenere_decrypt(text, key):
        result = ""
        j = 0

        for ch in text:
            if ch.isalpha():
                shift = ord(key[j % len(key)]) - ord('A')

                if ch.isupper():
                    result += chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
                else:
                    result += chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))

                j += 1
            else:
                result += ch

        return result


    # --------------------------------------------------
    # 4. PLAYFAIR CIPHER
    # --------------------------------------------------

    def playfair_key(uid):
        key = vigenere_key(uid)

        unique = ""

        for ch in key:
            if ch not in unique:
                unique += ch

        return unique


    def playfair_matrix(key):
        key = key + ALPHABET
        unique = ""

        for ch in key:
            if ch not in unique and ch != 'J':
                unique += ch

        matrix = []

        for i in range(0, 25, 5):
            matrix.append(list(unique[i:i+5]))

        return matrix


    def playfair_position(matrix, ch):
        if ch == 'J':
            ch = 'I'

        for i in range(5):
            for j in range(5):
                if matrix[i][j] == ch:
                    return i, j

        return None


    def playfair_prepare(text):
        text = ''.join(ch for ch in text.upper() if ch.isalpha())
        text = text.replace('J', 'I')

        result = ""
        i = 0

        while i < len(text):
            a = text[i]

            if i + 1 >= len(text):
                result += a + 'X'
                i += 1

            elif a == text[i+1]:
                result += a + 'X'
                i += 1

            else:
                result += a + text[i+1]
                i += 2

        return result


    def playfair_encrypt(text, key):
        matrix = playfair_matrix(key)
        text = playfair_prepare(text)

        result = ""

        for i in range(0, len(text), 2):
            a = text[i]
            b = text[i+1]

            r1, c1 = playfair_position(matrix, a)
            r2, c2 = playfair_position(matrix, b)

            if r1 == r2:
                result += matrix[r1][(c1+1) % 5]
                result += matrix[r2][(c2+1) % 5]

            elif c1 == c2:
                result += matrix[(r1+1) % 5][c1]
                result += matrix[(r2+1) % 5][c2]

            else:
                result += matrix[r1][c2]
                result += matrix[r2][c1]

        return result


    def playfair_decrypt(text, key):
        matrix = playfair_matrix(key)
        result = ""

        for i in range(0, len(text), 2):
            a = text[i]
            b = text[i+1]

            r1, c1 = playfair_position(matrix, a)
            r2, c2 = playfair_position(matrix, b)

            if r1 == r2:
                result += matrix[r1][(c1-1) % 5]
                result += matrix[r2][(c2-1) % 5]

            elif c1 == c2:
                result += matrix[(r1-1) % 5][c1]
                result += matrix[(r2-1) % 5][c2]

            else:
                result += matrix[r1][c2]
                result += matrix[r2][c1]

        return result


    # --------------------------------------------------
    # 5. HILL CIPHER
    # --------------------------------------------------

    def hill_key(uid):

        # Take the first eight UID digits in groups of two.
        values = [
            int(uid[0:2]),
            int(uid[2:4]),
            int(uid[4:6]),
            int(uid[6:8])
        ]

        a, b, c, d = [x % 26 for x in values]

        # First try changing only the bottom-right element.
        for i in range(26):
            new_d = (d + i) % 26
            det = (a * new_d - b * c) % 26

            if math.gcd(det, 26) == 1:
                return [[a, b], [c, new_d]]

        # If impossible, adjust the top-left element too.
        # This is needed if the original matrix cannot be
        # made invertible by changing only the bottom-right.
        for i in range(1, 27):
            new_a = (a + i) % 26

            for j in range(26):
                new_d = (d + j) % 26
                det = (new_a * new_d - b * c) % 26

                if math.gcd(det, 26) == 1:
                    print("Note: Top-left element also adjusted.")
                    return [[new_a, b], [c, new_d]]

        return None


    def matrix_inverse(key):

        a, b = key[0]
        c, d = key[1]

        det = (a*d - b*c) % 26

        det_inv = None

        for i in range(26):
            if (det * i) % 26 == 1:
                det_inv = i
                break

        if det_inv is None:
            return None

        inverse = [
            [(d * det_inv) % 26, (-b * det_inv) % 26],
            [(-c * det_inv) % 26, (a * det_inv) % 26]
        ]

        return inverse


    def hill_encrypt(text, key):

        text = ''.join(ch for ch in text.upper() if ch.isalpha())

        if len(text) % 2 != 0:
            text += 'X'

        result = ""

        for i in range(0, len(text), 2):

            x = ord(text[i]) - ord('A')
            y = ord(text[i+1]) - ord('A')

            a = (key[0][0]*x + key[0][1]*y) % 26
            b = (key[1][0]*x + key[1][1]*y) % 26

            result += chr(a + ord('A'))
            result += chr(b + ord('A'))

        return result


    def hill_decrypt(text, key):

        inverse = matrix_inverse(key)

        if inverse is None:
            return None

        result = ""

        for i in range(0, len(text), 2):

            x = ord(text[i]) - ord('A')
            y = ord(text[i+1]) - ord('A')

            a = (inverse[0][0]*x + inverse[0][1]*y) % 26
            b = (inverse[1][0]*x + inverse[1][1]*y) % 26

            result += chr(a + ord('A'))
            result += chr(b + ord('A'))

        return result


    # --------------------------------------------------
    # HELPER FUNCTIONS FOR ANALYSIS
    # --------------------------------------------------

    def clean_text(text):
        return ''.join(ch for ch in text.upper() if ch.isalpha())


    def frequency(text):
        text = clean_text(text)

        print("\nFrequency Distribution:")

        for ch in ALPHABET:
            count = text.count(ch)

            if count > 0:
                print(ch, ":", count)


    def changed_characters(text1, text2):
        count = 0

        for a, b in zip(text1, text2):
            if a != b:
                count += 1

        return count


    def modify_one_character(text):
        chars = list(text)

        for i in range(len(chars)):
            if chars[i].isalpha():
                if chars[i].upper() == 'A':
                    chars[i] = 'B'
                else:
                    chars[i] = 'A'
                return ''.join(chars)

        return text


    # --------------------------------------------------
    # MAIN PROGRAM
    # --------------------------------------------------

    uid = input("Enter your 10-digit UID: ")

    if len(uid) != 10 or not uid.isdigit():
        print("Invalid UID. Enter exactly 10 digits.")
        return

    plaintext = input("\nEnter plaintext: ")

    # Generate all keys

    ck = caesar_key(uid)
    mk = mono_key(uid)
    vk = vigenere_key(uid)
    pk = playfair_key(uid)
    hk = hill_key(uid)

    print("\n========== GENERATED KEYS ==========")

    print("Caesar Key:", ck)
    print("Monoalphabetic Key:", mk)
    print("Vigenere Key:", vk)
    print("Playfair Keyword:", pk)
    print("Playfair Matrix:")

    matrix = playfair_matrix(pk)

    for row in matrix:
        print(row)

    print("Hill Key:", hk)


    # Encrypt and decrypt

    print("\n========== ENCRYPTION AND DECRYPTION ==========")

    c1 = caesar_encrypt(plaintext, ck)
    d1 = caesar_decrypt(c1, ck)

    print("\n1. CAESAR")
    print("Ciphertext:", c1)
    print("Decrypted:", d1)
    print("Verified:", d1 == plaintext)


    c2 = mono_encrypt(plaintext, mk)
    d2 = mono_decrypt(c2, mk)

    print("\n2. MONOALPHABETIC")
    print("Ciphertext:", c2)
    print("Decrypted:", d2)
    print("Verified:", d2 == plaintext)


    c3 = vigenere_encrypt(plaintext, vk)
    d3 = vigenere_decrypt(c3, vk)

    print("\n3. VIGENERE")
    print("Ciphertext:", c3)
    print("Decrypted:", d3)
    print("Verified:", d3 == plaintext)


    c4 = playfair_encrypt(plaintext, pk)
    d4 = playfair_decrypt(c4, pk)

    print("\n4. PLAYFAIR")
    print("Ciphertext:", c4)
    print("Decrypted (may contain filler X):", d4)
    print("Prepared plaintext:", playfair_prepare(plaintext))
    print("Verified:", d4 == playfair_prepare(plaintext))


    c5 = hill_encrypt(plaintext, hk)
    d5 = hill_decrypt(c5, hk)

    hill_plain = clean_text(plaintext)

    if len(hill_plain) % 2 != 0:
        hill_plain += 'X'

    print("\n5. HILL")
    print("Ciphertext:", c5)
    print("Decrypted (may contain padding X):", d5)
    print("Expected padded plaintext:", hill_plain)
    print("Verified:", d5 == hill_plain)


    # --------------------------------------------------
    # PART A: CONFUSION
    # Change last UID digit by +1 modulo 10
    # --------------------------------------------------

    print("\n========== PART A: CONFUSION ==========")

    new_last_digit = (int(uid[-1]) + 1) % 10
    new_uid = uid[:9] + str(new_last_digit)

    new_ck = caesar_key(new_uid)
    new_mk = mono_key(new_uid)
    new_vk = vigenere_key(new_uid)
    new_pk = playfair_key(new_uid)
    new_hk = hill_key(new_uid)

    print("Original UID:", uid)
    print("Modified UID:", new_uid)

    print("\nCaesar changed characters:",
          changed_characters(c1, caesar_encrypt(plaintext, new_ck)))

    print("Monoalphabetic changed characters:",
          changed_characters(c2, mono_encrypt(plaintext, new_mk)))

    print("Vigenere changed characters:",
          changed_characters(c3, vigenere_encrypt(plaintext, new_vk)))

    print("Playfair changed characters:",
          changed_characters(c4, playfair_encrypt(plaintext, new_pk)))

    print("Hill changed characters:",
          changed_characters(c5, hill_encrypt(plaintext, new_hk)))


    # --------------------------------------------------
    # PART B AND C: DIFFUSION AND AVALANCHE EFFECT
    # --------------------------------------------------

    print("\n========== PART B AND C: DIFFUSION / AVALANCHE ==========")

    modified_text = modify_one_character(plaintext)

    print("Original Plaintext:", plaintext)
    print("Modified Plaintext:", modified_text)

    print("\nNumber of changed ciphertext characters:")

    print("Caesar:",
          changed_characters(c1, caesar_encrypt(modified_text, ck)))

    print("Monoalphabetic:",
          changed_characters(c2, mono_encrypt(modified_text, mk)))

    print("Vigenere:",
          changed_characters(c3, vigenere_encrypt(modified_text, vk)))

    print("Playfair:",
          changed_characters(c4, playfair_encrypt(modified_text, pk)))

    print("Hill:",
          changed_characters(c5, hill_encrypt(modified_text, hk)))


    # --------------------------------------------------
    # PART D: FREQUENCY DISTRIBUTION
    # --------------------------------------------------

    print("\n========== PART D: FREQUENCY DISTRIBUTION ==========")

    print("\nPlaintext")
    frequency(plaintext)

    print("\nCaesar Ciphertext")
    frequency(c1)

    print("\nMonoalphabetic Ciphertext")
    frequency(c2)

    print("\nVigenere Ciphertext")
    frequency(c3)

    print("\nPlayfair Ciphertext")
    frequency(c4)

    print("\nHill Ciphertext")
    frequency(c5)


    # --------------------------------------------------
    # END
    # --------------------------------------------------

    print("\n========== EXPERIMENT COMPLETED ==========")


# ##################################################
# EXPERIMENT 3: ASYMMETRIC CRYPTOGRAPHY (RSA, Diffie-Hellman, ElGamal, ECC)
# ##################################################

def experiment_3():

    # EXPERIMENT 3: ASYMMETRIC CRYPTOGRAPHY
    # RSA, Diffie-Hellman, ElGamal and ECC
    # Plain Python - No external libraries


    # --------------------------------------------------
    # COMMON FUNCTIONS
    # --------------------------------------------------

    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return abs(a)


    def extended_gcd(a, b):
        if b == 0:
            return abs(a), 1, 0

        g, x1, y1 = extended_gcd(b, a % b)

        x = y1
        y = x1 - (a // b) * y1

        return g, x, y


    def mod_inverse(a, m):
        g, x, y = extended_gcd(a, m)

        if g != 1:
            return None

        return x % m


    # --------------------------------------------------
    # 1. RSA ALGORITHM
    # --------------------------------------------------

    def rsa_key_generation(p, q, e):

        n = p * q
        phi = (p - 1) * (q - 1)

        if gcd(e, phi) != 1:
            return None

        d = mod_inverse(e, phi)

        public_key = (e, n)
        private_key = (d, n)

        return public_key, private_key, phi


    def rsa_encrypt(message, public_key):

        e, n = public_key

        if message < 0 or message >= n:
            return None

        cipher = pow(message, e, n)

        return cipher


    def rsa_decrypt(cipher, private_key):

        d, n = private_key

        message = pow(cipher, d, n)

        return message


    def rsa():

        print("\n========== RSA ALGORITHM ==========")

        p = int(input("Enter prime number p: "))
        q = int(input("Enter prime number q: "))
        e = int(input("Enter public exponent e: "))

        if p == q or p <= 1 or q <= 1:
            print("Invalid prime inputs")
            return

        result = rsa_key_generation(p, q, e)

        if result is None:
            print("Invalid public exponent")
            return

        public_key, private_key, phi = result

        print("\nn =", p * q)
        print("Phi(n) =", phi)

        print("Public Key:", public_key)
        print("Private Key:", private_key)

        message = int(input("Enter numerical message: "))

        cipher = rsa_encrypt(message, public_key)

        if cipher is None:
            print("Message must be between 0 and n-1")
            return

        print("Encrypted Message:", cipher)

        decrypted = rsa_decrypt(cipher, private_key)

        print("Decrypted Message:", decrypted)


    # --------------------------------------------------
    # 2. DIFFIE-HELLMAN KEY EXCHANGE
    # --------------------------------------------------

    def diffie_hellman():

        print("\n========== DIFFIE-HELLMAN ==========")

        p = int(input("Enter prime number p: "))
        g = int(input("Enter primitive root g: "))

        a = int(input("Enter Alice private key: "))
        b = int(input("Enter Bob private key: "))

        if p <= 2 or not (1 <= a < p - 1) or not (1 <= b < p - 1):
            print("Invalid input")
            return

        # Alice calculates public key
        A = pow(g, a, p)

        # Bob calculates public key
        B = pow(g, b, p)

        print("\nAlice Public Key:", A)
        print("Bob Public Key:", B)

        # Both calculate shared secret
        secret_A = pow(B, a, p)
        secret_B = pow(A, b, p)

        print("\nAlice Shared Secret:", secret_A)
        print("Bob Shared Secret:", secret_B)

        if secret_A == secret_B:
            print("Key Exchange Successful")
        else:
            print("Key Exchange Failed")


    # --------------------------------------------------
    # 3. ELGAMAL ENCRYPTION AND DECRYPTION
    # --------------------------------------------------

    def elgamal():

        print("\n========== ELGAMAL ALGORITHM ==========")

        p = int(input("Enter prime number p: "))
        g = int(input("Enter primitive root g: "))

        x = int(input("Enter private key: "))

        if p <= 2 or not (1 <= x <= p - 2):
            print("Invalid input")
            return

        # Public key
        y = pow(g, x, p)

        print("Public Key:", (p, g, y))
        print("Private Key:", x)

        message = int(input("Enter numerical message: "))
        k = int(input("Enter random integer k: "))

        if not (0 <= message < p):
            print("Message must be between 0 and p-1")
            return

        if not (1 <= k <= p - 2):
            print("Invalid k")
            return

        # Encryption
        c1 = pow(g, k, p)
        c2 = (message * pow(y, k, p)) % p

        print("\nCiphertext:", (c1, c2))

        # Decryption
        shared = pow(c1, x, p)

        inverse = mod_inverse(shared, p)

        decrypted = (c2 * inverse) % p

        print("Decrypted Message:", decrypted)


    # --------------------------------------------------
    # 4. ELLIPTIC CURVE CRYPTOGRAPHY
    # --------------------------------------------------

    # Curve equation:
    # y^2 = x^3 + ax + b (mod p)

    p = 17
    a = 2
    b = 2

    # Generator point
    G = (5, 1)

    # Point at infinity = None


    def point_add(P, Q):

        if P is None:
            return Q

        if Q is None:
            return P

        x1, y1 = P
        x2, y2 = Q

        # Inverse points
        if x1 == x2 and (y1 + y2) % p == 0:
            return None

        # Point doubling
        if P == Q:

            denominator = (2 * y1) % p

            inverse = mod_inverse(denominator, p)

            if inverse is None:
                return None

            numerator = (3 * x1 * x1 + a) % p

            slope = (numerator * inverse) % p

        # Point addition
        else:

            denominator = (x2 - x1) % p

            inverse = mod_inverse(denominator, p)

            if inverse is None:
                return None

            numerator = (y2 - y1) % p

            slope = (numerator * inverse) % p

        x3 = (slope * slope - x1 - x2) % p

        y3 = (slope * (x1 - x3) - y1) % p

        return (x3, y3)


    def point_multiply(k, P):

        result = None
        current = P

        while k > 0:

            if k % 2 == 1:
                result = point_add(result, current)

            current = point_add(current, current)

            k //= 2

        return result


    # --------------------------------------------------
    # ECC KEY GENERATION AND KEY EXCHANGE
    # --------------------------------------------------

    def ecc_key_exchange():

        print("\n========== ECC KEY EXCHANGE ==========")

        print("Curve: y^2 = x^3 + 2x + 2 mod 17")
        print("Generator Point:", G)

        alice_private = int(input("Enter Alice private key: "))
        bob_private = int(input("Enter Bob private key: "))

        if not (1 <= alice_private <= 18) or not (1 <= bob_private <= 18):
            print("Private keys must be between 1 and 18")
            return

        # Public keys
        alice_public = point_multiply(alice_private, G)
        bob_public = point_multiply(bob_private, G)

        print("\nAlice Public Key:", alice_public)
        print("Bob Public Key:", bob_public)

        # Shared secret
        secret_A = point_multiply(alice_private, bob_public)
        secret_B = point_multiply(bob_private, alice_public)

        print("\nAlice Shared Secret:", secret_A)
        print("Bob Shared Secret:", secret_B)

        if secret_A == secret_B:
            print("ECC Key Exchange Successful")
        else:
            print("ECC Key Exchange Failed")


    # --------------------------------------------------
    # ECC ELGAMAL ENCRYPTION AND DECRYPTION
    # --------------------------------------------------

    def ecc_elgamal():

        print("\n========== ECC ELGAMAL ==========")

        print("Generator Point:", G)

        private_key = int(input("Enter private key: "))
        k = int(input("Enter random integer k: "))

        if not (1 <= private_key <= 18) or not (1 <= k <= 18):
            print("Private key and k must be between 1 and 18")
            return

        # Public key
        public_key = point_multiply(private_key, G)

        print("Public Key:", public_key)

        # Message point (using generator point for demonstration)
        message_point = G

        print("Message Point:", message_point)

        # Encryption
        C1 = point_multiply(k, G)

        shared = point_multiply(k, public_key)

        C2 = point_add(message_point, shared)

        print("\nCiphertext:", (C1, C2))

        # Decryption
        shared = point_multiply(private_key, C1)

        # Find negative of shared point
        negative_shared = (shared[0], (-shared[1]) % p)

        decrypted = point_add(C2, negative_shared)

        print("Decrypted Message Point:", decrypted)

        if decrypted == message_point:
            print("ECC ElGamal Successful")
        else:
            print("ECC ElGamal Failed")


    # --------------------------------------------------
    # MAIN MENU
    # --------------------------------------------------

    while True:

        print("\n========== ASYMMETRIC CRYPTOGRAPHY MENU ==========")

        print("1. RSA")
        print("2. Diffie-Hellman")
        print("3. ElGamal")
        print("4. ECC Key Exchange")
        print("5. ECC ElGamal")
        print("0. Exit")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            rsa()

        elif choice == 2:
            diffie_hellman()

        elif choice == 3:
            elgamal()

        elif choice == 4:
            ecc_key_exchange()

        elif choice == 5:
            ecc_elgamal()

        elif choice == 0:
            print("Program terminated")
            break

        else:
            print("Invalid choice")


# ##################################################
# EXPERIMENT 8: DIGITAL SIGNATURES (RSA, ElGamal, ECDSA)
# ##################################################

def experiment_8():

    # EXPERIMENT 8: DIGITAL SIGNATURES
    # RSA, ElGamal and ECDSA
    # Plain Python - No external libraries

    # --------------------------------------------------
    # COMMON MATHEMATICAL FUNCTIONS
    # --------------------------------------------------

    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a


    def extended_gcd(a, b):
        if b == 0:
            return a, 1, 0

        g, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1

        return g, x, y


    def mod_inverse(a, m):
        g, x, y = extended_gcd(a, m)

        if g != 1:
            raise ValueError("Modular inverse does not exist")

        return x % m


    def mod_power(base, exponent, modulus):
        result = 1
        base = base % modulus

        while exponent > 0:
            if exponent % 2 == 1:
                result = (result * base) % modulus

            base = (base * base) % modulus
            exponent //= 2

        return result


    # --------------------------------------------------
    # SIMPLE MESSAGE HASH
    # Educational hash for demonstrating signatures only
    # --------------------------------------------------

    def message_hash(message, modulus):
        value = 0

        for ch in message:
            value = (value * 31 + ord(ch)) % modulus

        return value


    # --------------------------------------------------
    # 1. RSA DIGITAL SIGNATURE
    # --------------------------------------------------

    def rsa_signature(message):
        print("\n========== RSA DIGITAL SIGNATURE ==========")

        # Small example primes for demonstration
        p = 61
        q = 53

        n = p * q
        phi = (p - 1) * (q - 1)

        e = 17
        d = mod_inverse(e, phi)

        h = message_hash(message, n)

        # Sender signs using private key
        signature = mod_power(h, d, n)

        # Receiver verifies using public key
        verified_hash = mod_power(signature, e, n)

        print("Message:", message)
        print("Public Key:", (e, n))
        print("Private Key:", (d, n))
        print("Message Hash:", h)
        print("Digital Signature:", signature)

        if verified_hash == h:
            print("Signature Verification: VALID")
        else:
            print("Signature Verification: INVALID")

        # Tampering test
        modified_message = message + " changed"
        modified_hash = message_hash(modified_message, n)

        print("\nTampered Message:", modified_message)

        if verified_hash == modified_hash:
            print("Tampering Test: NOT DETECTED")
        else:
            print("Tampering Test: DETECTED")


    # --------------------------------------------------
    # 2. ELGAMAL DIGITAL SIGNATURE
    # --------------------------------------------------

    def elgamal_signature(message):
        print("\n========== ELGAMAL DIGITAL SIGNATURE ==========")

        p = 23
        g = 5

        # Private key
        x = 6

        # Public key
        y = mod_power(g, x, p)

        h = message_hash(message, p - 1)

        # Choose k such that gcd(k, p-1) = 1
        k = 7

        r = mod_power(g, k, p)

        k_inverse = mod_inverse(k, p - 1)

        s = ((h - x * r) * k_inverse) % (p - 1)

        print("Message:", message)
        print("Public Key:", (p, g, y))
        print("Private Key:", x)
        print("Message Hash:", h)
        print("Signature:", (r, s))

        # Verification
        left = mod_power(g, h, p)

        right = (
            mod_power(y, r, p) *
            mod_power(r, s, p)
        ) % p

        if left == right:
            print("Signature Verification: VALID")
        else:
            print("Signature Verification: INVALID")

        # Tampering test
        modified_message = message + " changed"
        modified_hash = message_hash(modified_message, p - 1)

        modified_left = mod_power(g, modified_hash, p)

        if modified_left == right:
            print("Tampering Test: NOT DETECTED")
        else:
            print("Tampering Test: DETECTED")


    # --------------------------------------------------
    # 3. ELLIPTIC CURVE DIGITAL SIGNATURE (ECDSA)
    # --------------------------------------------------

    # Curve: y^2 = x^3 + ax + b mod p

    p = 17
    a = 2
    b = 2

    G = (5, 1)

    # Point at infinity is represented by None


    def point_add(P, Q):
        if P is None:
            return Q

        if Q is None:
            return P

        x1, y1 = P
        x2, y2 = Q

        if x1 == x2 and (y1 + y2) % p == 0:
            return None

        if P == Q:
            numerator = (3 * x1 * x1 + a) % p
            denominator = mod_inverse((2 * y1) % p, p)
        else:
            numerator = (y2 - y1) % p
            denominator = mod_inverse((x2 - x1) % p, p)

        slope = (numerator * denominator) % p

        x3 = (slope * slope - x1 - x2) % p
        y3 = (slope * (x1 - x3) - y1) % p

        return (x3, y3)


    def point_multiply(k, P):
        result = None
        current = P

        while k > 0:
            if k % 2 == 1:
                result = point_add(result, current)

            current = point_add(current, current)
            k //= 2

        return result


    def ecdsa_signature(message):
        print("\n========== ECDSA DIGITAL SIGNATURE ==========")

        # Private key
        private_key = 5

        # Generator order for this small curve is 19
        n = 19

        # Public key
        public_key = point_multiply(private_key, G)

        h = message_hash(message, n)

        # Nonce
        k = 7

        # Calculate R = kG
        R = point_multiply(k, G)

        r = R[0] % n

        # Calculate s
        k_inverse = mod_inverse(k, n)

        s = (k_inverse * (h + private_key * r)) % n

        print("Message:", message)
        print("Generator:", G)
        print("Public Key:", public_key)
        print("Private Key:", private_key)
        print("Message Hash:", h)
        print("Signature:", (r, s))

        # Verification
        w = mod_inverse(s, n)

        u1 = (h * w) % n
        u2 = (r * w) % n

        P1 = point_multiply(u1, G)
        P2 = point_multiply(u2, public_key)

        X = point_add(P1, P2)

        if X is not None and X[0] % n == r:
            print("Signature Verification: VALID")
        else:
            print("Signature Verification: INVALID")

        # Tampering test
        modified_message = message + " changed"
        modified_hash = message_hash(modified_message, n)

        u1_modified = (modified_hash * w) % n
        P1_modified = point_multiply(u1_modified, G)
        X_modified = point_add(P1_modified, P2)

        if X_modified is not None and X_modified[0] % n == r:
            print("Tampering Test: NOT DETECTED")
        else:
            print("Tampering Test: DETECTED")


    # --------------------------------------------------
    # MAIN PROGRAM
    # --------------------------------------------------

    message = input("Enter message to sign: ")

    print("\nOriginal Message:", message)

    rsa_signature(message)

    elgamal_signature(message)

    ecdsa_signature(message)

    print("\n========== EXPERIMENT COMPLETED ==========")


# ##################################################
# MASTER MENU
# ##################################################

def main():
    while True:
        print("\n========== CNS EXPERIMENTS ==========")
        print("1. Experiment 1: Number Theory")
        print("2. Experiment 2: Classical Symmetric Ciphers")
        print("3. Experiment 3: Asymmetric Cryptography")
        print("8. Experiment 8: Digital Signatures")
        print("0. Exit")

        choice = input("\nSelect experiment: ").strip()

        if choice == "1":
            experiment_1()
        elif choice == "2":
            experiment_2()
        elif choice == "3":
            experiment_3()
        elif choice == "8":
            experiment_8()
        elif choice == "0":
            print("Program terminated")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
