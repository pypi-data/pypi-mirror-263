# PyUnits
# Physical units for scientific and engineering This is a simple implementation of a units framework for python, and can be expanded upon as desired. These conversions are implemented in an easy-to-read format, which may add additional computation time, in python, when used in operations that involve many computations.
# Use:
# from physicalunits import units
# C = units("SI")
# #assign units to a number - in this case 10 lbf of force:
# F = 10*C.LBF
# #report the number in units force:
# print( F/C.LBF )
# #report the number in units of Newtons:
# print ( F/C.N )
# #assign a mixed unit to a value in this case density in SI units:
# rho = 10 *C.KG/C.M**3
# report the unit is US customary units:
# #print ( rho / (C.SLUG/C.FT**3) )

class units():
    # the following classes reference NIST Guide to the SI, Appendix B.9
    class Celsius:
        def __rmul__(self,other):
            return other+273
        def __rtruediv__(self,other):
            return other-273
    class Fahrenheit:
        def __rmul__(self,other):
            return (other+459.67)/1.8
        def __rtruediv__(self,other):
            return other*1.8-459.67

    class __SI_Const:
        G0_M_SEC2       = 9.806_65
        C_M_SEC         = 299_792_458
        ATM_PA          = 101_325
        G_M3_KG_SEC2    = 6.674_30E-11
        
    class __US_2_SI:
        FT_2_M          = 3.048E-01
        SLUG_2_KG       = 1.459_390E+01
        LBF_2_N         = 4.448_222
        GAL_2_M3        = 3.785_412E-03
    
    # initialize the class and establish the base unit system
    def __init__(self,base_unit_sys="SI"):
        from math import pi
        match base_unit_sys:
            case "SI":
                # length - ref m
                self.M          = 1
                self.FT         = self.__US_2_SI.FT_2_M

                # mass - ref kg
                self.KG         = 1
                self.SLUG       = self.__US_2_SI.SLUG_2_KG

                # force - ref Newton
                self.N          = 1
                self.LBF        = self.__US_2_SI.LBF_2_N
                
                #volume - ref m3
                self.M3         = 1
                self.GAL        = self.__US_2_SI.GAL_2_M3

            case "US":
                # length - ref ft
                self.M          = 1/self.__US_2_SI.FT_2_M
                self.FT         = 1

                # mass - ref slug
                self.KG         = 1/self.__US_2_SI.SLUG_2_KG
                self.SLUG       = 1

                # force - ref lbf
                self.N          = 1/self.__US_2_SI.LBF_2_N
                self.LBF        = 1
                
                #volume - ref gal
                self.M3         = 1/self.__US_2_SI.GAL_2_M3
                self.GAL        = 1
            
            case "US-INCH":
                # length - ref inch
                self.M          = 12/self.__US_2_SI.FT_2_M
                self.FT         = 12

                # mass - ref slinch
                self.KG         = 1/self.__US_2_SI.SLUG_2_KG/12
                self.SLUG       = 1/12

                # force - ref lbf
                self.N          = 1/self.__US_2_SI.LBF_2_N
                self.LBF        = 1
                
                #volume - ref gal
                self.M3         = 1/self.__US_2_SI.GAL_2_M3
                self.GAL        = 1
            case _:
                raise Exception('error incorrect base unit name.\nUse "SI", "US", or "US-INCH"')
        
        # define units, which are common to all unit base systems
        # time - ref sec
        self.SEC        = 1
        self.MILISEC    = 1.0e-3
        self.MICROSEC   = 1.0e-6
        self.MIN        = 60
        self.HOUR       = 3600
        self.DAY        = 3600.*24
        self.YEAR       = 3600*24*365

        #periodic rate ref - rad/sec
        self.HZ         = 2.*pi
        self.DPS        = pi/180.
        self.RPM        = 2.*pi/60.
        
        # angles - ref radians
        self.RAD        = 1.
        self.DEG        = pi/180.
        self.ARCMIN     = pi/180./60.
        self.ARCSEC     = pi/180./3600.
        
        # temp - ref Kelvin
        self.K = 1
        self.R = 1/1.8
        self.C = self.Celsius()
        self.F = self.Fahrenheit()
        
        # establish physical constants
        # gravitational constant
        self.G          = self.__SI_Const.G_M3_KG_SEC2*self.M3/self.KG/self.SEC**2
        # earth surface gravity
        self.G0         = self.__SI_Const.G0_M_SEC2*self.M/self.SEC**2
        # standard atmosphere
        self.ATM        = self.__SI_Const.ATM_PA*self.N/self.M**2
        # speed of light in vacuum
        self.C0         = self.__SI_Const.C_M_SEC*self.M/self.SEC**2
        
        # Define Derived Unites
        # length
        self.MIL        = self.FT/12/1000
        self.IN         = self.FT/12
        self.YARD       = self.FT*3
        self.MILE       = self.FT*5280

        self.MM         = self.M*1.0E-03
        self.CM         = self.M*1.0E-02
        self.KM         = self.M*1.0E+03
        self.NM         = self.M*1852

        # mass
        self.SLINCH     = self.SLUG*12
        self.LBM        = self.LBF/self.G0
        self.OZ         = self.LBM/16

        self.GM         = self.KG*1.0E-03
                       
        # force - ref Newton
        self.TON        = self.LBF*2000
        self.KN         = self.N*1000

        # pressure - ref Pascal
        self.PSI        = self.LBF/self.IN**2
        self.KSI        = self.PSI*1.0E3
        self.MSI        = self.PSI*1.0E6

        self.PA         = self.N/self.M**2
        self.BAR        = self.PA

        # speed ref m/sec
        self.FPS        = self.FT/self.SEC
        self.FPM        = self.FT/self.MIN
        self.IPS        = self.IN/self.SEC
        self.MPH        = self.MILE/self.HOUR

        self.KPH        = self.KM/self.HOUR
        self.KNOT       = self.NM/self.HOUR

        # volume ref m3
        self.QT         = self.GAL/4
        self.CUP        = self.GAL/16
        self.FLOZ       = self.GAL/16/8
        self.TBSP       = self.GAL/16/16
        self.TSP        = self.GAL/16/48

        self.L          = self.M3*1.0E-03
        self.ML         = self.M3*1.0E-06
        self.CC         = self.M3*1.0E-06