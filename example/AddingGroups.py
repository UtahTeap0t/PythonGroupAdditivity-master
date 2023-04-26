from pgradd.GroupAdd.Library import GroupLibrary
import pgradd.ThermoChem
#lib = GroupLibrary.Load('GuSolventGA2017Aq')

lib = GroupLibrary.Load('Chikos1993')
#descriptors = lib.GetDescriptors('CCCCN')#this works!
#descriptors = lib.GetDescriptors('CCCC[N]')#This doesn't work
#descriptors = lib.GetDescriptors('CCCC(N)')#this works!
#descriptors = lib.GetDescriptors('CCCC([N])')#This doesn't work
#descriptors = lib.GetDescriptors('C(C)(CN)([H])([H])')#this works!
#descriptors = lib.GetDescriptors('C(C)(C(N))([H])([H])')#this works!
#descriptors = lib.GetDescriptors('CC1=CC=C(C=C1)N')
#descriptors = lib.GetDescriptors('CC1=CC=C(C=C1)[N]')
#descriptors = lib.GetDescriptors('CC1=CC=C(C=C1)(N)')
#descriptors = lib.GetDescriptors('CC1=CC=C(C=C1)([N])')
#descriptors = lib.GetDescriptors('[H]c1c([H])c(C([H])([H])[H])c([H])c([H])c1N([H])[H]')
#descriptors = lib.GetDescriptors('[H]c1c([H])c(C([H])([H])[H])c([H])c([H])c1[N]')
#descriptors = lib.GetDescriptors('FP(OC(C)C)')
#descriptors = lib.GetDescriptors('FP(=O)(OC(C)C)')
descriptors = lib.GetDescriptors('CCCS')
#descriptors = lib.GetDescriptors('CC(=C=C)C')

print(descriptors)
thermochem = lib.Estimate(descriptors,'thermochem')
print((thermochem.get_HoRT(298)))