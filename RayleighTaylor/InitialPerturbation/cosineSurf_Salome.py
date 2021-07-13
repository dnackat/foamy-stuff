
from salome.geom import geomBuilder
geompy = geomBuilder.New(salome.myStudy)
theStudy = salome.myStudy

import salome
import GEOM
import math
import numpy

gg = salome.ImportComponentGUI("GEOM")


#number of points to evaluate along radial direction
nsegs = 100  

#number of points to evaluate along angular direction
nsegs_angular = 200 

mindeg = 2
maxdeg = 5
tol3d = 0.0001
tol2d = 0.0001
nbiter = 0

v_array = numpy.linspace(-0.5,0.5,nsegs)
compoundlist = []

for v in v_array:
	XExpr = v #"%s * ( (%s+%s+%s+%s) * cos(t) + %s * cos(t)*cos(%s*t - %s*%s) ) + (%s+%s)*(1-%s)*cos(t)" % (v, R, d, w, rf, rf, c, omega, t, R, d, v)
	YExpr = 0.05*math.cos(-2*math.pi*v + math.pi) #"%s * ( (%s+%s+%s+%s) * sin(t) + %s * sin(t)*cos(%s*t - %s*%s) ) + (%s+%s)*(1-%s)*sin(t)" % (v, R, d, w, rf, rf, c, omega, t, R, d, v)
	#ZExpr = "%s * ( (%s+%s+%s+%s) * 0      + %s *        sin(%s*t - %s*%s) ) + (%s+%s)*(1-%s)*0"      % (v, R, d, w, rf, rf, c, omega, t, R, d, v)
	curve = geompy.MakeCurveParametric(XExpr, YExpr, 0, 0, 2*math.pi, nsegs_angular, GEOM.Interpolation, True)
	compoundlist.append(curve)
	

compound = geompy.MakeCompound(compoundlist)
filling = geompy.MakeFilling(compound,mindeg,maxdeg,tol2d,tol3d,nbiter,GEOM.FOM_Default,False)
id_filling = geompy.addToStudy(filling,"Filling")
gg.createAndDisplayGO(id_filling)
gg.setDisplayMode(id_filling,1)


#Sphere_1 = geompy.MakeSphereR(R+d)
#id_sphere = geompy.addToStudy( Sphere_1, 'Sphere_1' )
#gg.createAndDisplayGO(id_sphere)
#gg.setDisplayMode(id_sphere,1)


###
### SMESH component
###
#import  SMESH, SALOMEDS
#from salome.smesh import smeshBuilder
#smesh = smeshBuilder.New(theStudy)

#Mesh_1 = smesh.Mesh(filling)
#NETGEN_2D = Mesh_1.Triangle(algo=smeshBuilder.NETGEN_1D2D)
#NETGEN_2D_Parameters = NETGEN_2D.Parameters()
#NETGEN_2D_Parameters.SetSecondOrder( 1 )
#NETGEN_2D_Parameters.SetOptimize( 1 )
#NETGEN_2D_Parameters.SetUseSurfaceCurvature( 1 )
#NETGEN_2D_Parameters.SetFuseEdges( 1 )
#NETGEN_2D_Parameters.SetQuadAllowed( 0 )
#NETGEN_2D_Parameters.SetFineness( 0 )
#NETGEN_2D_Parameters.SetMaxSize( 0.7 )
#NETGEN_2D_Parameters.SetMinSize( 0.3 )
#isDone = Mesh_1.Compute()


#Mesh_2 = smesh.Mesh(Sphere_1)
#NETGEN_2D_1 = Mesh_2.Triangle(algo=smeshBuilder.NETGEN_1D2D)
#NETGEN_2D_Parameters_1 = NETGEN_2D_1.Parameters()
#NETGEN_2D_Parameters_1.SetMaxSize( 1 )
#NETGEN_2D_Parameters_1.SetSecondOrder( 1 )
#NETGEN_2D_Parameters_1.SetOptimize( 1 )
#NETGEN_2D_Parameters_1.SetFineness( 0 )
#NETGEN_2D_Parameters_1.SetMinSize( 0.5 )
#NETGEN_2D_Parameters_1.SetUseSurfaceCurvature( 1 )
#NETGEN_2D_Parameters_1.SetFuseEdges( 1 )
#NETGEN_2D_Parameters_1.SetQuadAllowed( 0 )

#isDone = Mesh_2.Compute()

