import bpy

objs = bpy.context.selected_objects
def delete_uv_groups():
    for obj in objs:
        bpy.context.scene.objects.active = obj
        obj.select = True
        if obj.type == 'MESH':
            uv_textures = obj.data.uv_textures
            for i in range(0, len(uv_textures)):
                uv_textures.remove(uv_textures[0])
            obj.select = False
        else:
            obj.select = False
            continue
delete_uv_groups()