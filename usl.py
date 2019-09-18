from game2048.bll import *
import os

class GameConsoleView:
    def __init__(self):
        self.__controller = GameCoreController()

    def __start(self):
        self.__controller.generate_numer()
        self.__controller.generate_numer()
        self.__draw_map()

    def __draw_map(self):
        os.system('clear')
        for line in self.__controller.map:
            for item in line:
                print(item,end=' ')
            print()

    def __operation(self):
        while True:
            self.__move_map()
            self.__draw_map()
            if self.__controller.is_game_over():
                print('游戏结束，菜鸡')
                break

    def __move_map(self):
        direction = input('请输入方向(wasd):')
        if direction == 'w':
            self.__controller.move_up()
        elif direction == 's':
            self.__controller.move_down()
        elif direction == 'a':
            self.__controller.move_lift()
        elif direction == 'd':
            self.__controller.move_right()
        else:
            print('输入错误')

    def main(self):
        self.__start()
        self.__operation()
