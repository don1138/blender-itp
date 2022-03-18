# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name"       : "ITP (Image Texture Properties)",
    "author"     : "Don Schnitzius",
    "version"    : (1, 0),
    "blender"    : (2, 80, 0),
    "location"   : "Node Editor > Sidebar > Node",
    "description": "Set Properties for Selected Image Nodes",
    "warning"    : "",
    "wiki_url"   : "https://github.com/don1138/blender-itp",
    "support"    : "COMMUNITY",
    "category"   : "Node",
}


"""
VERSION HISTORY

1.0 – 18/03/22
    – Create Addon
"""

import bpy
from bpy.types import Operator, Panel

not_image = "One or more nodes are not Image Textures"
def ShowMessageBox(message = "", title = "", icon = 'INFO'):
    def draw(self, context):
        self.layout.label(text=message)
    bpy.context.window_manager.popup_menu(draw, title = title, icon = icon)

def get_active_tree(context):
    tree = context.space_data.node_tree
    path = []
    if tree.nodes.active:
        while tree.nodes.active != context.active_node:
            tree = tree.nodes.active.node_tree
            path.append(tree)
    return tree, path

def get_nodes_links(context):
    tree, path = get_active_tree(context)
    return tree.nodes, tree.links

def whenUpdate( self, context ):
    nodes, links = get_nodes_links(context)
    for node in nodes:
        if node.select == True:
            if node.type == 'TEX_IMAGE':
                node.projection_blend = self.blend_val

class MyProperties(bpy.types.PropertyGroup):
    blend_val : bpy.props.FloatProperty(name = "Blend:", min = 0, max = 1, update = whenUpdate)

class RN_PT_NodeITPanel(Panel):
    bl_label       = "Image Texture Properties"
    bl_space_type  = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category    = "Node"

    def draw(self, context):
        if context.active_node is not None:
            layout = self.layout
            scene = context.scene
            mytool = scene.my_tool
            row = layout.row()
            node = context.space_data.node_tree.nodes.active
            if node and node.type == 'TEX_IMAGE':

                row = layout.row(align=True)
                row.label(text="Interpolation:")

                row = layout.row(align=True)
                row.operator('node.button_linear')
                row.operator('node.button_closest')

                row = layout.row(align=True)
                row.operator('node.button_cubic')
                row.operator('node.button_smart')


                row = layout.row(align=True)
                row.label(text="Projection:")

                row = layout.row(align=True)
                row.operator('node.button_flat')
                row.operator('node.button_box')

                row = layout.row(align=True)
                row.operator('node.button_sphere')
                row.operator('node.button_tube')

                if node.projection == 'BOX':
                    row = layout.row(align=True)
                    row.prop(mytool, "blend_val")


                row = layout.row(align=True)
                row.label(text="Extension:")

                row = layout.row(align=True)
                row.operator('node.button_repeat')

                row = layout.row(align=True)
                row.operator('node.button_extend')
                row.operator('node.button_clip')

            else:
                layout.label(text="(No Image Texture Selected)", icon='GHOST_DISABLED')

class RN_OT__NodeButtonLinear(Operator):

    'Set Image Texture interpolation to Linear'
    bl_idname = 'node.button_linear'
    bl_label  = 'Linear'

    def execute(self, context):
        nodes, links = get_nodes_links(context)
        for node in nodes:
            if node.select == True:
                if node.type == 'TEX_IMAGE':
                    node.interpolation = 'Linear'
                else:
                    print("Possible Error - One or more nodes are not Image Textures")
        return {'FINISHED'}

class RN_OT__NodeButtonClosest(Operator):

    'Set Image Texture interpolation to Closest'
    bl_idname = 'node.button_closest'
    bl_label  = 'Closest'

    def execute(self, context):
        nodes, links = get_nodes_links(context)
        for node in nodes:
            if node.select == True:
                if node.type == 'TEX_IMAGE':
                    node.interpolation = 'Closest'
                else:
                    print("Possible Error - One or more nodes are not Image Textures")
        return {'FINISHED'}

class RN_OT__NodeButtonCubic(Operator):

    'Set Image Texture interpolation to Cubic'
    bl_idname = 'node.button_cubic'
    bl_label  = 'Cubic'

    def execute(self, context):
        nodes, links = get_nodes_links(context)
        for node in nodes:
            if node.select == True:
                if node.type == 'TEX_IMAGE':
                    node.interpolation = 'Cubic'
                else:
                    print("Possible Error - One or more nodes are not Image Textures")
        return {'FINISHED'}

class RN_OT__NodeButtonSmart(Operator):

    'Set Image Texture interpolation to Smart'
    bl_idname = 'node.button_smart'
    bl_label  = 'Smart'

    def execute(self, context):
        nodes, links = get_nodes_links(context)
        for node in nodes:
            if node.select == True:
                if node.type == 'TEX_IMAGE':
                    node.interpolation = 'Smart'
                else:
                    print("Possible Error - One or more nodes are not Image Textures")
        return {'FINISHED'}



class RN_OT__NodeButtonFlat(Operator):

    'Set Image Texture projection to Flat'
    bl_idname = 'node.button_flat'
    bl_label  = 'Flat'

    def execute(self, context):
        nodes, links = get_nodes_links(context)
        for node in nodes:
            if node.select == True:
                if node.type == 'TEX_IMAGE':
                    node.projection = 'FLAT'
                else:
                    print("Possible Error - One or more nodes are not Image Textures")
        return {'FINISHED'}

class RN_OT__NodeButtonBox(Operator):

    'Set Image Texture projection to Box'
    bl_idname = 'node.button_box'
    bl_label  = 'Box'

    def execute(self, context):
        nodes, links = get_nodes_links(context)
        for node in nodes:
            if node.select == True:
                if node.type == 'TEX_IMAGE':
                    node.projection = 'BOX'
                else:
                    print("Possible Error - One or more nodes are not Image Textures")
        return {'FINISHED'}

class RN_OT__NodeButtonSphere(Operator):

    'Set Image Texture projection to Sphere'
    bl_idname = 'node.button_sphere'
    bl_label  = 'Sphere'

    def execute(self, context):
        nodes, links = get_nodes_links(context)
        for node in nodes:
            if node.select == True:
                if node.type == 'TEX_IMAGE':
                    node.projection = 'SPHERE'
                else:
                    print("Possible Error - One or more nodes are not Image Textures")
        return {'FINISHED'}

class RN_OT__NodeButtonTube(Operator):

    'Set Image Texture projection to TTube'
    bl_idname = 'node.button_tube'
    bl_label  = 'Tube'

    def execute(self, context):
        nodes, links = get_nodes_links(context)
        for node in nodes:
            if node.select == True:
                if node.type == 'TEX_IMAGE':
                    node.projection = 'TUBE'
                else:
                    print("Possible Error - One or more nodes are not Image Textures")
        return {'FINISHED'}



class RN_OT__NodeButtonRepeat(Operator):

    'Set Image Texture extension to Repeat'
    bl_idname = 'node.button_repeat'
    bl_label  = 'Repeat'

    def execute(self, context):
        nodes, links = get_nodes_links(context)
        for node in nodes:
            if node.select == True:
                if node.type == 'TEX_IMAGE':
                    node.extension = 'REPEAT'
                else:
                    print("Possible Error - One or more nodes are not Image Textures")
        return {'FINISHED'}

class RN_OT__NodeButtonExtend(Operator):

    'Set Image Texture extension to Extend'
    bl_idname = 'node.button_extend'
    bl_label  = 'Extend'

    def execute(self, context):
        nodes, links = get_nodes_links(context)
        for node in nodes:
            if node.select == True:
                if node.type == 'TEX_IMAGE':
                    node.extension = 'EXTEND'
                else:
                    print("Possible Error - One or more nodes are not Image Textures")
        return {'FINISHED'}

class RN_OT__NodeButtonClip(Operator):

    'Set Image Texture extension to Clip'
    bl_idname = 'node.button_clip'
    bl_label  = 'Clip'

    def execute(self, context):
        nodes, links = get_nodes_links(context)
        for node in nodes:
            if node.select == True:
                if node.type == 'TEX_IMAGE':
                    node.extension = 'CLIP'
                else:
                    print("Possible Error - One or more nodes are not Image Textures")
        return {'FINISHED'}



classes = [
    MyProperties,
    RN_PT_NodeITPanel,
    RN_OT__NodeButtonLinear,
    RN_OT__NodeButtonClosest,
    RN_OT__NodeButtonCubic,
    RN_OT__NodeButtonSmart,
    RN_OT__NodeButtonFlat,
    RN_OT__NodeButtonBox,
    RN_OT__NodeButtonSphere,
    RN_OT__NodeButtonTube,
    RN_OT__NodeButtonRepeat,
    RN_OT__NodeButtonExtend,
    RN_OT__NodeButtonClip
]

def register():
    for c in classes:
        bpy.utils.register_class(c)
        bpy.types.Scene.my_tool = bpy.props.PointerProperty(type = MyProperties)

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
        del bpy.types.Scene.my_tool

if __name__ == "__main__":
    register()
