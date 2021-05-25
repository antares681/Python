# n, m = input().split(' ')
# n_length, m_length = int(n), int(m)
# n, m = set(), set()
#
# for _ in range(n_length):
#     n.add(int(input()))
# for _ in range(m_length):
#     m.add(int(input()))
#
# result = n & m
# for el in result:
#     print(el)
#
data = input()
n_length, m_length = int(data.split(' ')[0]), int(data.split(' ')[1])
n, m = set(), set()
for _ in range(n_length):
    n.add(int(input()))
for _ in range(m_length):
    m.add(int(input()))
[print(el) for el in n & m]
