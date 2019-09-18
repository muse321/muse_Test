'''
    逻辑业务
'''
import random
from game2048.model import *

class GameCoreController:
    def __init__(self):
        self.__map = [
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]
        ]

    @property
    def map(self):
        return self.__map

    def __select_number(self):
        return 4 if random.randint(0,10) == 1 else 2

    def generate_numer(self):
        cho = random.choice(self.__find_blank())
        self.__map[cho.r_index][cho.c_index] = self.__select_number()

    def __find_blank(self):
        list_blank = []
        for r in range(len(self.__map)):
            for c in range(len(self.__map[r])):
                if self.__map[r][c] == 0:
                    list_blank.append(Location(r,c))
        return list_blank

    def __square_matrix_transpose(self):
        '''
            将方阵转置
        '''
        for r in range(1,len(self.__map)):
            for c in range(r):
                self.__map[r][c],self.__map[c][r] = self.__map[c][r],self.__map[r][c]

    def __zero_to_end(self, list_target):
        '''
            将零元素移至后面
        '''
        for item in range(-1, -len(list_target)-1, -1):
            if list_target[item] == 0:
                del list_target[item]
                list_target.append(0)

    def __merge(self, list_target):
        '''
            将相邻的相同元素相加（忽略中间的零元素）
        '''
        self.__zero_to_end(list_target)
        for item in range(len(list_target)-1):
            if list_target[item] == list_target[item+1]:
                list_target[item] = list_target[item] * 2
                del list_target[item + 1]
                list_target.append(0)

    def move_lift(self):
        '''
            左移
        '''
        for item in self.__map:
            self.__merge(item)
        self.generate_numer()

    def move_right(self):
        '''
            右移
        '''
        for item in range(len(self.__map)):
            list02 = self.__map[item][::-1]
            self.__merge(list02)
            self.__map[item] = list02[::-1]
        self.generate_numer()

    def move_up(self):
        '''
            上移
        '''
        self.__square_matrix_transpose()
        self.move_lift()
        self.__square_matrix_transpose()

    def move_down(self):
        '''
            下移
        '''
        self.__square_matrix_transpose()
        self.move_right()
        self.__square_matrix_transpose()

    def is_game_over(self):
        '''
            游戏是否结束
        :return: False表示没有结束　True表示游戏结束
        '''
        if len(self.__find_blank()) != 0:
            return False
        for r in range(len(self.__map)):
            for c in range(len(self.__map[r])-1):
                if self.__map[r][c] == self.__map[r][c+1] or self.__map[c][r] == self.__map[c+1][r]:
                    return False
        return True

if __name__ == '__main__':
    controller = GameCoreController()
    controller.move_down()
    print(controller.map)
