import bpy

def update_all_render_settings(x_res=1920, y_res=1080, scale=100, samples=2**4):
    for scene in bpy.data.scenes:
        scene.render.resolution_x = x_res
        scene.render.resolution_y = y_res
        scene.render.resolution_percentage = scale
        scene.eevee.taa_render_samples = samples
        
update_all_render_settings(1920,1080, 100, 2**4)
