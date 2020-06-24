from sense_hat import SenseHat

sense = SenseHat()

on = [255, 255, 255]
off = [0, 0, 0]

grid = [off for i in range(64)]
mid = int(len(grid)/2)
grid[(len - 5):(mid + 5)] = on
# print(grid)

sense.set_pixels(grid)
