nmbr_of_electrons = int(input())
electrons = []
shell_numbers = 1

while nmbr_of_electrons > 0:
    max_electron_current_shell = 2 * (shell_numbers**2)
    if max_electron_current_shell > nmbr_of_electrons:
        electrons.append(nmbr_of_electrons)
    else:
        electrons.append(max_electron_current_shell)
    nmbr_of_electrons -= max_electron_current_shell
    shell_numbers +=1

print(electrons)
