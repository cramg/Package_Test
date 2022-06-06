import packagetest as p

def test_one():
    ave_1 = p.Ave()
    assert ave_1.especies == ['aguila', 'gallina', 'pato']

def test_two():
    ave_2 = p.Ave()
    assert ave_2.especies[2] == 'pato'
