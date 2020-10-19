from HashTable import HashTable


class SymbolTable:
    def __init__(self, size):
        self.__hash_table = HashTable(size)

    def add(self, value):
        self.__hash_table.add(value)

    def search(self, value):
        return self.__hash_table.search(value)

    def get_position(self, value):
        return self.__hash_table.get_position(value)

    def __str__(self) -> str:
        return str(self.__hash_table)
