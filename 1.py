from utils import read_input, save_result
from _1.logic import one, two

FILE_NAME = '_1/input.txt'
RESULT_ONE = '_1/one.txt'
RESULT_TWO = '_1/two.txt'

if __name__ == '__main__':
    result_one = one(read_input(FILE_NAME))
    save_result(RESULT_ONE, result_one)
    result_two = two(read_input(FILE_NAME))
    save_result(RESULT_TWO, result_two)