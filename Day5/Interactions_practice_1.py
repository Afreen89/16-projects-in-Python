from random import choice

def throw_dice():
    dice_one = int(choice(range(1, 6)))
    dice_two = int(choice(range(1, 6)))
    return dice_one, dice_two


def roll_result(n, m):
    sum_dice = n + m
    if sum_dice <= 6:
        return (f"The sum of your dice is {sum_dice}. Unfortunate")
    if sum_dice > 6 and sum_dice < 10:
        return (f"The sum of your dice is {sum_dice}. You have a good chance")
    if sum_dice >= 10:
        return (f"The sum of your dice is {sum_dice}. It looks like a winning roll")

one, two = throw_dice()
print(roll_result(one, two))
