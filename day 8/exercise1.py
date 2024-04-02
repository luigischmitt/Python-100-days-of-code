import math

def paint_calc(height, width, cover):
    result = math.ceil(height * width / cover)
    print(f"You'll need {result} cans of paint.")
  
test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(test_h, test_w, coverage)
