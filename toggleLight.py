from sense_hat import SenseHat

sense = SenseHat()

on = [255, 255, 255]
off = [0, 0, 0]

grid = [off for i in range(64)]
grid[int(len(grid)/2)] = on
# print(grid)

sense.set_pixels(grid)
