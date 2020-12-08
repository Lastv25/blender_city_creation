import bpy

class RoadPropertyGroup(bpy.types.PropertyGroup):

    city_name: bpy.props.StringProperty(
        name = "City Name",
        description = "Name of the city to load",
        default = "Melouse")

    use_file: bpy.props.BoolProperty(
        name="Download or Use Existing", 
        description="Bool to select an existing file", 
        default = True)