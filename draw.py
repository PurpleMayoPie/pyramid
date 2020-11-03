

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    shape = input("Shape?: ").lower()
    if shape == "pyramid" or shape == "square" or shape == "triangle" or shape == "diamond" or shape == "trapeze" or shape == "parallelogram":
        return shape
    else:
        return get_shape()

# TODO: Step 1 - get height (it must be int!)
def get_height():
    
    height = input("Height?: ")
    if height.isdigit() and int(height) <= 80:
        return int(height)
    else:
        return get_height()

# TODO: Step 2
def draw_pyramid(height, outline):
    count = height
    if outline == False:
        space = height - 2
        star = 3
        print(" "*(height - 1) + "*")
        for i in range(height - 1):
            print(" "*(space) + "*"*(star))
            space -= 1
            star += 2

    if outline == True:
        stars = ("*")
        count = height - 1      
        inside = 1
        print(" "*(height-1) + "*")
        for p in range(height-2):
            print(" "*(count - 1) + "*" + " "*(inside) + "*")
            count -= 1
            inside += 2
        print("*"*(height * 2 - 1))


  
# TODO: Step 3
def draw_square(height, outline):
    i = 0
    j = 0
    if outline == False:
        for i in range(height):
            print("*"*(height))
    if outline == True:
        print("*"*(height))
        for j in range(height - 2):
            print("*" + " "*(height - 2) + "*")
        print("*"*(height))

# TODO: Step 4
def draw_triangle(height, outline):
    j = 0
    k = height
    i = 0
    if outline == False:
        for i in range(1, height + 1):
            print("*"*(i))

    if outline == True:
     count = 1
     print("*")
     print("**")
     while count < height - 2:
         print("*" + " "*(count) + "*")
         count += 1
     print("*"*(height))

def draw_diamond(height, outline):
    if outline == False:
     if height <= 5:
         inside = height + 2
         print(" " + "*"*(height))
         for i in range(height):
             print(" "*(i) + "*"*(inside))
             inside -= 2
     if height >= 6:
         inside = height + 2
         test = height - 5
         print(" " + "*"*(height + test))
         for i in range(height - 1):
             print(" "*(i) + "*"*(inside + test))
             inside -= 2
    if outline == True:
         testinside = height - 5
         print(" " + "*"*(height + testinside))
         for j in range(height - 2):
             print(" "*(j) + "*" + " "*(height + testinside) + "*")
             testinside -= 2
         print(" "*(j + 1) + "*")

def draw_trapeze(height, outline):
    if outline == False:
        side_space = height - 1
        star = height
        for j in range(height):
            print(" "*(side_space) + "*"*(star))
            side_space -= 1
            star += 2

    if outline == True:
        side_space = height - 2
        inside_space = height
        print(" "*(height - 1) + "*"*(height))
        for i in range(height - 2):
         print(" "*(side_space) + "*" + " "*(inside_space) + "*")
         side_space -= 1
         inside_space += 2
        print("*"*(height * 3 - 2))
         
def draw_parallelogram(height, outline):
    if outline == False:
        extra = height * 3
        space = height - 1
        for i in range(height):
            print(" "*(space) + "*"*(height + extra))
            space -= 1
    
    if outline == True:
        space = height - 2
        extra = height * 3
        print(" "*(height - 1) + "*"*(height + extra))
        for j in range(height - 2):
         print(" "*(space) + "*" + " "*(height + extra - 2) + "*")
         space -= 1
        print("*"*(height + extra))






# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):

    if shape == "square":
        draw_square(height, outline)
    elif shape == "triangle":
          draw_triangle(height, outline)
    elif shape == "pyramid":
          draw_pyramid(height, outline)
    elif shape == "diamond":
          draw_diamond(height, outline)
    elif shape == "trapeze":
         draw_trapeze(height, outline)
    elif shape == "parallelogram":
         draw_parallelogram(height, outline)
    else:
        get_shape()
    #draw_pyramid(height, outline)


# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    lines = input("Outline? [y/n]: ")

    if lines == "y":
        return True
    else:
     return False


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

