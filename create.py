N=767
M=5000
d=0.001
f = open("plot_" + str(N) + "_heatmap.gx", "w")
for i in range(N):
    for j in range(M):
	x1 = d * i
	y1 = d * j
	x2 = x1 + d
	y2 = y1 + d
	f.write("set object {0} polygon from {1},{2} to {3},{4} to {5},{6} to {7},{8} to {1},{2} fs solid 1 fc palette cb 0.123456\n".format(N*M - M*i - j + 1, x1,y1,x1,y2,x2,y2,x2,y1))
