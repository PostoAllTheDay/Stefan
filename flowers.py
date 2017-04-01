import turtle
ada = turtle.Pen()
ada.shape("turtle")
ada.speed(10)
for i in range (4):
    for j in range(4):
        ada.fd(50)
        ada.lt(60)
        ada.fd(50)
        ada.lt(60)
        ada.fd(50)
        ada.lt(60)
        ada.lt(30)

ada.fd(50)
ada.pu()
ada.fd(100)
ada.pd()

for k in range(29):
    ada.fd(100)
    ada.lt(120)
    ada.lt(45)

ada.pu()
ada.fd(300)
ada.pd()

for a in range(8):
    for b in range(4):
        ada.lt(90)
        ada.fd(30)
        ada.pu()
        ada.fd(10)
        ada.pd()
        ada.fd(30)
    ada.lt(45)

ada.lt(45)
ada.pu()
ada.fd(200)
ada.pd()

ada.reset()
ada.down()
ada.speed(22)
for i in range(1000):
    ada.fd(i)
    ada.lt(22222)
