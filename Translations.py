
import math
def read_pbm(filename):
    with open(filename, 'r') as f:
        # Helper to skip comment and blank lines
        def next_non_comment():
            line = f.readline()
            while line.startswith('#') or line.strip() == '':
                line = f.readline()
            return line.strip()

        # Check for correct magic number
        magic_number = next_non_comment()
        if magic_number != 'P1':
            raise ValueError("Unsupported format: Expected P1 PBM file")

        # Get image dimensions
        width, height = map(int, next_non_comment().split())

        # Read pixel data
        pixels = []
        for line in f:
            if line.startswith('#') or line.strip() == '':
                continue
            pixels.extend(map(int, line.strip().split()))

        if len(pixels) != width * height:
            raise ValueError("Pixel data does not match width and height")

        # Build 2D matrix
        matrix = []
        index = 0
        for _ in range(height):
            row = []
            for _ in range(width):
                row.append(pixels[index])
                index += 1
            matrix.append(row)

        return matrix
    
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
            x_rot = x0 + (x - x0) * math.cos(theta) + (y - y0) * math.sin(theta)
            y_rot = y0 - (x - x0) * math.sin(theta) + (y - y0) * math.cos(theta)
            x_rot = round(x_rot)
            y_rot = round(y_rot)
            coords_and_values.append((x_rot, y_rot, val))

    # bounding box
    min_x = min(x for x, y, v in coords_and_values)
    max_x = max(x for x, y, v in coords_and_values)
    min_y = min(y for x, y, v in coords_and_values)
    max_y = max(y for x, y, v in coords_and_values)

    new_height = max_x - min_x + 1
    new_width = max_y - min_y + 1

    # blank matrix and shift all coordinates
    rotated = [[0 for _ in range(new_width)] for _ in range(new_height)]

    for x, y, val in coords_and_values:
        #new_x = x - min_x
        #new_y = y - min_y
        rotated[x][y] = val

    
    return rotated


def grayscale_ave(matrix):
    height = len(matrix)
    width = len(matrix[0])

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
            gray = 0,3*r + 0.59*g + 0,11*b
            grayscale_matrix[x][y] = (gray, gray, gray)

    return grayscale_matrix


def scale(matrix, factor):
    height = len(matrix)
    width = len(matrix[0])

    scaled_height = int(height * factor)
    scaled_width = int(width * factor)

    scaled_matrix = [[0 for _ in range(scaled_width)] for _ in range(scaled_height)]

    for x in range(scaled_height):
        for y in range(scaled_width):
            orig_x = int(x / factor)
            orig_y = int(y / factor)
            if orig_x < height and orig_y < width:
                scaled_matrix[x][y] = matrix[orig_x][orig_y]

    return scaled_matrix
    
def write_pbm_2d(filename, matrix, comment=None):
    height = len(matrix)
    width = len(matrix[0]) if height > 0 else 0

    with open(filename, 'w') as f:
        f.write("P1\n")
        if comment:
            f.write(f"# {comment}\n")
        f.write(f"{width} {height}\n")
        for row in matrix:
            f.write(' '.join(map(str, row)) + '\n')


print(read_pbm('C:/Users/bonga/Downloads/j.pbm'))  # Replace 'example.ppm' with your PPM file path
print('\n')
print(rotate(read_pbm('C:/Users/bonga/Downloads/j.pbm'), angle=90))

write_pbm_2d('C:/Users/bonga/Downloads/j_rotated.pbm', rotate(read_pbm('C:/Users/bonga/Downloads/j.pbm'), angle=30), comment='Rotated by 30 degrees')
