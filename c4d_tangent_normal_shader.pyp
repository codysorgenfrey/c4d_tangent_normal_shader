import math
import c4d

PLUGIN_ID = 1060113


class c4d_inverted_z_world_normal_shader(c4d.plugins.ShaderData):
    
    def __init__(self):
        # If a Python exception occurs during the calculation of a pixel colorize this one in red for debugging purposes
        self.SetExceptionColor(c4d.Vector(1, 0, 0))
    
    def Output(self, sh, cd):
        """Called by Cinema 4D for each point of the visible surface of a shaded object to return the color.
        
        Important: No OS calls are allowed during this function. Doing so could cause a crash, since it can be called in a multi-processor context.
        Args:
            sh (c4d.BaseShader): The shader node connected with this instance.
            cd (c4d.modules.render.ChannelData): Channel data to use and/or modify.
        Returns:
            c4d.Vector: The color of the shaded from 0 = black to 1 = white
        """
        # If shader is computed in 3d space
        if cd.vd:
            myN = cd.vd.n;
            myN.z *= -1;
            return myN;

        # If shader is computed in 2d space, return black
        else:
            return c4d.Vector(0.0)


if __name__ == '__main__':
    # String resource, see c4d_symbols.h, have to be redefined in python
    IDS_PY_FRESNEL = 10000
    c4d.plugins.RegisterShaderPlugin(PLUGIN_ID, c4d.plugins.GeLoadString(IDS_PY_FRESNEL), 0, c4d_inverted_z_world_normal_shader, "", 0)