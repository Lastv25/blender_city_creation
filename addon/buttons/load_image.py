import bpy
 
class loadImage(bpy.types.Operator):
    bl_idname = 'custom.load_road_image'
    bl_label = 'Load Image'
 
    def execute(self, context):
        print('Current City:', context.scene.city_name)
        return {"FINISHED"}