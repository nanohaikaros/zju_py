from PIL import Image
im = Image.open('pybit.gif')
try:
    im.save('picframe{:02d}.png'.format(im.tell()))
    while True:
        im.seek(im.tell() + 1)
        im.save('picframe{:2d}.png'.format(im.tell()))
except:
    print("处理结束")