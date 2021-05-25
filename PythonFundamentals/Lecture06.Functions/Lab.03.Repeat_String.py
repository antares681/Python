text = input()
repeat_times = int(input())


def text_repeater(entered_text, repeater_value):
    for times in range (repeater_value):
        print(entered_text, end = "")
    return

text_repeater(text, repeat_times)