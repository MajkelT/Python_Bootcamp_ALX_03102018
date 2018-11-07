def przytnij (data, start, stop):
    result = []
    dodawac_do_listy = False
    for element in data:
        if start(element):
            dodawac_do_listy = True
        if dodawac_do_listy:
            result.append(element)    #po dodaniu elementu sprawdzam, czy ten element jest końcowym
            if stop(element):
                break
    return result

def test_przytnij():
    assert przytnij(
        data = [1, 2, 3, 4, 5, 6, 7],
        start = lambda x: x > 3,
        stop = lambda x: x == 6
    ) == [4, 5, 6]