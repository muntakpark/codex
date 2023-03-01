# random.random() -> 0(포함)과 1(포함하지 않음) 사이의 부동소수점 수를 난수로 발생시킴.
import random

# 가위-바위-보 시뮬레이션
user_com = int(input('정수 커맨드를 입력하세요\n 1)가위\n 2)바위\n 3)보\n입력: '))
com_val = random.random()
com_com = 1 if com_val<(1/3) else (2 if com_val<(2/3) else 3)

win_results = [(1, 3), (2, 1), (3, 2)]
if user_com == com_com:
    result = 'Draw'
else:
    result = 'Win' if (user_com, com_com) in win_results else 'Lose'

rsp = [0, '가위', '바위', '보']
print(f'User: {rsp[user_com]}, Com: {rsp[com_com]}')
print(f'Result is {result}')