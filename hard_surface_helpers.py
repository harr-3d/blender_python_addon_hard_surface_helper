
bl_info = {
    "name": "Hard Surface Helpers",
    "author": "Harrison Noe",
    "version": (1, 0),
    "blender": (3, 6, 0),
    "description": "Hard Surface Modeling Helpers",
    "category": "Modeling Tools",
}

import bpy

class OBJECT_bevel_to_bottom(bpy.types.Operator):
    """Move the Bevel modifier to the bottom of object's modifier stack"""
    bl_idname = "object.move_modifier_to_bottom"
    bl_label = "Bevel to Bottom of Stack"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.selected_objects
    def execute(self, context):
        bottom = len(bpy.context.object.modifiers) - 1
        bpy.ops.object.modifier_move_to_index(modifier="Bevel", index = bottom)
        return {'FINISHED'}
    
class OBJECT_harden_bevel_normals(bpy.types.Operator):
    """Hardens the normals of the bevel"""
    bl_idname = "object.harden_normals"
    bl_label = "Harden Bevel Normals"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.selected_objects
    def execute(self, context):
        bpy.context.object.modifiers["Bevel"].harden_normals = True
        return {'FINISHED'}
    
class OBJECT_clamp_overlap_off(bpy.types.Operator):
    """Disables the clamp overlap of the bevel"""
    bl_idname = "object.disable_clamp_overlap"
    bl_label = "Disable Clamp Overlap"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.selected_objects
    def execute(self, context):
        bpy.context.object.modifiers["Bevel"].use_clamp_overlap = False
        return {'FINISHED'}
    
    
class OBJECT_PT_hard_surface_helpers(bpy.types.Panel):
    """Creates a Panel in the object context of the properties editor"""
    bl_label = "Hard Surface Helpers"
    bl_idname = "HARDSURFACEHELPERS_PT_layout"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Hard Surface Helpers"
    
    def draw(self, context):
        col = self.layout.column()
        
        row = col.row()
        col.operator(OBJECT_bevel_to_bottom.bl_idname)

        row = col.row()
        col.operator(OBJECT_harden_bevel_normals.bl_idname)

        row = col.row()
        col.operator(OBJECT_clamp_overlap_off.bl_idname)


def register():
    bpy.utils.register_class(OBJECT_PT_hard_surface_helpers)
    bpy.utils.register_class(OBJECT_bevel_to_bottom)
    bpy.utils.register_class(OBJECT_harden_bevel_normals)
    bpy.utils.register_class(OBJECT_clamp_overlap_off)

def unregister():
    bpy.utils.unregister_class(OBJECT_PT_hard_surface_helpers)
    bpy.utils.unregister_class(OBJECT_bevel_to_bottom)
    bpy.utils.unregister_class(OBJECT_harden_bevel_normals)
    bpy.utils.unregister_class(OBJECT_clamp_overlap_off)

if __name__ == "__main__":
    register()
