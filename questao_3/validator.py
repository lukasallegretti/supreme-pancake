""" Validate CDvPy register """
from collections import Counter


def valida_cdvpy(cdvpy: int) -> bool:
    """ Validate cdvpy register

    Args:
        cdvpy (int): Registration number

    Returns:
        bool: Is a validate register or not
    """
    register = str(cdvpy)
    check = [
        rule_1(register),
        rule_2(register),
        rule_3(register)
    ]

    validate = False
    if all(check) == True:
        validate = True

    return validate


def rule_1(cdvpy: str) -> bool:
    """ Check if cdvpy ahs six numbers
    Args:
        cdvpy (str): Registration number

    Returns:
        bool: Respected or not the rule
    """
    register = str(cdvpy)
    rule = True

    if len(register) != 6:
        rule = False
    
    try:
        for i in range(len(register)):
            int(register[i])
    except ValueError:
        rule = False
    
    return rule


def rule_2(cdvpy: str) -> bool:
    """ Check if first number is zero

    Args:
        cdvpy (str): Registration number

    Returns:
        bool: Respected or not the rule
    """
    register = str(cdvpy)
    try:
        if int(register[0]) == 0:
            rule = False
        else:
            rule = True
    except ValueError:
        rule = False

    return rule


def rule_3(cdvpy: str) -> bool:
    """ Check for duplicate pairs

    Args:
        cdvpy (str): Registration number

    Returns:
        bool: Respected or not the rule
    """
    register = str(cdvpy)
    pairs = []
    rule = True

    for i in range(len(register) - 1):
        pairs.append(
            register[i] + register[i + 1]
        )

    count = Counter(pairs)
    for value in count.values():
        if value > 1:
            rule = False

    return rule


if __name__ == '__main__':
    cdvpy = input('Digite um CDvPy:')
    print(valida_cdvpy(cdvpy))
