def read_ppm_as_rows(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    clean_lines = [line.strip() for line in lines
                   if not line.strip().startswith('#') and line.strip()]
    
    magic = clean_lines[0]
    width, height = map(int, clean_lines[1].split())
    max_val = int(clean_lines[2])
    
    # Collect all pixel values
    pixels = []
    for line in clean_lines[3:]:
        pixels.extend(map(int, line.split()))
    
    # Group into rows: [[(r,g,b), (r,g,b), ...], [(r,g,b), (r,g,b), ...], ...]
    image = []
    pixel_index = 0
    for y in range(height):
        row = []
        for x in range(width):
            r = pixels[pixel_index]
            g = pixels[pixel_index + 1]
            b = pixels[pixel_index + 2]
            row.append((r, g, b))
            pixel_index += 3
        image.append(row)
    
    return width, height, max_val, image

def write_ppm(filename, matrix, max_val=255):
    """
    Write PPM file - handles both RGB tuples and separate RGB values
    """
    height = len(matrix)
    width = len(matrix[0]) if matrix else 0
    
    with open(filename, 'w') as f:
        f.write("P3\n")
        f.write(f"{width} {height}\n")
        f.write(f"{max_val}\n")
        
        for row in matrix:
            for pixel in row:
            
                r, g, b = pixel
                
                
                f.write(f"{r} {g} {b}  ")
            f.write("\n")
            
def read_pgm_as_rows(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    clean_lines = [line.strip() for line in lines
                   if not line.strip().startswith('#') and line.strip()]
    
    magic = clean_lines[0]
    if magic != 'P2':
        raise ValueError("Not a P2 PGM file")
    width, height = map(int, clean_lines[1].split())
    max_val = int(clean_lines[2])
    
    # Collect all pixel values
    pixels = []
    for line in clean_lines[3:]:
        pixels.extend(map(int, line.split()))
    
    # Group into rows: [[val, val, ...], [val, val, ...], ...]
    image = []
    pixel_index = 0
    for y in range(height):
        row = []
        for x in range(width):
            row.append(pixels[pixel_index])
            pixel_index += 1
        image.append(row)
    
    return width, height, max_val, image

def write_pgm(filename, matrix, max_val=255):
    """
    Write P2 PGM file - grayscale
    """
    height = len(matrix)
    width = len(matrix[0]) if matrix else 0
    
    with open(filename, 'w') as f:
        f.write("P2\n")
        f.write(f"{width} {height}\n")
        f.write(f"{max_val}\n")
        
        for row in matrix:
            for val in row:
                f.write(f"{val} ")
            f.write("\n")

def read_pbm_as_rows(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    clean_lines = [line.strip() for line in lines
            if not line.strip().startswith('#') and line.strip()]

    magic = clean_lines[0]
    if magic != 'P1':
        raise ValueError("Not a P1 PBM file")
    width, height = map(int, clean_lines[1].split())

    # Collect all pixel values
    pixels = []
    for line in clean_lines[2:]:
        pixels.extend(map(int, line.split()))

    # Group into rows: [[val, val, ...], [val, val, ...], ...]
    image = []
    pixel_index = 0
    for y in range(height):
        row = []
        for x in range(width):
            row.append(pixels[pixel_index])
            pixel_index += 1
        image.append(row)

    return width, height, image
def write_pbm(filename, matrix, max_val=1):
    """ Write P1 PBM file - black and white
    """     
    height = len(matrix)
    width = len(matrix[0]) if matrix else 0
    
    with open(filename, 'w') as f:
        f.write("P1\n")
        f.write(f"{width} {height}\n")
        
        for row in matrix:
            for val in row:
                f.write(f"{val} ")
            f.write("\n")                                                       