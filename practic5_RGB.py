'''The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal
representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range
must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:
rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
'''


def rgb(r, g, b):
    rgb_dex = [r, g, b]
    rgb_hex = []
    for i in rgb_dex:
        if 0 <= i < 256 and i < 16:
            rgb_hex.append('0' + hex(int(i)))
        elif 0 <= i < 256 and i >= 16:
            rgb_hex.append(hex(int(i)))
        elif i < 0:
            rgb_hex.append('0' + hex(int(0)))
        else:
            rgb_hex.append(hex(int(255)))
    return ''.join(rgb_hex).replace('0x', '').upper()

rgb(16, 151, 281)
rgb(14, 275, 125)
rgb(16, 275, 125)
rgb(-20, 275, 125)
rgb(255, 255, 255)
rgb(0, 0, 0)
rgb(1, 2, 3)
rgb(-5, 900, 5)

# test.assert_equals(rgb(0,0,0),"000000", "testing zero values")
# test.assert_equals(rgb(1,2,3),"010203", "testing near zero values")
# test.assert_equals(rgb(255,255,255), "FFFFFF", "testing max values")
# test.assert_equals(rgb(254,253,252), "FEFDFC", "testing near max values")
# test.assert_equals(rgb(-20,275,125), "00FF7D", "testing out of range values")

def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    print(("{:02X}" * 3).format(round(r), round(g), round(b)))

print(f'{255:X}')
print(hex(100))
print('#' * 100)
rgb(16, 151, 281)
rgb(14, 275, 125)
rgb(16, 275, 125)
rgb(-20, 275, 125)
rgb(255, 255, 255)
rgb(0, 0, 0)
rgb(1, 2, 3)
rgb(-5, 900, 5)
