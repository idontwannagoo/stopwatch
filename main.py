import time
import keyboard
import pygame
import pyperclip

# pygame.mixer.init()



filename = time.strftime('%Y{y}%m{m}%d{d} %H{h}%M{f}%S{s}').format(y='年', m='月', d='日', h='时', f='分', s='秒') + ' ' + input("输入数据文件名：")
with open('%s.txt' % filename, 'w') as f_obj:
    f_obj.write('')
rest_homework = input('还剩下的份数（包括当前未完成）: ')

if rest_homework == '':
    rest_homework = 1
else:
    rest_homework = int(rest_homework)
rest_still_homework = rest_homework
start_num = input('初始题号：')
if start_num == '':
    start_num = 1
else:
    start_num = int(start_num)
int_rest_homework = rest_homework
anjian = input('请输入按键，默认为F12：')
if anjian == '':
    anjian = 'F12'
print('按下{}开始计时，按下{}计次'.format(anjian, anjian))
keyboard.wait(anjian)
ta = time.time()
start_time = time.time()
total_start_time = time.time()
print('开始')
times = 1
# pygame.mixer.music.load('E:\\Noame\\飞机上广播的提示音_耳聆网_[声音ID：12956].wav')
# pygame.mixer.music.play()

while True:
    # if rest_homework == 0:
    #     with open('%s.txt' % filename, 'a') as f_obj:
    #         f_obj.write('Mission Completed.' + "\n")
    #     print('Mission Completed.')
    #     break
    if keyboard.is_pressed('F10'):
        print('Mission Completed.')
        break

    t = time.time() - ta
    d_sec = time.time() - start_time  # 计算△t 开始总时间
    t_sec = time.time() - total_start_time
    dm, ds = divmod(d_sec, 60)  # 格式化
    dh, dm = divmod(dm, 60)
    tm, ts = divmod(t_sec, 60)
    th, tm = divmod(tm, 60)

    # 计算平均速度
    r_sec = t_sec * ((rest_still_homework - times)/times)
    rest_m, rest_s = divmod(r_sec, 60)  # 格式化
    rest_h, rest_m = divmod(rest_m, 60)

    if round(d_sec, 3) == 180.000:
        pygame.mixer.music.load('E:\\Noame\\14543.wav')
        pygame.mixer.music.play()
    # if dm == 0:
    #     message = '%s  |  %d 分 %.03f 秒  |  %.03f 秒  |  剩余时间：%d 分 %.03f 秒  |  剩余份数：%d 份' % (str(times), tm, ts, ds, rest_m, rest_s, rest_homework)
    # else:
    #     message = '%s  |  %d 分 %.03f 秒 |  %d 分 %.03f 秒  |  剩余时间：%d 分 %.03f 秒  |  剩余份数：%d 份' % (str(times), tm, ts, dm, ds, rest_m, rest_s, rest_homework)
    time_now = time.strftime('%H:%M:%S').format(y='年', m='月', d='日')
    message = '%s  |  %s  |  %d 时 %d 分 %.03f 秒 |  %d 时 %d 分 %.03f 秒  |  剩余：%d 时 %d 分 %.03f 秒  |  剩余份数：%d 份' % (start_num + times - 1, time_now, th, tm, ts, dh, dm, ds, rest_h, rest_m, rest_s, rest_homework)
    # print('\r' + message, end="")  # 输出
    print(message, end="\r")  # 输出
    time.sleep(0.001)
    if keyboard.is_pressed('F9'):
        keyboard.wait('F8')
        start_time = time.time()
        total_start_time = time.time()
    if keyboard.is_pressed(anjian):  # F12监听
        ta = time.time()  # 初始化开始时间

        if t > 0.01:  # 防止一直按住空格的误会
            # pygame.mixer.music.load('E:\\Noame\\飞机上广播的提示音_耳聆网_[声音ID：12956].wav')
            # pygame.mixer.music.play()
            with open('%s.txt' % filename, 'a') as f_obj:
                f_obj.write(message + "\n")
            start_time = time.time()
            print('')  # 换行输入
            times = times + 1
            rest_homework = rest_homework - 1
