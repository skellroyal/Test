#   載入套件
import pyautogui, time

#   關掉安全模式，避免程式在滑鼠滑到左上角時中斷。
pyautogui.FAILSAFE = False

#   按 Windows 鍵：按開始
pyautogui.press('win')

#   輸入 mspaint 後按 Enter 鍵，執行小畫家
pyautogui.typewrite('mspaint')
pyautogui.press('enter')

#   滑鼠跑到左上角，並浪費兩秒鐘。
#   重點是要浪費兩秒鐘等小畫家打開，不然接不上下一個動作。
pyautogui.moveTo(0,0,2)

#   同時按下 Windows 鍵與 上箭頭 鍵，用熱鍵將小畫家最大化。
pyautogui.hotkey('win','up')

#   多按幾下確保有最大化
pyautogui.hotkey('win','up')
pyautogui.hotkey('win','up')
pyautogui.hotkey('win','up')

def drawRokuMon(x, y):
    # 選畫圈圈
    # 找到畫圈圈的工具
    loc = pyautogui.locateOnScreen('oval.png')
    while loc == None:
        print('oval','not found')
        time.sleep(0.1)
        loc = pyautogui.locateOnScreen('oval.png')
    
    # 點擊
    center = pyautogui.center(loc)
    pyautogui.click(center)
    
    # 畫圈圈
    # 移到左上
    pyautogui.moveTo(x, y)
    # 拖曳到右下
    pyautogui.dragRel(200, 200)
    
    # 選畫正方形
    # 找到畫矩形的工具
    loc = pyautogui.locateOnScreen('rec.png')
    while loc == None:
        print('rec','not found')
        time.sleep(0.1)
        loc = pyautogui.locateOnScreen('rec.png')
    
    # 點擊
    center = pyautogui.center(loc)
    pyautogui.click(center)
    
    # 畫正方形
    # 移到左上
    pyautogui.moveTo(x+60, y+60)
    # 拖曳到右下
    pyautogui.dragRel(80, 80)
    
    # 選填色
    # 找到填滿工具
    loc = pyautogui.locateOnScreen('paint.png')
    while loc == None:
        print('paint','not found')
        time.sleep(0.1)
        loc = pyautogui.locateOnScreen('paint.png')
    
    # 點擊
    center = pyautogui.center(loc)
    pyautogui.click(center)
    
    # 移到要填的地方
    pyautogui.moveTo(x+23, y+97)
    # 點擊
    pyautogui.click()

for i in [(200, 200), (400, 200), (600, 200), (200, 400), (400, 400), (600, 400)]:
    print('{}, {}'.format(i[0],i[1]))
    drawRokuMon(i[0], i[1])
    

