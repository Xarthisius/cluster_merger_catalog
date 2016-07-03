from collections import OrderedDict
from sim_defs import Simulation
    
visc_info = {"name": "viscosity",
             "cadence": 0.05,
             "filespec": "virgo_%s.%04d",
             "set_name": "The Effect of Anisotropic Viscosity on Cold Fronts in Galaxy Clusters (ZuHone et al. 2015)",
             "set_journal": "ZuHone, J. A., Kunz, M. W., Markevitch, M., Stone, J. M., & Biffi, V. 2015, ApJ, 798, 90",
             "ads_link": "http://adsabs.harvard.edu/abs/2015ApJ...798...90Z",
             "box_size": 4.0,
             "cell_size": 0.977,
             "sim_type": "SMR",
             "code": "Athena",
             "primary_mass": "TBD"}

fields = {}
fields["slice"] = ["dens","temp","bmag","velx","vely"]
fields["proj"] = ["xray","temp","szy","szk"]
fields["SZ"] = []
pngs = {}
pngs["slice"] = ["dens","temp","bmag"]
pngs["proj"] = ["xray","temp","dens","szy"]
pngs["cxo_evt"] = ["counts"]
pngs["SZ"] = []

filenos = [0, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36,
           38, 40, 42, 44, 46, 48, 50, 52, 54]
           
visc_dict = OrderedDict()
visc_dict["novisc"] = Simulation(":math:`\\beta` = 1000, inviscid",
                                 filenos, fields, pngs,
                                 ["x", "y", "z"])
