'''You can move with arrow keys'''
import keyboard

x, y = 0, 0

arrow_keys = ["left", "right", "up", "down"]
dxs = {"left": -1, "right": 1, "up": 0, "down": 0}
dys = {"left": 0, "right": 0, "up": 1, "down": -1}

print(f"x: {x} | y: {y}", end='\r')

while True:
    # Wait for the next event.
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_UP and event.name == "esc":
        print("Goodbye.                 ")
        break
    if event.event_type == keyboard.KEY_UP and event.name in arrow_keys:
        nx = x + dxs[event.name]
        ny = y + dys[event.name]

        if (nx, ny) == (5, 5):
            print("Collision            ", end='\r')
        else:
            x, y = nx, ny
            print(f"x: {x} | y: {y}    ", end='\r')

        if (nx, ny) == (10, 10):
            print("Goal! Congratulations.   ")
            break