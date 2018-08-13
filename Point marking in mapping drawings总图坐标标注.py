# -- coding: utf-8 --
#这段代码的功能是画一个引线标注，自动给出起点的XY坐标，第一个点是需要标注的坐标点位置
#注意: rhino的单位默认为MM, 测绘图的坐标体系X为建筑专业平面图竖坐标，Y为横坐标
#引线的默认尺寸画完后在属性里可以改
import rhinoscriptsyntax as rs

leaderB = rs.GetPoints(True, False, "Select leader points")
PC_B=leaderB[0]
PS_B=repr (PC_B)

#Attention that the Mapping Drawing X is the vertical co-ordinates in CAD plan 
XB0=float(PS_B.split('[')[-1].split(',')[1])
YB0=float(PS_B.split('[')[-1].split(',')[0])
#When the rhino Unit is mm,IF not comment out the next line 注意rhino的单位默认为MM，测绘图为米，如果都是米则下面一行前加#号
XB0=XB0/1000
XB=round(XB0,3)
#When the rhino Unit is mm,IF not comment out the next line 注意rhino的单位默认为MM，测绘图为米，如果都是米则下面一行前加#号
YB0=YB0/1000
YB=round(YB0,3)

if PS_B: rs.AddLeader( leaderB,None,"X=%s\nY=%s"%(XB,YB)) 
