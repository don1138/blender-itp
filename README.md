# Blender ITP (Image Texture Properties)

**Set Image Texture Properties on Multiple Nodes**

## Installation

Download the latest ZIP from **Releases**, or `node_image_texture_properties.py` from repository, and install addon.

## Usage

This addon creates a panel named **Image Texture Properties** under ``Shader Editor > Sidebar > Node``.

## Backstory

I was working on a PBR with six image textures, and had to change the `Projection` to `BOX` six time.

The existing `Properties` panel will set things like `Color Mode` for all selected images, but doesn't include the full set of properties listed on the node itself.

Deciding that such tyranny will not stand on my watch, I made a quick extension to allow me to set the outstanding properties of all selected `Image Textures` with one click.

Because that's what heroes do.
