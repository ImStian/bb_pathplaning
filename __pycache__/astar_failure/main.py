import aStar as aStar
from image_conversion import generate_pixelmap
from matplotlib import image 
from matplotlib import pyplot as plt 
  

pixelmap = generate_pixelmap("grid_smile.png")


maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]



start = (0, 0)
end = (40,40)

path = aStar.astar(pixelmap, start, end)
print(path)


# to read the image stored in the working directory 
data = image.imread('grid_smile.png') 
  

for waypoint in path:
    plt.plot(waypoint[0], waypoint[1], marker='v', color="red") 
plt.imshow(data) 
plt.show()

print('Hello world')