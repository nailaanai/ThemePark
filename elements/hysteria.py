import math
import elements.basics as basics
import primitif.basic as basic
import tools.utility as utility
import tools.modifier as modifier
import tools.objectProperty as objectProperty
import bpy
from importlib import reload
import random
reload(basics)

class Hysteria(basics.BasicElement):
    def _init_(self, name, coordinates):
        coordinates = (coordinates[0], coordinates[1], coordinates[2] + 1)
        super()._init_(name, coordinates)

    def create(self):

        atap = basic.Cube(name="atap", coords=(0,0,200))
        atap.scale((40,40,10))
        atap.rotate((0,0,-45))

        center_pole = basic.Cylinder(name="center_pole", coords=(0, 0, 100))
        center_pole.scale((22, 22, 100))  
            
        penyangga1 = basic.Cylinder(name="penyangga1", coords=(-25, 0, 100))
        penyangga1.scale((6, 6, 100))      
        
        penyangga2 = basic.Cylinder(name="penyangga2", coords=(25, 0, 100))
        penyangga2.scale((6, 6, 100))    

        penyangga3 = basic.Cylinder(name="penyangga3", coords=(0, -25, 100))
        penyangga3.scale((6, 6, 100))    

        penyangga4 = basic.Cylinder(name="penyangga4", coords=(0, 25, 100))
        penyangga4.scale((6, 6, 100))     

        Cutter1 = basic.Cylinder(name="Cutter1", coords=(0, 0, 100))
        Cutter1.scale((50, 50, 15)) 
        Cutter1 = bpy.context.object
    
        yangNaikTurun = basic.Cylinder(name="yangNaikTurun", coords=(0, 0, 100))
        yangNaikTurun.scale((40, 40, 15)) 
        yangNaikTurun = bpy.context.object

        bool_mod = Cutter1.modifiers.new(type="BOOLEAN", name="Boolean")
        bool_mod.object = yangNaikTurun
        bool_mod.operation = 'DIFFERENCE'

        bpy.context.view_layer.objects.active = Cutter1
        bpy.ops.object.modifier_apply(modifier="Boolean")
        bpy.data.objects.remove(yangNaikTurun, do_unlink=True)

        rotate = 0
        for i in range(0, 360, 20):
            rotate += 60
            x = 60 * math.cos(math.radians(i))
            y = 60 * math.sin(math.radians(i))
            kursi1 = Chair("chair",(x, y, 90))
            kursi1.rotate((0,0,i+90))
        # kursi2 = Chair("chair2",(17, -59, 90))

        self.mainObject=center_pole.object


class Chair(basics.BasicElement):
    def create(self):
        seat = basic.Cube(name="tempat_duduk", coords=(0, -51, 0))
        seat.scale((8, 6, 2))
        
        atasKursi = basic.Cube(name="atas_kursi", coords=(0, -51, 10))
        atasKursi.scale((8, -2, 12))
        
        pengamanKanan = basic.Cube(name="pengaman_kanan", coords=(6.0389,-57.232,11.098))
        pengamanKanan.scale((-0.757, -0.557, 12.000))
        pengamanKanan.rotate((-27.858, -0.86724, -0.20174))
        
        pengamanKiri = basic.Cube(name="pengaman_kiri", coords=(-6.0905, -57.56, 10.15))
        pengamanKiri.scale((-0.757, -0.557, 12.000))
        pengamanKiri.rotate((-26.928, -0.92175, -0.13101))

        pengamanBawah = basic.Cube(name="pengaman_Bawah", coords=(0.040151, -61, 2.8849))
        pengamanBawah.scale((-0.757, -0.557, 6.202))
        pengamanBawah.rotate((-76.986, 87.504, -77.137))

        utility.parent_objects(seat.object, atasKursi.object)
        utility.parent_objects(atasKursi.object, pengamanKanan.object)
        utility.parent_objects(atasKursi.object, pengamanKiri.object)
        utility.parent_objects(atasKursi.object, pengamanBawah.object)

        atasKursi.translate((0, -4, 0))
        

        self.mainObject = seat.object