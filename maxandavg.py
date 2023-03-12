def calculate_max_and_average(*args):
    max_num = max(args)
    avg = sum(args) / len(args)
    return (max_num, avg)

input_str = input("Enter the numbers: ")
input_list = [float(x) for x in input_str.split() if float(x) >= 0]
if len(input_list) == 0:
    print("No numbers entered.")
else:
    max_num, avg = calculate_max_and_average(*input_list)
    print(f'{max_num:.2f} {avg:.2f}')