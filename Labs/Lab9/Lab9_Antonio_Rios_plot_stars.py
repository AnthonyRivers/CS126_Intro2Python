# Antonio Rios
# October 29, 2014
# CS126 Lab9
# Lab9: Draw Stars
# ##########################


import turtle

t = turtle.Turtle()
t.screen.tracer(1000)

# Global variable to keep track of
# stars with no name
count = 0


def read_coords(file):
    '''Given a text file that contains a star catalog
    returns three dictionaries as a tuple'''

    # Define 3 empty dictionaries
    xy_coordinates = {}
    magnitude = {}
    star_names = {}

    # Create the file handler
    stars_file = open(file, "r")

    # Loop through each line in the file
    for line in stars_file:

        # Split each line to create a list
        star_coord_list = line.split()

        # Create the first dictionary with
        # the keys being the Henry Draper
        # numbers. The nested dictionary
        # has 'x' and 'y' as keys.
        xy_coordinates[star_coord_list[3]] = {'x': star_coord_list[0],
                                              'y': star_coord_list[1]}
        # Create the second dictionary
        # the key of the dictionary is also
        # the Henry Draper numbers. The nested
        # key is 'magnitude' and its value
        # is the magnitude.
        magnitude[star_coord_list[3]] = {'magnitude': star_coord_list[4]}

        # Check to see if the lenght of list for each line
        # has 7 elements. If it has 7 elements then
        # it means that the star has a name.
        if len(star_coord_list) >= 7:

            # Join the list to a string
            # and slice the string to
            # just get the name out of the
            # string.
            names = ' '.join(star_coord_list[6:])

            # If the string contains a ';' then
            # it means that the star has two names.
            # Split the string and use each name
            # as a key for the star_names dictionary.
            # Strip the name of all white spaces before
            # or after the name.
            if ';' in names:
                second_name = names.split(';')
                star_names[second_name[0].strip()] = star_coord_list[3]
                star_names[second_name[1].strip()] = star_coord_list[3]

            # If the name has only a space
            # then it is still part of the
            # first name.
            elif ' ' in names:
                star_names[names.strip()] = star_coord_list[3]

        # If the name is less than or equal to 6
        # then this means that the star has no name.
        # We used a count variable to keep track of the
        # stars that have no names and used that as
        # the key for the star_names dictionary.
        elif len(star_coord_list) <= 6:
            global count
            no_name = 'No Name ' + str(count)
            star_names[no_name] = star_coord_list[3]
            count += 1

    stars_file.close()

    # print('xy_coordinates dict', xy_coordinates)
    # print('magnitude dict', magnitude)
    # print('star names', star_names)
    return (xy_coordinates, magnitude, star_names)


def plot_plain_stars(picture_size, coordinates):
    xy_coord, magnitude, star_names = coordinates

    t.ht()
    t.screen.bgcolor("black")
    t.pen(fillcolor="white", pencolor="white", pensize=1)
    t.up()

    for star in star_names:
        point_x, point_y = coords_to_pixel(xy_coord[star_names[star]]['x'],
                                           xy_coord[star_names[star]]['y'],
                                           picture_size)

        t.goto(point_x, point_y)
        t.down()
        t.begin_fill()

        # Draw the square of 2x2 pixels
        for i in range(4):
            t.fd(2)
            t.rt(90)

        t.end_fill()
        t.up()
    turtle.Screen().exitonclick()

    return t.screen.getcanvas()


def plot_by_magnitude(picture_size, coord_dict, mag_dict):

    t.ht()
    t.screen.bgcolor("black")
    t.pen(fillcolor="white", pencolor="white", pensize=1)
    t.up()

    for star in mag_dict:
        #print(magnitudes_dict[star]['magnitude'])
        star_size = round(10.0 / (float(mag_dict[star]['magnitude']) + 2))
        #print(star_size)

        point_x, point_y = coords_to_pixel(coord_dict[star]['x'],
                                           float(coord_dict[star]['y']),
                                           (500, 500))
        #print(point_x, point_y)
        t.goto(point_x, point_y)
        t.down()
        t.begin_fill()

        #Draw star base on star_size
        for i in range(4):
            if star_size > 8:
                t.fd(8)
            else:
                t.fd(star_size)
            t.rt(90)

        t.end_fill()
        t.up()

    turtle.Screen().exitonclick()


def coords_to_pixel(orgi_x, orig_y, size):

    width, length = size

    width /= 2
    length /= 2

    x_pixel = (int(width) * float(orgi_x)) + int(width)
    y_pixel = (int(length) * float(orig_y))
    #print(x_pixel, y_pixel)
    return (int(x_pixel), int(y_pixel))


# Test code
coordinates, magnitude, star_names = read_coords("stars.txt")
plot_plain_stars((500, 500), read_coords("stars.txt"))
#print(plot_by_magnitude((500, 500), coordinates, magnitude))
