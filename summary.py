import math
from calcs import Calculate
PERCENTILE = 60

def compute_summary(num_list):
    calculate_1 = Calculate(num_list, 25)
    calculate_2 = Calculate(num_list, 50)
    calculate_3 = Calculate(num_list, 75)

    nums_list = calculate_1.list_nums
    # three quartiles
    q_1 = calculate_1.calculate_q()
    q_2 = calculate_2.calculate_q()
    q_3 = calculate_3.calculate_q()

    # iqr (inter quartillian range)
    iqr = q_3 - q_1
    print(f"iqr:{iqr}")


    # fences

    fences = [round(q_1 - 1.5 * iqr, 2), round(q_3 + 1.5 * iqr, 2)]

    # find s and l
    list_values =[]
    for i in range(len(nums_list)):
        if nums_list[i] <= fences[0] or nums_list[i] >= fences[1]:
            list_values.append(nums_list[i])


    for values in list_values:
        if values in nums_list:
            nums_list.remove(values)

    s = nums_list[0]
    l = nums_list[-1]

    summary = f"\n    S: {s}\n    q1: {q_1}\n    q2: {round(q_2, 3)}\n    q3: {q_3}\n    l: {l}"

    return f"fences:{fences}\nSummary:{summary}"


def compute_percentile(num_list):
    calculate_1 = Calculate(num_list, PERCENTILE)

    nums_list = calculate_1.list_nums
    # three quartiles
    q_1 = calculate_1.calculate_q()

    summary = f"{PERCENTILE} percentile: {q_1}"
    return summary
