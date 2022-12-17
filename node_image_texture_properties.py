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
    "version"    : (1, 0, 3),
    "blender"    : (2, 80, 0),
    "location"   : "Node Editor > Sidebar > Node",
    "description": "Set Properties for Selected Image Nodes",
    "warning"    : "",
    "doc_url"    : "https://github.com/don1138/blender-itp",
    "support"    : "COMMUNITY",
    "category"   : "Node",
}


import bpy
from bpy.types import Operator, Panel


not_image = "One or more nodes are not Image Textures"


def ShowMessageBox(message="", title="", icon='INFO'):
    def draw(self, context):
        self.layout.label(text=message)
    bpy.context.window_manager.popup_menu(draw, title=title, icon=icon)


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


def whenUpdate(self, context):
    nodes, links = get_nodes_links(context)
    for node in nodes:
        if node.select == True and node.type == 'TEX_IMAGE':
            node.projection_blend = self.blend_val


class BlendValProperty(bpy.types.PropertyGroup):
    blend_val: bpy.props.FloatProperty(
        name="Blend:", min=0, max=1, update=whenUpdate)


class RN_PT_NodeITPanel(Panel):
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "Node"
    bl_label = "Image Texture Properties"

    def draw(self, context):
        if context.active_node is None:
            return
        layout = self.layout
        scene = context.scene
        row = layout.row()
        node = context.space_data.node_tree.nodes.active
        while node and node.type == "GROUP":
            node = node.node_tree.nodes.active
        if node and node.type == 'TEX_IMAGE':

            row = layout.row(align=True)
            row.label(text="Interpolation:")

            row = self.draw_button(
                layout, 'node.button_linear', 'node.button_closest'
            )
            row = self.draw_button(
                layout, 'node.button_cubic', 'node.button_smart'
            )
            row = layout.row(align=True)
            row.label(text="Projection:")

            row = self.draw_button(
                layout, 'node.button_flat', 'node.button_box'
            )
            row = self.draw_button(
                layout, 'node.button_sphere', 'node.button_tube'
            )
            if node.projection == 'BOX':
                row = layout.row(align=True)
                mytool = scene.blend_val_tool
                row.prop(mytool, "blend_val")

            row = layout.row(align=True)
            row.label(text="Extension:")

            row = layout.row(align=True)
            row.operator('node.button_repeat')

            row = self.draw_button(
                layout, 'node.button_extend', 'node.button_clip'
            )
        else:
            layout.label(text="(No Image Texture Selected)",
                         icon='GHOST_DISABLED')

    def draw_button(self, layout, arg1, arg2):
        result = layout.row(align=True)
        result.operator(arg1)
        result.operator(arg2)

        return result


# INTERPOLATIONS
class RN_OT__NodeButtonLinear(Operator):
    '''Set Image Texture interpolation to Linear'''
    bl_idname = 'node.button_linear'
    bl_label = 'Linear'

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
    '''Set Image Texture interpolation to Closest'''
    bl_idname = 'node.button_closest'
    bl_label = 'Closest'

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
    '''Set Image Texture interpolation to Cubic'''
    bl_idname = 'node.button_cubic'
    bl_label = 'Cubic'

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
    '''Set Image Texture interpolation to Smart'''
    bl_idname = 'node.button_smart'
    bl_label = 'Smart'

    def execute(self, context):
        nodes, links = get_nodes_links(context)
        for node in nodes:
            if node.select == True:
                if node.type == 'TEX_IMAGE':
                    node.interpolation = 'Smart'
                else:
                    print("Possible Error - One or more nodes are not Image Textures")
        return {'FINISHED'}


# PROJECTIONS
class RN_OT__NodeButtonFlat(Operator):
    '''Set Image Texture projection to Flat'''
    bl_idname = 'node.button_flat'
    bl_label = 'Flat'

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
    '''Set Image Texture projection to Box'''
    bl_idname = 'node.button_box'
    bl_label = 'Box'

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
    '''Set Image Texture projection to Sphere'''
    bl_idname = 'node.button_sphere'
    bl_label = 'Sphere'

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
    '''Set Image Texture projection to TTube'''
    bl_idname = 'node.button_tube'
    bl_label = 'Tube'

    def execute(self, context):
        nodes, links = get_nodes_links(context)
        for node in nodes:
            if node.select == True:
                if node.type == 'TEX_IMAGE':
                    node.projection = 'TUBE'
                else:
                    print("Possible Error - One or more nodes are not Image Textures")
        return {'FINISHED'}


# EXTENSIONS
class RN_OT__NodeButtonRepeat(Operator):
    '''Set Image Texture extension to Repeat'''
    bl_idname = 'node.button_repeat'
    bl_label = 'Repeat'

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
    '''Set Image Texture extension to Extend'''
    bl_idname = 'node.button_extend'
    bl_label = 'Extend'

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
    '''Set Image Texture extension to Clip'''
    bl_idname = 'node.button_clip'
    bl_label = 'Clip'

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
    BlendValProperty,
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
        bpy.types.Scene.blend_val_tool = bpy.props.PointerProperty(
            type=BlendValProperty)


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
        # del bpy.types.Scene.blend_val_tool


if __name__ == "__main__":
    register()


# To get all the image textures recursively in a node tree you can use :
# image_texture_nodes = []
# node_groups = [n for n in context.space_data.node_tree.nodes if n.type == "GROUP"]
# while node_groups:
#     node_group = node_groups.pop(0)
#     node_groups.extend([n for n in node_group.node_tree.nodes if n.type == "GROUP"])
#     image_texture_nodes.extend([n for n in node_group.node_tree.nodes if n.type == "TEX_IMAGE"])
# print(image_texture_nodes)
