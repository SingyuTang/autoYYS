import action
width, height = action.grab_resolution()
#截屏，并裁剪以加速
# upleft = (0, 0)
# downright = (width, height)
x0,y0 = (0,0)
x1,y1 = (width, height)
monitor = {"top": x0, "left": y0, "width": x1, "height": y1}