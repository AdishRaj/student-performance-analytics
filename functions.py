def assign_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"


def check_result(row):
    if (
        row["Python"] >= 35
        and row["Maths"] >= 35
        and row["AI"] >= 35
    ):
        return "Pass"
    return "Fail"


def calculate_total(row):
    return row["Python"] + row["Maths"] + row["AI"]