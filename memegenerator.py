#Created by Nelson Dellis
#Documentation for PIL: https://pillow.readthedocs.io/en/stable/reference/Image.html

from PIL import Image, ImageDraw, ImageFont
import sys

######TASK1 : STUDENT MUST MODIFY##########
#1. Replace the following Python statement instead to ask user to enter name of the image file and save to a variable filename
filename = input('What is the name of your image file? (include extension): ')

#2. Replace the following Python statement instead to ask user to enter text for the meme and store in a variable text
# To add multiple lines to the text, include a '\n' character within the text
# In the default example shown below, you will see the text 'into Mordor' will appear on the second line.
text = input('What text do you want to store in your meme?: ')

#3. Replace the following Python statement instead to ask user to enter color for the text in the meme and store in a variable color
#User can enter the names of anyone of the 140 HTML colors: https://htmlcolorcodes.com/color-names/
color = input('What color do you want the text to be?: ')

#4. Replace the following Python statement instead to ask user to enter a number to scale the image and store in variable resize_scale
# This value must be converted into a float using the float() function, similar to int()
# int() converts string to int, float() converts string to a real number
# If user enters 1, image will not be resized.
# If user enters 0.5, width and height of image will be halved.
# If user enters 2, width and height of image will be doubled.
resize_scale = float(input("What scale do you want your image to be?: "))

#5. Replace the following Python statement instead to ask user to enter name of the final image and store in a variable outfile
outfile = input("What do you want your final image to be named?: ")
##########END MODIFY###############

im = Image.open(filename)

img_width, img_height = im.size

#get a drawing context
draw = ImageDraw.Draw(im)

#draw multiline text
text_width, text_height = draw.textsize(text)

######TASK 2: STUDENT MUST MODIFY##########
#Replace the following two Python statements with mathematical
#expressions to compute new_x and new_y
#so that the text is centered at the bottom of the image
#see pdf for what the modified image should look like
new_x = (img_width - text_width)/2
new_y = (img_height - text_height)

##########END MODIFY###############

#Prints text at the new location, with the color requested by the user
draw.multiline_text((new_x,new_y), text, fill=color, align='center')

#Make the new image half the width and half the height of the original image
resized_im = im.resize((round(im.size[0]*resize_scale), round(im.size[1]*resize_scale)))

#Display the resized imaged
resized_im.show()

#Saves the image
resized_im.save(outfile+'.jpg')
