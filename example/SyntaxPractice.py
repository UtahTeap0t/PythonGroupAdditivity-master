from pgradd.GroupAdd.Library import GroupLibrary
import pgradd.ThermoChem
liblist = ["Chikos1993", "BensonGA"]
#          ,"XieGA2022" ,"SalciccioliGA2012","GRWSurface2018","GRWAqueous2018","GuSolventGA2017Vac","GuSolventGA2017Aq"]
#chemlist = ["CC(C)(C)(C)","CCC", "CCO"]
#chemlist = [ "CC1=CC=C(C=C1)O"]
#,"CC1=CC=C(C=C1)O"]
chemlist = ["CC(=C=C)C", "CC(CI)I","CC1=CC=C(C=C1)O","C(C)OP(=O)(O)O ", "FP(=O)(OC(C)C)C", "FP(=O)(OC(C)C)","CCC(=O)C(C1CCC(CC1)CCc2ccccc2)c3ccccc3", "CCCS"]
#"CC(=C=C)C",, "CCS"
#lib = GroupLibrary.Load('GuSolventGA2017Aq')
#lib = GroupLibrary.Load('GuSolventGA2017Vac')
#lib = GroupLibrary.Load('GRWAqueous2018')
#lib = GroupLibrary.Load('GRWSurface2018')
#lib = GroupLibrary.Load('SalciccioliGA2012')
#lib = GroupLibrary.Load('XieGA2022')
#lib = GroupLibrary.Load('BensonGA')
current = 0
while current <len(liblist):
    lib = GroupLibrary.Load(liblist[current])
    chem = 0
    while chem < len(chemlist):
        descriptors = lib.GetDescriptors(chemlist[chem])
        print(descriptors)
        thermochem = lib.Estimate(descriptors,'thermochem')
        print("Enthalpy 298.15K: ",(thermochem.get_HoRT(298.15)))
        print("Enthalpy 300K: ",(thermochem.get_HoRT(300)))
        print("Heat Capacity 298.15K: ",(thermochem.get_Cp(298.15,'J/mol/K')))
        chem += 1
    current += 1