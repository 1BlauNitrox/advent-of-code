# Read input.txt line by line
start = 50
amount_of_zeros = 0

with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        starting_letter = line[0]
        rotations = int(line.strip()[1:])
        if starting_letter == "L": #decrease number
            base = start if start > 0 else 100
            if rotations >= base:
                amount_of_zeros += 1 + (rotations - base) // 100
            start = (start - rotations) % 100

        elif starting_letter == "R": #increase number
            if (start + rotations) >= 100:
                amounts_passed_zero = (start + rotations) // 100
                amount_of_zeros += amounts_passed_zero
            start = (start + rotations) % 100
        

print(f"Final number: {start}")
print(f"Amount of times number was 0: {amount_of_zeros}")