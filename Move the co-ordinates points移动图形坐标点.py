import rhinoscriptsyntax as rs
pA = rs.GetPoint("Pick point 0")
psA=repr (pA)
XA0=float(psA.split('[')[-1].split(',')[0])
YA0=float(psA.split('[')[-1].split(',')[1])
#Attention that the defaut  rhino Unit is mm
rs.AddLine( (XA0,YA0,0),(455094483,3467361496,0) )