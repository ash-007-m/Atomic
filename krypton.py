import sys
from pfac import fac
import numpy as np


use_openmp = False
if len(sys.argv) == 2 and sys.argv[1] == 'openmp':
    use_openmp = True

if use_openmp:
    # enable openmp with 2 cores
    fac.InitializeMPI(2)

fac.SetAtom('Kr')

fac.Config('1s2 2s2 2p6 3s',group='gr_state')
fac.Config('1s2 2s2 2p6 3[p-]',group='ex_state')

fac.ListConfig()
fac.ConfigEnergy(0)
fac.OptimizeRadial(['gr_state'])
fac.ConfigEnergy(1)
fac.Structure('ne.lev.b')
fac.MemENTable('ne.lev.b')
fac.PrintTable('ne.lev.b', 'ne.lev', 1)
e_low=1.69
e_high=5
n_points=1000
e_log = np.logspace(e_low,e_high,n_points)
e_ran= list(e_log)

low_lev=0
up_lev=1
fac.CETable('keb.ce',['gr_state'],['ex_state'])
print("done CE")
fac.CECross('keb.ce','ce_cross11.out',low_lev,up_lev,e_ran,0)



if use_openmp:
    fac.FinalizeMPI()


