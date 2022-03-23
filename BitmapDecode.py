"""
Encode PPM file to RV32I compatible Data Block for PolyPlatformers
"""

if __name__ == '__main__':
    with open('PerryPlat.ppm', 'r') as image:
        image_dump = image.readlines()
    image_list = image_dump[4:]

    output_string = '.data .byte \n'
    value_temp = ''
    while image_list:
        # print(image_list)
        blue = int(image_list.pop(-3).rstrip("\n"))
        green = int(image_list.pop(-2).rstrip("\n"))
        red = int(image_list.pop(-1).rstrip("\n"))

        red_shift = red >> 5
        green_shift = green >> 5
        blue_shift = blue >> 6

        value_temp += str(bin(red_shift)).strip('0b').zfill(3)
        value_temp += str(bin(green_shift)).strip('0b').zfill(3)
        value_temp += str(bin(blue_shift)).strip('0b').zfill(2)
        hex_temp = hex(int(value_temp, 2))
        hex_temp += ',\n'
        # print(hex_temp)
        value_temp = ''
        output_string += hex_temp

    print(output_string)

