import bpy
import bmesh

class DepthifyAddonPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__

    def draw(self, context):
        layout = self.layout
        layout.label(text="No preferences available yet.")

class DepthifyOperator(bpy.types.Operator):
    bl_idname = "object.depthify_operator"
    bl_label = "Apply Depthify"
    
    # UI feedback properties
    bl_options = {'REGISTER', 'UNDO'}
    progress: bpy.props.StringProperty(name="Progress", default="Idle")

    # Properties for user input
    depth_map: bpy.props.StringProperty(name="Depth Map", subtype='FILE_PATH')
    diffusion_texture: bpy.props.StringProperty(name="Diffusion Texture", subtype='FILE_PATH')
    depth_scale: bpy.props.FloatProperty(name="Depth Scale", default=1.0, min=0.0, max=10.0)
    invert_depth: bpy.props.BoolProperty(name="Invert Depth", default=False)

    def execute(self, context):
        try:
            self.progress = "Loading Images"
            self.report({'INFO'}, self.progress)
            
            # Load images
            depth_map_image = self.load_image(self.depth_map)
            diffusion_texture_image = self.load_image(self.diffusion_texture) if self.diffusion_texture else None

            self.progress = "Generating Mesh"
            self.report({'INFO'}, self.progress)
            
            # Generate mesh
            base_plane = self.create_base_plane(context)
            self.apply_displacement(base_plane, depth_map_image, self.depth_scale, self.invert_depth)

            self.progress = "Applying Material"
            self.report({'INFO'}, self.progress)
            
            # Apply material
            if diffusion_texture_image:
                self.apply_material(base_plane, diffusion_texture_image)

            self.progress = "Finished"
            self.report({'INFO'}, "Depthify process completed successfully.")

        except Exception as e:
            self.report({'ERROR'}, f"Depthify failed: {str(e)}")
            return {'CANCELLED'}

        return {'FINISHED'}

    def load_image(self, file_path):
        if file_path:
            image = bpy.data.images.load(file_path)
            return image
        else:
            raise FileNotFoundError(f"File not found: {file_path}")

    def create_base_plane(self, context):
        bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False)
        plane = context.object
        return plane

    def apply_displacement(self, plane, depth_map_image, depth_scale, invert_depth):
        # Adaptive subdivision
        modifier = plane.modifiers.new("Subdivision", 'SUBSURF')
        modifier.levels = 6
        bpy.ops.object.modifier_apply(modifier="Subdivision")

        # Displacement
        displacement_modifier = plane.modifiers.new("Displace", 'DISPLACE')
        displacement_texture = bpy.data.textures.new("Displacement Texture", type='IMAGE')
        displacement_texture.image = depth_map_image

        displacement_modifier.texture = displacement_texture
        displacement_modifier.strength = -depth_scale if invert_depth else depth_scale
        bpy.ops.object.modifier_apply(modifier="Displace")

    def apply_material(self, plane, diffusion_texture_image):
        mat = bpy.data.materials.new(name="DepthifyMaterial")
        mat.use_nodes = True
        bsdf = mat.node_tree.nodes.get("Principled BSDF")
        tex_image_node = mat.node_tree.nodes.new('ShaderNodeTexImage')
        tex_image_node.image = diffusion_texture_image
        mat.node_tree.links.new(bsdf.inputs['Base Color'], tex_image_node.outputs['Color'])

        if plane.data.materials:
            plane.data.materials[0] = mat
        else:
            plane.data.materials.append(mat)

class DepthifyPanel(bpy.types.Panel):
    bl_idname = "VIEW3D_PT_depthify_panel"
    bl_label = "Depthify"
    bl_category = "Depthify"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = "objectmode"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        op = layout.operator(DepthifyOperator.bl_idname)
        op.depth_map = bpy.path.abspath("//depth_map.png")
        op.diffusion_texture = bpy.path.abspath("//diffusion_texture.png")
        layout.prop(op, "depth_scale")
        layout.prop(op, "invert_depth")
        layout.label(text=f"Progress: {op.progress}")

def register():
    bpy.utils.register_class(DepthifyAddonPreferences)
    bpy.utils.register_class(DepthifyOperator)
    bpy.utils.register_class(DepthifyPanel)

def unregister():
    bpy.utils.unregister_class(DepthifyAddonPreferences)
    bpy.utils.unregister_class(DepthifyOperator)
    bpy.utils.unregister_class(DepthifyPanel)

if __name__ == "__main__":
    register()
