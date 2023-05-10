'''You must make a system to count the
number of errors occurred in a factory. Errors will be identified by
images. The images will be composed of zeros and ones. You must identify the
amount of errors occurred in an image, looking for a pattern
(looking for a template). The template will also be represented by a
image of zeros and ones, but always with dimensions smaller than the image
original. All locations in the original image that match this template must
be counted as an error. The search must be done by scanning the entire original image.
ATTENTION: Be careful not to extrapolate the dimensions of the image when scanning with the
template.
Input: The input consists of two images, one representing the original image and the other
representing the error template image. Each image will be described by two integers
L and C representing respectively the number of lines and
columns of the image followed by the elements of the image itself. The elements of the image
will be given in L rows and C columns. See input examples below.
• Output: The output should inform the number of errors found, following the format
“RESP:#”, where # represents the number of errors found. '''

#**********MAP***********
linesMap = int(input(''))
columnsMap = int(input(''))
map = list()
for count in range(0, linesMap):
    line = str(input(''))
    map.append(line[:])

#**********TEMPLATE********
linesTemplate = int(input(''))
columnsTemplate = int(input(''))
template = list()
for count in range(0, linesTemplate):
    line = str(input(''))
    template.append(line[:])

#*******LOOKING FOR ERROR*********
corresponds = 0
NumberOfErrors = 0
for L_map in range(0, linesMap):
    for C_map in range(0, columnsMap):
        
        for L_temp in range(0, linesTemplate):
            for C_temp in range(0, columnsTemplate):
                
                if L_map+L_temp<linesMap and C_map+C_temp<columnsMap and map[L_map+L_temp][C_map+C_temp] == template[L_temp][C_temp]:
                    corresponds+=1
        
        if corresponds == linesTemplate*columnsTemplate:
            NumberOfErrors+=1
        corresponds = 0
print(f'RESP:{NumberOfErrors}', end='')