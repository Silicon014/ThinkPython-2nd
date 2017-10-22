import turtle#导入turtle模块用来画线
import math#导入math模块用来提供高级计算功能(三角函数和常数pi)
def polyline(t, n, l, a):
	#多边形，n条长为l的边，每条边之间角度（外角）为a
	for i in range(n):#执行n遍
		t.fd(l)#画长为l的线
		t.lt(a)#向左转a度
def arc(t, r, a):
	#弧线，半径为r,转过的角度为a（弧度）
	length = a * r#计算弧线长度
	#弧线可以近似为由许多短边构成的多边形
	n = int(length / 3) + 1#短边的总数约为弧线总长的3分之1，
	step_length = length / n#即每条短边的长度约为3
	step_angle = a * 180 / math.pi / n#先把弧度转化为角度，再除以n，得到每次需要转的角度
	#使用上面的polyline（）函数画多边形
	polyline(t, n, step_length, step_angle)
def fp(t, r, a):
	#画单个花瓣,花瓣长为r，尖角的角度为a
	radius = (r / 2) / math.sin(angle / 2)#计算弧线的半径
	arc(t, radius, angle)#画弧线
	t.lt(180 - a)#调转方向
	arc(t, radius, angle)#画另一半弧线
	t.lt(180)#再转方向,以备画下一个花瓣
def flower_single(t, r, n):
	#用来画单层花的函数
	#花的半径为r，花瓣数为n
	angle = 360 / n#计算一个花瓣所占的角度
	for i in range(n):#下面的语句执行n遍：
		fp(t, r, angle)#调用fp（）函数画一个花瓣
def flower_double(t, r, n):
	#用来画双层花的函数
	angle = 360 / n#计算角度
	for i in range(n):#画第一层
		fp(t, r, angle)
	t.lt(angle / 2)#两层错开以防重叠
	for i in range(n):#画第二层
		fp(t, r, angle)
#从这里开始执行:
bob = turtle.Turtle()#启动画线器
flower_double(bob, 200, 5)#调用flower_double（）函数，用画线器绘制半径为200，每层花瓣数为5的双层花
turtle.mainloop()#窗口保持打开(否则会自动关闭)
