def completness__bar_modifier(percentage):
    x = []
    completness_range = int(percentage / len(completeness_bar))
    del completeness_bar[0:completness_range]
    for i in range (completness_range):
        completeness_bar.insert(i, "%")
    x = ''.join(completeness_bar)
    return x

def if_complete_checker(percentage):

    if percentage == 100:
        print("100% Complete!")
        print(f"[{completness__bar_modifier(number)}]")
    elif 0 < percentage < 100:
        print(f"{number}% [{completness__bar_modifier(number)}]")
        print("Still loading...")

number = int(input())
completeness_bar = ["."] * 10
if_complete_checker(number)