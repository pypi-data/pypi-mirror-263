from PyConSolv.misc.inputparser import XYZ
from PyConSolv.misc.fragmenting import Fragmentor
import os

if __name__ == '__main__':
    # xyz = XYZ(db_file=os.path.split(__file__)[0] + '/../src/PyConSolv/db/atom-radius.txt',
    #           db_metal_file=os.path.split(__file__)[0] + '/../src/PyConSolv/db/metal-radius.txt')
    # xyz.readXYZ('/home/rat/PYCONSOLV_DATA/issue_47/input.xyz')
    # xyz.prepareInput('/home/rat/PYCONSOLV_DATA/issue_47/input.xyz')
    # xyz.writePDBFiles('/home/rat/PYCONSOLV_DATA/issue_47/pdbs/')
    frag = Fragmentor(path='/home/rat/PYCONSOLV_DATA/issue_47b/input.xyz', radius = 2)
    frag.run()

