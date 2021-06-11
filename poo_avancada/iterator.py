#!/usr/local/bin/python3
class RGB:
    def __init__(self):
        self.cores = ['red', 'green', 'blue'][::-1]

    def __next__(self):
        try:
            return self.cores.pop()
        except IndexError:
            raise StopIteration()

    def __iter__(self):
        return self  # self vai chamar o next


if __name__ == '__main__':
    cores = RGB()
    print(next(cores))
    print(next(cores))
    print(next(cores))
    try:
        print(next(cores))
    except StopIteration:
        print('cabou\n')

    for cor in RGB():
        print(cor)
