from sense_hat import SenseHat

sense = SenseHat()

on = [255, 255, 255]
off = [0, 0, 0]

grid = sense.get_pixels()
mid = int(len(grid)/2)

for i in range(64):
    grid[i] = off

sense.set_pixels(grid)
