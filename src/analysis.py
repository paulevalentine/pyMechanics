# standard analysis calculations

class beam():
    def __init__(self, span):
        self.span = span

    def ssUdlForces(self,w):
        m = w * self.span**2 / 8
        v = w * self.span / 2
        print(f"The maximum bending moment = {m:.2f} kNm")
        print(f"The maximum shear = {v:.2f} kN")
        return m,v

    def ssUdlDeflection(self, w, iSec, aSec, Emod, Gmod):
        dm = (5*w*(self.span*10**3)**4)/(384*Emod*iSec)
        dv = 1.2 * w * (self.span*10**3)**2/(8*Gmod*aSec)
        dt = dm + dv
        print(f"Beam deflection = {dt:.2f} mm")
        return dt

