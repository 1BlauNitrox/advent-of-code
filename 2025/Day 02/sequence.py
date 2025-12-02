added_sequence_number = 0

def is_invalid_id(num: int) -> bool:
    s = str(num)
    n = len(s)
    if n < 2:
        return False

    for block_len in range(1, n // 2 + 1):
        if n % block_len != 0:
            continue # Block length must divide the string length evenly

        repeat_count = n // block_len
        if repeat_count < 2:
            continue # At least two repetitions required

        block = s[:block_len]
        if block * repeat_count == s:
            return True # Found a repeating sequence

    return False

with open('input.txt', 'r') as file:
    sequences = file.read().strip().split(",")

    for seq in sequences:
        start_str, end_str = map(int, seq.split("-"))

        for number in range(start_str, end_str + 1):
            if is_invalid_id(number):
                added_sequence_number += number

print(f"Sum of all added sequence numbers: {added_sequence_number}")