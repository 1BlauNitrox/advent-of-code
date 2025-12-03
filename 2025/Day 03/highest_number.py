K = 12

total = 0

with open("input.txt", "r") as file:
    for line in file:
        number = line.strip()
        result_digits = []
        start = 0  

        for remaining in range(K, 0, -1):
            end = len(number) - remaining + 1

            best_digit = "0"
            best_pos = start

            for i in range(start, end):
                if number[i] > best_digit:
                    best_digit = number[i]
                    best_pos = i

            result_digits.append(best_digit)
            start = best_pos + 1 

        highest_number_str = "".join(result_digits)
        highest_number = int(highest_number_str)
        total += highest_number

print(f"Total of highest numbers: {total}")
