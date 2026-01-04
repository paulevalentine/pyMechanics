import sympy as sp
from IPython.display import display, Markdown
"""
A set of functions for general use in structural engineering
"""

def ss_max_bending_moment(udl: float, span: float)->float:
    display(Markdown("Calculate the simply supported max moment from the UDL (kNm):"))
    m, w, l = sp.symbols('m, w, l')
    m_eq = sp.Eq(m, w * l**2 / 8)
    m_val = m_eq.subs({w: udl, l:span}).evalf(3)
    display(m_eq, m_val)
    return m_val.rhs

def ss_max_shear(udl: float, span: float)->float:
    display(Markdown("Calculate the simply supported max shear from the UDL (kN):"))
    v, w, l = sp.symbols('v, w, l')
    v_eq = sp.Eq(v, w * l / 2)
    v_val = v_eq.subs({w: udl, l:span}).evalf(3)
    display(v_eq, v_val)
    return v_val.rhs

def I_rectangle(breadth: float, height: float)->float:
    display(Markdown("Calculate the moment of area of a rectangle (mm4)"))
    I, b, h = sp.symbols('I, b, h')
    I_eq = sp.Eq(I, b*h**3/12)
    I_val = I_eq.subs({b: breadth, h: height}).evalf(3)
    display(I_eq, I_val)
    return I_val.rhs

def Z_rectangle(breadth: float, height: float)->float:
    display(Markdown("Calculate the section modulus of a rectangle (mm3)"))
    Z, b, h = sp.symbols('Z, b, h')
    Z_eq = sp.Eq(Z, b*h**2/6)
    Z_val = Z_eq.subs({b: breadth, h: height}).evalf(3)
    display(Z_eq, Z_val)
    return Z_val.rhs

def A_rectangle(breadth: float, height: float)->float:
    display(Markdown("Calculate the area of a rectangle (mm2)"))
    A, b, h = sp.symbols('A, b, h')
    A_eq = sp.Eq(A, b*h)
    A_val = A_eq.subs({b: breadth, h: height}).evalf(3)
    display(A_eq, A_val)
    return A_val.rhs

def elastic_bending_stress(moment: float, load: float, area: float, secton_modulus: float)->tuple:
    display(Markdown("Calculate the max elastic bending strees (MPa)"))
    smax, smin, m,w,a,z = sp.symbols("sigma_max, sigma_min, M, W, A, Z")
    smax_eq = sp.Eq(smax, w/a + m/z)
    smin_eq = sp.Eq(smin, w/a - m/z)
    smax_val = smax_eq.subs({w:load, m:moment, a:area, z:secton_modulus})
    smin_val = smin_eq.subs({w:load, m:moment, a:area, z:secton_modulus})
    display(smax_eq, smax_val, smin_eq, smin_val)
    return smax_val.rhs, smin_val.rhs


def ss_max_deflection(w: float, l: float, iSec: float, aSec: float, Emod: float, Gmod: float)->float:
    """
    Function to calculate the bending and shear deflection of a simply supported beam
    under a UDL
    :param w: load per metre in kN/m
    :param l: span in mm
    :param iSec: section moment of inertia in mm^4
    :param aSec: section area in mm^2
    :param Emod: modulus of elasticity in MPa
    :param Gmod: modulus of rigidity in MPa
    :return: deflection in mm
    """
    display(Markdown("Calculate the max bending deflection (mm):"))
    dm, load, span, i, a, Em, Gm = sp.symbols("delta_m, w, l, I, A, E_m, G_m")
    dm_eq = sp.Eq(dm, (5 * load * span**4)/(384 * Em * i))
    dm_val = dm_eq.subs({load:w, span:l, i:iSec, a:aSec, Em:Emod, Gm:Gmod}).evalf(3)
    display(dm_eq, dm_val)

    display(Markdown("Calculate the max shear deflection (mm):"))
    dv = sp.symbols("delta_v")
    dv_eq = sp.Eq(dv, (1.2 * load * span**2)/(8 * Gm * a))
    dv_val = dv_eq.subs({load:w, span:l, a:aSec, Gm:Gmod}).evalf(3)
    display(dv_eq, dv_val)

    display(Markdown("Calculate the total deflection (mm):"))
    dt = sp.symbols("delta_t")
    dt_eq = sp.Eq(dt, dm + dv)
    dt_val = dt_eq.subs({dm:dm_val.rhs, dv:dv_val.rhs}).evalf(3)
    display(dt_eq, dt_val)

    return dt_val.rhs

