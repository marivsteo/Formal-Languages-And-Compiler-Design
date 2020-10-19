from SymbolTable import SymbolTable


def test():
    size = 15
    st = SymbolTable(size)
    identifiers = ['a', 'b', 'c', 'd']
    constants = ['15', '2', '7']
    identifiers_constants = identifiers + constants
    for value in identifiers_constants:
        st.add(value)
    st.get_position('z')
    pos, deque = st.get_position('a')
    assert pos != (-1)
    print(st)


if __name__ == "__main__":
    test()
