import curses
from  random import randrange,choice
from collections import defaultdict


actions = ['Up','Left','Down','Right','Restart','Exit']

letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']


actions_dict = dict(zip(letter_codes,actions*2))

def main(stdscr):
    def init():
        return 'Game'
    def not_game(state):
        #画出 GameOver 或者 Win 的界面
        #读取用户输入得到action，判断是重启游戏还是结束游戏
        responses = defaultdict(lambda :state) ＃默认是当前状态，没有行为就会一直在当前界面循环
        responses['Restart'],responses['Exit'] = 'Init','Exit'
        return responses[action]
    def game():
        if action == 'Restart':
            return 'Init'
        if actions =='Exit':
            return 'Exit'
        #chenggongyifong
            if :
                return 'Win'
            if ：
                return 'gameover'
        return 'game'





