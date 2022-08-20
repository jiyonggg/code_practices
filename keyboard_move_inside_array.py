'''Move inside array with arrow keys'''
import keyboard
import sys

def in_range(nx, ny):
    return 0 <= nx and nx < 10 and 0 <= ny and ny < 10

x, y = 0, 0

arrow_keys = ["left", "right", "up", "down"]
dxs = {"left": 0, "right": 0, "up": -1, "down": 1}
dys = {"left": -1, "right": 1, "up": 0, "down": 0}

arr_2d = [['□'] * 10 for _ in range(10)] # 10 x 10
arr_2d[x][y] = '●'
arr_2d[9][9] = 'F'

for i in range(1, 9):
    arr_2d[i] = ['■', '■', '■', '■', '□', '□', '■', '■', '■', '■', '■']

while True:
    print()
    for i in range(10):
        for j in range(10):
            print(arr_2d[i][j], end=' ')
        print()
    sys.stdout.write("\033[A" * 11)
    
    event = keyboard.read_event()

    if event.event_type == keyboard.KEY_UP and event.name == "esc":
        print("\n" * 12 + "Goodbye.\n")
        break
    elif event.event_type == keyboard.KEY_UP and event.name in arrow_keys:
        nx, ny = x + dxs[event.name], y + dys[event.name]

        if in_range(nx, ny) and arr_2d[nx][ny] != '■':
            arr_2d[x][y] = '□'
            if arr_2d[nx][ny] == 'F':
                print("\n" * 12 + "Congratulations. You won!\n")
                break
            else:
                arr_2d[nx][ny] = '●'
                x, y = nx, ny
