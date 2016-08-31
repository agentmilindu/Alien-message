import png

#zooming effect
def n_plicate(original_list, n):
    return reduce(lambda x,y: x+y, map(lambda x: [x]*n, original_list))

palette = [(0x55,0x55,0x55), (0xff,0x99,0x99)]
l = "00110000011000111111110110010011001001100101111000100100010010001001001100110"
img = open('alien.png', 'wb')
m = []

m = [ n_plicate(l[i:i+7], 100) for i in range(0,len(l), 7) ]
m = n_plicate(m, 100)
w = png.Writer(700,1100, palette=palette, bitdepth=1)
w.write(img, m)
