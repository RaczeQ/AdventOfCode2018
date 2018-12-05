from utils import read_input, save_result
from _5.logic import one, two

FILE_NAME = '_5/input.txt'
RESULT_ONE = '_5/one.txt'
RESULT_TWO = '_5/two.txt'

if __name__ == '__main__':
    result_one = one(read_input(FILE_NAME))
    save_result(RESULT_ONE, result_one)
    result_two = two(read_input(FILE_NAME))
    save_result(RESULT_TWO, result_two)