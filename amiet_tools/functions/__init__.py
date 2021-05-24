"""
@Author: Fabio Casagrande Hirono
================================
Models:
-------
    xxx
    Available functions:
    ---------------------
        >>> xxx
        >>> xxx
        >>> xxx
        >>> xxx
    For further information, check the function specific documentation.
"""

from .discretizers import create_airf_mesh, chord_sampling
from .loaders import loadTestSetup, loadAirfoilGeom
from .DARP2016_MicArray import DARP2016_MicArray, DARP2016_Acoular_XML
from .wrappers import calc_airfoil_Sqq, calc_radiated_Spp
from .fresnel import fr_int, fr_int_cc, fr_integrand_im, fr_integrand_re
from .shear_layer import r, r_bar, _sigma, t_convect, t_sound, t_total, \
    constr_xl, constr_yl, ShearLayer_X, ShearLayer_matrix, ShearLayer_Corr
from .sound_propagation import dipole_shear, dipole3D
from .flat_plate_response import delta_p, g_LE, g_LE_sub, g_LE_super, L_LE, L_LE_sub, L_LE_super
from .hydronamics import ky_att, ky_vector
from .turbulent_velocity import Phi_2D
from .others import read_ffarray_lvm, rect_grid
__all__ = [
    # Functions
    'create_airf_mesh',
    'chord_sampling',
    'loadTestSetup',
    'loadAirfoilGeom',
    'DARP2016_MicArray',
    'DARP2016_Acoular_XML',
    'calc_airfoil_Sqq',
    'calc_radiated_Spp',
    'fr_int', 'fr_int_cc',
    'fr_integrand_im',
    'fr_integrand_re',
    'r', 'r_bar', '_sigma',
    't_convect', 't_sound',
    't_total', 'constr_xl',
    'constr_yl', 'ShearLayer_X',
    'ShearLayer_matrix',
    'ShearLayer_Corr',
    'dipole_shear', 'dipole3D',
    'delta_p', 'g_LE',
    'g_LE_sub', 'g_LE_super',
    'L_LE', 'L_LE_sub',
    'L_LE_super', 'ky_vector',
    'ky_att', 'Phi_2D',
    'rect_grid',
    'read_ffarray_lvm']
