from questao_3.validator import valida_cdvpy


def test_correct_register():
    check = valida_cdvpy(123456)
    assert check

def test_duplicate_register():
    check = valida_cdvpy(552524)
    assert check == False

def test_duplicate_register2():
    check = valida_cdvpy(435643)
    assert check == False

def test_less_digits():
    check = valida_cdvpy(3421)
    assert check == False

def test_more_digits():
    check = valida_cdvpy(53871053)
    assert check == False

def test_zero_register():
    check = valida_cdvpy('034567')
    assert check == False

def test_letters_register():
    check = valida_cdvpy('123b56')
    assert check == False
