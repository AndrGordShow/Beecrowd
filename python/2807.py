x = int(input())
aux = []
a = [
    267914296,
    165580141,
    102334155,
    63245986,
    39088169,
    24157817,
    14930352,
    9227465,
    5702887,
    3524578,
    2178309,
    1346269,
    832040,
    514229,
    317811,
    196418,
    121393,
    75025,
    46368,
    28657,
    17711,
    10946,
    6765,
    4181,
    2584,
    1597,
    987,
    610,
    377,
    233,
    144,
    89,
    55,
    34,
    21,
    13,
    8,
    5,
    3,
    2,
    1,
    1,
]
for i in range(1, x + 1):
    aux.append(a[-i])
aux.reverse()
for i in range(x - 1):
    print(aux[i], end=" ")
print(aux[x - 1])
