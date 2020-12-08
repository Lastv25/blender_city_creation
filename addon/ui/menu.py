import bpy

 

class panel1(bpy.types.Panel):
    bl_idname = "panel.RoadObjects"
    bl_label = "Road Add On"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"

 

    def draw(self, context):
        layout = self.layout

        col = layout.column(align=True)
        rowsub = col.row(align=True)
        rowsub.prop(context.scene, 'city_name')
        rowsub = col.row(align=True)

        col2 = layout.column(align=True)
        rowsub2 = col2.row(align=True)
        rowsub2.operator("custom.load_road_image", icon='IMAGE')
        rowsub2 = col.row(align=True)

        
        
 
