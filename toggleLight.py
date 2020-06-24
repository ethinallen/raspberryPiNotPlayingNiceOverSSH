from sense_hat import SenseHat

sense = SenseHat()

on = [255, 255, 255]
off = [0, 0, 0]

grid = sense.get_pixels()
mid = int(len(grid)/2)

if on in grid:
    for i in range(64):
        grid[i] = off
else:
    for i in range(mid-5,mid+5):
        grid[i] = on

sense.set_pixels(grid)
