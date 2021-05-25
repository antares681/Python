# cards = input()
# players_count_A = 11
# players_count_B = 11
# is_Terminated = False
# team_A_out = []
# team_B_out = []
# cards_list = cards.split()
#
# for event in cards_list:
#     if event in team_A_out or event in team_B_out:
#         continue
#     else:
#         if "A" in event:
#             players_count_A -= 1
#             team_A_out.append(event)
#         elif "B" in event:
#             players_count_B -= 1
#             team_B_out.append(event)
#         if players_count_A < 7 or players_count_B < 7:
#             is_Terminated = True
#             break
#
# print(f"Team A - {players_count_A}; Team B - {players_count_B}")
#
# if is_Terminated:
#     print("Game was terminated")

team_a = [f"A-{i}" for i in range(1, 12)]
team_b = [f"B-{i}" for i in range(1, 12)]

players_kicked = input().split()

for i in players_kicked:

    if i in team_a:
        team_a.remove(i)

    if i in team_b:
        team_b.remove(i)

    if len(team_b) < 7 or len(team_a) < 7:
        isTerminated = True
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")

if isTerminated:
    print("Game was terminated")
