#!/usr/bin/env python3

import pyemf

width=197
height=197
dpi=1

emf=pyemf.EMF(width,height,dpi)
thin=emf.CreatePen(pyemf.PS_SOLID,1,(0x01,0x02,0x03))
emf.Comment()
emf.SelectObject(thin)
emf.Rectangle(0, 0, width, height)
emf.save("test.emf")
