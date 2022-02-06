tpl=(23,45,12,67)

def addToTuple(a):
  a=3
  newtpl=list(tpl)
  x=newtpl.append(a)
  tpl=tuple(x)
  print(tpl)
addToTuple(a)