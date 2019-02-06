import arcpy,string

from arcpy import env

from arcpy.sa import*

arcpy.CheckOutExtension("spatial")

env.workspace=r'D:\test3'

input=r'C:\Users\Apurva\Documents\ArcGIS\Worldview2\053964097050_01_P001_MUL\13JU L08111238-M2AS_R04C2-053964097050_01_P001.TIF'

result = "outputName.tif"

NIR = input + "\Band_6"

Red = input + "\Band_2"

red = arcpy.sa.Raster(input+'/Band_2')

NIR = arcpy.sa.Raster(input+'/Band_6')

num = arcpy.sa.Float(NIR-red)

denom = arcpy.sa.Float(NIR+red)

NDVI = arcpy.sa.Divide(num, denom)

NDVI.save(result)