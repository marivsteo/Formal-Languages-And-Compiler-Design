from collections import deque


class HashTable:
    def __init__(self, size):
        self.__values = [deque() for _ in range(size)]
        self.__size = size

    def hash(self, value):
        ascii_sum = 0
        for character in value:
            ascii_sum += ord(character) - ord('0')
        return ascii_sum % self.__size

    def add(self, value):
        self.__values[self.hash(value)].append(value)

    def search(self, value):
        return value in self.__values[self.hash(value)]

    def get_position(self, value):
        """returns the position in the list and in the deque or adds the value to the hashtable if not present"""
        found_value = self.search(value)
        if found_value is False:
            self.add(value)
        position_list = self.hash(value)
        position_deque = 0
        for v in self.__values[position_list]:
            if v == value:
                return position_list, position_deque
            else:
                position_deque += 1

    def __str__(self):
        hash_table = ""
        for i in range(len(self.__values)):
            hash_table += str(i) + ": " + str(self.__values[i]) + "; \n"
        return hash_table
