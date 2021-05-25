names_nmbr = int(input())
unique_names = set()
for _ in range(names_nmbr):
    unique_names.add(input())
print("\n".join(unique_names))