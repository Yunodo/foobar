import itertools

def primes():
    candidates = itertools.count(2)
    multiples = {}
    while True:
        candidate = next(candidates)
        divisors = multiples.pop(candidate, None)
        if divisors is None:
            yield candidate
            multiples[candidate ** 2] = [candidate]
        else:
            for divisor in divisors:
                multiples.setdefault(candidate + divisor, []).append(divisor)

def solution(n):
    string_of_primes = ''
    prime = primes()
    while len(string_of_primes) < (n+5):
        string_of_primes += str(next(prime))
    return string_of_primes[n:n+5]

print(solution(10000))
