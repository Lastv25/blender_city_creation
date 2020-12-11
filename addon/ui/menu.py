import bpy

 

class panel1(bpy.types.Panel):
    bl_idname = "panel.Road_PT_Objects"
    bl_label = "Road Add On"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"

 

    def draw(self, context):
        layout = self.layout

        col = layout.column(align=True)
        rowsub = col.row(align=True)
        rowsub.prop(context.scene.road_tool, 'city_name')
        rowsub = col.row(align=True)

        col2 = layout.column(align=True)
        rowsub2 = col2.row(align=True)
        rowsub2.prop(context.scene.road_tool, 'download')
        rowsub2.prop(context.scene.road_tool, 'use_file')
        rowsub2 = col2.row(align=True)
        rowsub2 = col2.row(align=True)

        col3 = layout.column(align=True)
        rowsub3 = col3.row(align=True)
        rowsub3.prop(context.scene.road_tool, 'directory')
        rowsub3.operator("custom.identifier_selector", icon="FILE_FOLDER", text="")
        rowsub3 = col3.row(align=True)

        col4 = layout.column(align=True)
        rowsub4 = col4.row(align=True)
        rowsub4.operator("custom.load_road_image", icon='IMAGE')
        rowsub4 = col4.row(align=True)

        
        
 
