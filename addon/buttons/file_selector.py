import bpy
from bpy_extras.io_utils import ExportHelper

class WMFileSelector(bpy.types.Operator, ExportHelper):
    bl_idname = "custom.identifier_selector"
    bl_label = "folder"

    filename_ext = ""

    def execute(self, context):
        fdir = self.properties.filepath
        context.scene.road_tool.directory = fdir
        return {'FINISHED'}