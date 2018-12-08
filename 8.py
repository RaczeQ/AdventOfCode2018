from utils import read_input, save_result
from _8.logic import one, two

FILE_NAME = '_8/input.txt'
RESULT_ONE = '_8/one.txt'
RESULT_TWO = '_8/two.txt'

if __name__ == '__main__':
    result_one = one(read_input(FILE_NAME))
    save_result(RESULT_ONE, result_one)
    result_two = two(read_input(FILE_NAME))
    save_result(RESULT_TWO, result_two)