n = int(input())

unique_elements = set()

for _ in range(n):
    elements = [unique_elements.add(x) for x in input().split()]

[print(element) for element in unique_elements]