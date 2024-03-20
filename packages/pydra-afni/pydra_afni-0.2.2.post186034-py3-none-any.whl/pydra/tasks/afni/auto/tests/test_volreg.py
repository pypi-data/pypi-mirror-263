from fileformats.medimage.nifti import Nifti1
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.auto.volreg import Volreg
import pytest


@pytest.mark.xfail
def test_volreg_1():
    task = Volreg()
    task.inputs.in_file = Nifti1.sample(seed=0)
    task.inputs.basefile = Nifti1.sample(seed=3)
    task.inputs.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_volreg_2():
    task = Volreg()
    task.inputs.in_file = Nifti1.sample(seed=0)
    task.inputs.zpad = 4
    task.inputs.outputtype = "NIFTI"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_volreg_3():
    task = Volreg()
    task.inputs.in_file = Nifti1.sample(seed=0)
    task.inputs.out_file = "rm.epi.volreg.r1"
    task.inputs.basefile = Nifti1.sample(seed=3)
    task.inputs.zpad = 1
    task.inputs.oned_file = "dfile.r1.1D"
    task.inputs.verbose = True
    task.inputs.oned_matrix_save = "mat.r1.tshift+orig.1D"
    task.inputs.interp = "cubic"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)
