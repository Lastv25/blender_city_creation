import bpy
import os
from .. request_scripts.get_data import get_city_info
 
class loadImage(bpy.types.Operator):
    bl_idname = 'custom.load_road_image'
    bl_label = 'Load Image'
 
    def __init__(self):
        print("Start")

    def __del__(self):
        print("End")
        
    def execute(self, context):
        if len(context.scene.road_tool.city_name) > 0 :
            if context.scene.road_tool.download and not context.scene.road_tool.use_file:
                print('download call')
                if len(context.scene.road_tool.directory) > 0:
                    if os.path.exists(context.scene.road_tool.directory):
                        if os.path.isfile(context.scene.road_tool.directory):
                            print('1 Download will write in file', context.scene.road_tool.directory)
                            get_city_info(context.scene.road_tool.city_name, context.scene.road_tool.directory)
                        elif os.path.isdir(context.scene.road_tool.directory):
                            if context.scene.road_tool.directory[-1] == '/':
                                new_path = context.scene.road_tool.directory+context.scene.road_tool.city_name+'.geojson'
                                print('2 Download will write in file', new_path)
                                get_city_info(context.scene.road_tool.city_name, new_path)
                            else:
                                new_path = context.scene.road_tool.directory+'/'+context.scene.road_tool.city_name+'.geojson'
                                print('3 Download will write in file', new_path)
                                get_city_info(context.scene.road_tool.city_name, new_path)
                    else:
                        print('Please enter a valid path and name')
                else:
                    print('Please enter a valid Path')
                
            elif not context.scene.road_tool.download and context.scene.road_tool.use_file:
                print('use existing file')
            else:
                print('Only one option should be selected')
        else:
            print('please enter a city name')   
        
        return {"FINISHED"}