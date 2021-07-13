#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 20:49:03 2021

@author: dileepn
"""

import FreeCAD
from FreeCAD import Base, Vector
import Part
import math
import Draft 

DOC = FreeCAD.activeDocument()
DOC_NAME = "cosineSurf"

def clear_doc():
    """
    Clear the active document deleting all the objects
    """
    for obj in DOC.Objects:
        DOC.removeObject(obj.Name)

def setview():
    """Rearrange View"""
    FreeCAD.Gui.SendMsgToActiveView("ViewFit")
    FreeCAD.Gui.activeDocument().activeView().viewAxometric()


if DOC is None:
    FreeCAD.newDocument(DOC_NAME)
    FreeCAD.setActiveDocument(DOC_NAME)
    DOC = FreeCAD.activeDocument()

else:

    clear_doc()

# EPS= tolerance to use to cut the parts
EPS = 0.10
EPS_C = EPS * -0.5

# Cube
# def cubo(nome, lung, larg, alt):
#     obj_b = DOC.addObject("Part::Box", nome)
#     obj_b.Length = lung
#     obj_b.Width = larg
#     obj_b.Height = alt

#     DOC.recompute()

#     return obj_b

# # objects definition

# obj = cubo("test_cube", 5, 5, 5)

# Cosine wave
pts = []
radius = 10.
for ii in range(-180,180):
    pts.append(FreeCAD.Base.Vector(1000*ii/180.,50.*math.cos(-2*math.pi*ii/180. + math.pi),0))

Draft.makeBSpline(pts)

setview()