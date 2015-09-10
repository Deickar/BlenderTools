import bpy

objs = bpy.context.selected_objects
def uv_multiple():
    for obj in objs:
        bpy.context.scene.objects.active = obj
        obj.select = True
        if obj.type == 'MESH':
            bpy.ops.object.mode_set(mode='EDIT', toggle=False)
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.uv.smart_project()
            bpy.ops.mesh.select_all(action='DESELECT')
            bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
            obj.select = False
        else:
            obj.select = False
            continue
uv_multiple()