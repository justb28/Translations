
import math
from ppm import read_ppm_as_rows, write_ppm 
def rotate(matrix, angle=90):
    width= len(matrix[0])
    height = len(matrix)

    theta = math.radians(angle)

    # Default center coordinates
    x0 = (height - 1) / 2
    y0 = (width - 1) / 2

    coords_and_values = []

    # Step 1: Rotate every pixel (0s and 1s)
    for x in range(height):
        for y in range(width):
            val = matrix[x][y]
            x_rot = x0 + (x - x0) * math.cos(-theta) + (y - y0) * math.sin(-theta)
            y_rot = y0 - (x - x0) * math.sin(-theta) + (y - y0) * math.cos(-theta)
            x_rot = round(x_rot)
            y_rot = round(y_rot)
            coords_and_values.append((x_rot, y_rot, val))

    # blank matrix and shift all coordinates
    rotated = [[0 for _ in range(width)] for _ in range(height)]
    for x, y, val in coords_and_values:
        #new_x = x - min_x
        #new_y = y - min_y
        rotated[x][y] = val

    
    return rotated


def grayscale_ave(width, height,matrix):
    #height = len(matrix)
    #width = len(matrix[0])

    grayscale_matrix = [[0 for _ in range(width)] for _ in range(height)]

    for x in range(height):
        for y in range(width):
            r, g, b = matrix[x][y]
            gray = (r + g + b) // 3
            grayscale_matrix[x][y] = (gray, gray, gray)

    return grayscale_matrix

def grayscale_luma(matrix):
    height = len(matrix)
    width = len(matrix[0])

    grayscale_matrix = [[0 for _ in range(width)] for _ in range(height)]

    for x in range(height):
        for y in range(width):
            r, g, b = matrix[x][y]
            gray = int(0.3*r + 0.59*g + 0.11*b)
            grayscale_matrix[x][y] = (gray, gray, gray)

    return grayscale_matrix
def greyscale_single_channel(width, height,matrix):
    #height = len(matrix)
    #width = len(matrix[0])

    grayscale_matrix = [[0 for _ in range(width)] for _ in range(height)]

    for x in range(height):
        for y in range(width):
            r, g, b = matrix[x][y]
            gray = g  # Assuming we want to use the red channel for grayscale
            # Alternatively, you can use g or b if you prefer
            grayscale_matrix[x][y] = (gray, gray, gray)

    return grayscale_matrix

def Nearest_neighbour_scale(matrix, factor):
    height = len(matrix)
    width = len(matrix[0])

    scaled_height = int(height * factor)
    scaled_width = int(width * factor)

    scaled_matrix = [[0 for _ in range(scaled_width)] for _ in range(scaled_height)]

    for x in range(scaled_height):
        for y in range(scaled_width):
            orig_x = int(x / factor)
            orig_y = int(y / factor)
            
            scaled_matrix[x][y] = matrix[orig_x][orig_y]

    return scaled_matrix

def interpolate_scale(matrix, factor):
    height = len(matrix)
    width = len(matrix[0])
    scaled_height = int(height * factor)
    scaled_width = int(width * factor)
    
    # Initialize scaled matrix
    scaled_matrix = [[0 for _ in range(scaled_width)] for _ in range(scaled_height)]
    
    for i in range(scaled_height):
        for j in range(scaled_width):
            # Map scaled coordinates back to original coordinates
            x = i / factor
            y = j / factor
            
            # Get the four surrounding pixels in original matrix
            x1 = int(x)
            y1 = int(y)
            x2 = min(x1 + 1, height - 1)
            y2 = min(y1 + 1, width - 1)
            
            # Calculate interpolation weights
            dx = x - x1
            dy = y - y1
            
            # Get pixel values (handle edge cases)
            p11 = matrix[x1][y1]  # top-left
            p12 = matrix[x1][y2]  # top-right
            p21 = matrix[x2][y1]  # bottom-left
            p22 = matrix[x2][y2]  # bottom-right
            
            # Bilinear interpolation for each color channel
            interpolated_pixel = []
            for channel in range(3):  # r, g, b
                # Interpolate top row
                top = p11[channel] * (1 - dy) + p12[channel] * dy
                # Interpolate bottom row
                bottom = p21[channel] * (1 - dy) + p22[channel] * dy
                # Final interpolation
                value = top * (1 - dx) + bottom * dx
                interpolated_pixel.append(int(round(value)))
            
            scaled_matrix[i][j] = tuple(interpolated_pixel)
    
    return scaled_matrix
width, height, max_val, image =read_ppm_as_rows("C:/Users/bonga/OneDrive/Documents/imageprocessing/color.ppm")
#print(width, height, max_val, image)

write_ppm("C:/Users/bonga/OneDrive/Documents/imageprocessing/colorgrey.ppm",grayscale_ave(width, height, image),max_val)
write_ppm("C:/Users/bonga/OneDrive/Documents/imageprocessing/colorgreyluma.ppm",grayscale_luma(image),max_val)
write_ppm("C:/Users/bonga/OneDrive/Documents/imageprocessing/colorgreysingle.ppm",greyscale_single_channel(width, height, image),max_val)
write_ppm("C:/Users/bonga/OneDrive/Documents/imageprocessing/colorscaled.ppm",Nearest_neighbour_scale(image,5),max_val)
write_ppm("C:/Users/bonga/OneDrive/Documents/imageprocessing/colorscaledinterpolate.ppm",interpolate_scale(image,2),max_val)
write_ppm("C:/Users/bonga/OneDrive/Documents/imageprocessing/colorrotated.ppm",rotate(image, 22.5),max_val)