#!/usr/bin/python
n = 250000.0
xmax = 100.0
dx = float(xmax/n)
dy = float(dx)
f = open("_heatmap.gx", "w")
i = 0
print dx,dy
for i in range(int(n)):
    ax = i * dx
    ay = float(i * dy)
    bx = float((i+1) *dx)
    by = float(ay)
    cx = float(ax)
    cy = float((i + 1) *dy)
    dxx = float(bx)
    dyx = float(cy)
   
    f.write("set object {0} polygon from {1},{2} to {3},{4} to {5},{6} to {7},{8} to {1},{2} fc \"blue\"\n".format(int(n - i), ax,ay,bx,by,dxx,dyx,cx,cy,ax,ay))
f.close()
