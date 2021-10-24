import bpy

def update_all_render_settings(x, y, p, s):
    for scene in bpy.data.scenes:
        scene.render.resolution_x = x
        scene.render.resolution_y = y
        scene.render.resolution_percentage = p
        scene.eevee.taa_render_samples = s
        
update_all_render_settings(2160,2160, 25, 1)
