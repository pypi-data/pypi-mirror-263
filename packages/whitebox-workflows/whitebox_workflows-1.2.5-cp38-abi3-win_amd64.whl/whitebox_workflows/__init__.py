from typing import Tuple
from .whitebox_workflows import *
from .scripts.horton_ratios import horton_ratios
from whitebox_workflows import Raster

__doc__ = whitebox_workflows.__doc__
if hasattr(whitebox_workflows, "__all__"):
    __all__ = whitebox_workflows.__all__

class WbEnvironment(WbEnvironmentBase):
    """The WbEnvironment class can be used to configure WbW settings (e.g. the working
directory, number of processors used, and verbose mode). It is also used to call
the various tool functions, which appear as methods of this class, and to read/write
spatial data."""
    def __init__(self, user_id: str = None):
        """Initializes a new WbEnvironment object with an optional user_id, i.e. a floating
license ID string used in WbW-Pro licenses.
        """
        # WbEnvironmentBase(user_id)

    def available_functions(self) -> None:
        """This function will list all of the available functions associated with a
WbEnvironment (wbe). The functions that are accessible will depend on the 
license level (WbW or WbWPro).
        """

        # Are we running a pro license?
        pro_license = self.license_type == LicenseType.WbWPro

        # Get all the non-dunder methods of WbEnvironment
        method_list = [func for func in dir(WbEnvironment) if callable(getattr(WbEnvironment, func)) and not func.startswith("__")]

        print(f"Available Methods ({self.license_type}):")

        j = 0
        s = ''
        for i in range(len(method_list)):
            val = method_list[i]
            val_len = len(f"{j}. {val}")
            is_pro_func = whitebox_workflows.is_wbw_pro_function(val)
            
            added = True
            if not is_pro_func and j % 2 == 0:
                s += f"{j+1}. {val}{' '* (50 - val_len)}"
                j += 1
            elif not is_pro_func and j % 2 == 1:
                s += f"{j+1}. {val}"
                j += 1
            elif (is_pro_func and pro_license) and j % 2 == 0:
                s += f"{j+1}. {val}{' '* (50 - val_len)}"
                j += 1
            elif (is_pro_func and pro_license) and j % 2 == 1:
                s += f"{j+1}. {val}"
                j += 1
            else:
                added = False
                

            if added and (j % 2 == 0 or i == len(method_list)-1):
                print(s)
                s = ''


    def horton_ratios(self, dem: Raster, streams_raster: Raster) -> Tuple[float, float, float, float]:
        '''This function can be used to calculate Horton's so-called laws of drainage network composition for a
input stream network. The user must specify an input DEM (which has been suitably hydrologically pre-processed
to remove any topographic depressions) and a raster stream network. The function will output a 4-element 
tuple containing the bifurcation ratio (Rb), the length ratio (Rl), the area ratio (Ra), and the slope ratio
(Rs). These indices are related to drainage network geometry and are used in some geomorphological analysis.
The calculation of the ratios is based on the method described by Knighton (1998) Fluvial Forms and Processes: 
A New Perspective.

# Code Example

```python
from whitebox_workflows import WbEnvironment

# Set up the WbW environment
wbe = WbEnvironment()
wbe.verbose = True
wbe.working_directory = '/path/to/data'

# Read the test inputs
dem = wbe.read_raster('DEM.tif')
streams = wbe.read_raster('streams.tif')

# Calculate the Horton ratios
(bifurcation_ratio, length_ratio, area_ratio, slope_ratio) = wbe.horton_ratios(dem, streams)

# Outputs
print(f"Bifurcation ratio (Rb): {bifurcation_ratio:.3f}")
print(f"Length ratio (Rl): {length_ratio:.3f}")
print(f"Area ratio (Ra): {area_ratio:.3f}")
print(f"Slope ratio (Rs): {slope_ratio:.3f}")
```

# See Also
<a href="tool_help_wbwpro.md#horton_stream_order">horton_stream_order</a>

# Function Signature
```python
def horton_ratios(self, dem: Raster, streams_raster: Raster) -> Tuple[float, float, float, float]: ...
```
'''
        return horton_ratios(self, dem, streams_raster)


