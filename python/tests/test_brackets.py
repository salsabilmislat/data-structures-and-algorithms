from code_challenges.stack_queue_brackets.stack_queue_brackets import validate_brackets


def test_Square_Brackets():
    actual = True
    exceptValue= validate_brackets('()')
    assert actual ==exceptValue

def test_Compine_Brackets():
    actual = True
    exceptValue= validate_brackets('{}(){}')
    assert actual ==exceptValue

def test_Compine_BracketsandWord():
    actual = True
    exceptValue= validate_brackets('()[[Extra Characters]]')
    assert actual ==exceptValue

def test_Compine_BracketsandWord2():
    actual = True
    exceptValue= validate_brackets('{}{Code}[Fellows](())')
    assert actual ==exceptValue

def test_Compine_Brackets2():
    actual = True
    exceptValue= validate_brackets('(){}[[]]')
    assert actual ==exceptValue

def test_Compine_Brackets3():
    actual = False
    exceptValue= validate_brackets('[({}]')
    assert actual ==exceptValue

def test_Compine_Brackets4():
    actual = False
    exceptValue= validate_brackets('(](')
    assert actual ==exceptValue

def test_Compine_Brackets5():
    actual = False
    exceptValue= validate_brackets('{(})')
    assert actual ==exceptValue
