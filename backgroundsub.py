
from ppm import read_pgm_as_rows, write_pgm

# Example frame: 3x3 grayscale image
frame1 = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

frame2 = [
    [12, 19, 35],
    [45, 49, 55],
    [75, 82, 88]
]

def background_subtraction(frame, background, threshold=0):
    height = len(frame)
    width = len(frame[0])
    result = [[0 for _ in range(width)] for _ in range(height)]

    for i in range(height):
        for j in range(width):
            diff = abs(frame[i][j] - background[i][j])
            result[i][j] = 255 if diff > threshold else 0
    return result
def frame_differencing(frame, prev_frame, threshold=30):
    height = len(frame)
    width = len(frame[0])
    result =  [[0 for _ in range(width)] for _ in range(height)]

    for i in range(height):
        for j in range(width):
            diff = abs(frame[i][j] - prev_frame[i][j])
            result[i][j] = 255 if diff > threshold else 0
    return result
def running_average(frame, background, alpha=0.1, threshold=0):
    height = len(frame)
    width = len(frame[0])
    result = [[0 for _ in range(width)] for _ in range(height)]

    new_background = [[0 for _ in range(width)] for _ in range(height)]


    for i in range(height):
        for j in range(width):
            # Update background with weighted average
            new_background[i][j] = int(alpha*frame[i][j] + (1-alpha)*background[i][j])

            # Foreground mask
            diff = abs(frame[i][j] - new_background[i][j])
            result[i][j] = 255 if diff > threshold else 0
    return result, new_background

# Initial background = first frame
background = frame1

# Background subtraction
fg1 = background_subtraction(frame2, background)

# Frame differencing
fg2 = frame_differencing(frame2, frame1)

# Running average
fg3, new_background = running_average(frame2, background, alpha=0.2)
write_pgm('frame1.ppm', frame1)
write_pgm('frame2.ppm', frame2)
write_pgm('fg_background_subtraction.ppm', fg1)
write_pgm('fg_frame_differencing.ppm', fg2) 
write_pgm('fg_running_average.ppm', fg3)
write_pgm('updated_background.ppm', new_background)