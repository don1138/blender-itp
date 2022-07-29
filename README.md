# Blender ITP (Image Texture Properties)

**Set Image Texture Properties on Multiple Nodes**

![Blender ITP](https://github.com/don1138/blender-itp/blob/main/imx/blender-itp.jpg)

## Installation

Download the latest ZIP from **Releases**, or `node_image_texture_properties.py` from repository, and install addon.

## Usage

This addon creates a panel named **Image Texture Properties** under ``Shader Editor > Sidebar > Node``.

Select one or more Image Textures and the panel looks like this:

![Blender ITP Active](https://github.com/don1138/blender-itp/blob/main/imx/itp-panel.png)

If `projection` is set to `BOX`, a Blend Value field appears:

![Blender ITP Active Box Blend](https://github.com/don1138/blender-itp/blob/main/imx/itp-panel-box-blend.png)

If no Image Texture is selected, the panel shows an empty state:

![Blender ITP Null](https://github.com/don1138/blender-itp/blob/main/imx/itp-panel-null.png)

## Backstory

I was working on a PBR with six image textures, and had to change the `Projection` to `BOX` six times. *(Because it had slipped my mind that I could simply hold the Control key to copy changes across all selected nodes. 🤔)*

The existing `Properties` panel will set things like `Color Mode` for all selected images, but doesn't include the full set of properties listed on the node itself.

Deciding that such tyranny will not stand on my watch, I made a quick extension to allow me to set the outstanding properties of all selected `Image Textures` with one click.

Because that's what heroes do. *(Instead of simply holding the Control key to copy changes across all selected nodes. 🙄)*

<br><br>

<p align="center">
  <img alt="GitHub latest commit" src="https://img.shields.io/github/last-commit/don1138/blender-itp">
  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/don1138/blender-itp">
  <img alt="Github all releases" src="https://img.shields.io/github/downloads/don1138/blender-itp/total.svg"><br>
  <img src="https://repobeats.axiom.co/api/embed/c0e3e1855d0f7003c53943d3efcfa0fc8f9d853f.svg" alt="Repobeats analytics image">
</p>
