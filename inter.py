import sys
import time

fc = open(sys.argv[1]).read().replace('\n','')

exec(f't = {fc}')

for dict in t:
    if dict.get('method') == 'say':
        for s in dict.get('text'):
            print(s)
    if dict.get('method') == 'create_files':
        for s in dict.get('files'):
            open(s, 'w')
    if dict.get('method') == 'write_file':
        info = dict.get('data')
        open(info[0], 'w').write(info[1])
    if dict.get('method') == 'wait_seconds':
        time.sleep(int(dict.get('len')))
    if dict.get('method') == 'move_mouse':
        pyautogui.moveTo(dict.get('pos')[0], dict.get('pos')[1])
    if dict.get('method') == 'comment':
        exec(f'#{dict.get("data")}')
    
        
