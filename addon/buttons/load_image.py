import bpy
from .. request_scripts.get_data import get_city_info
 
class loadImage(bpy.types.Operator):
    bl_idname = 'custom.load_road_image'
    bl_label = 'Load Image'
 
    def __init__(self):
        print("Start")

    def __del__(self):
        print("End")
        
    def execute(self, context):
        get_city_info(context.scene.road_tool.city_name)
        return {"FINISHED"}