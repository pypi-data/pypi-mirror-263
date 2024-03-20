from fileformats.generic import File
from fileformats.medimage.nifti import Nifti1
from fileformats.medimage_afni import OneD
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.auto.remlfit import Remlfit
import pytest


@pytest.mark.xfail
def test_remlfit_1():
    task = Remlfit()
    task.inputs.in_files = [Nifti1.sample(seed=0)]
    task.inputs.matrix = OneD.sample(seed=1)
    task.inputs.matim = File.sample(seed=3)
    task.inputs.mask = File.sample(seed=4)
    task.inputs.automask = False
    task.inputs.STATmask = File.sample(seed=6)
    task.inputs.addbase = [File.sample(seed=7)]
    task.inputs.slibase = [File.sample(seed=8)]
    task.inputs.slibase_sm = [File.sample(seed=9)]
    task.inputs.dsort = File.sample(seed=12)
    task.inputs.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_remlfit_2():
    task = Remlfit()
    task.inputs.in_files = [Nifti1.sample(seed=0)]
    task.inputs.matrix = OneD.sample(seed=1)
    task.inputs.gltsym = [
        ("SYM: +Lab1 -Lab2", "TestSYM"),
        ("timeseries.txt", "TestFile"),
    ]
    task.inputs.out_file = "output.nii"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)
