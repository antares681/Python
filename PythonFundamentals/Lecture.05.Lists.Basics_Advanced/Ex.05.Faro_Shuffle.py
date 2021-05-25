card_stack = input().split()
shuffle_number = int(input())
first_half = []
second_half = []

for shuffle in range(shuffle_number):
    for card in range(0, (len(card_stack) //2)):
        first_half.append(card_stack[card])
    for card in range(len(card_stack) - (len(card_stack)//2), len(card_stack)):
        second_half.append(card_stack[card])
    card_stack = []
    for i in range(len(second_half)):
        card_stack.append(first_half[0])
        first_half.pop(0)
        card_stack.append(second_half[0])
        second_half.pop(0)

print(card_stack)
