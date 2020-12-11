import bpy



class RoadPropertyGroup(bpy.types.PropertyGroup):

    city_name: bpy.props.StringProperty(
        name = "City Name",
        description = "Name of the city to load",
        default = "Melouse")
    
    directory: bpy.props.StringProperty(
        name="Directory",
        description="Where I will save my stuff"
        )

    download: bpy.props.BoolProperty(
        name="Download", 
        description="Bool to select an existing file", 
        default = True)

    use_file: bpy.props.BoolProperty(
        name="Use Existing File", 
        description="Bool to select an existing file", 
        default = False)

    
