from fileformats.generic import File
from fileformats.medimage.nifti import Nifti1
from fileformats.medimage_afni import OneD
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.auto.deconvolve import Deconvolve
import pytest


@pytest.mark.xfail
def test_deconvolve_1():
    task = Deconvolve()
    task.inputs.in_files = [Nifti1.sample(seed=0)]
    task.inputs.input1D = File.sample(seed=5)
    task.inputs.mask = File.sample(seed=19)
    task.inputs.STATmask = File.sample(seed=21)
    task.inputs.censor = File.sample(seed=22)
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_deconvolve_2():
    task = Deconvolve()
    task.inputs.in_files = [Nifti1.sample(seed=0)]
    task.inputs.x1D = "output.1D"
    task.inputs.out_file = "output.nii"
    task.inputs.stim_times = stim_times
    task.inputs.stim_label = [(1, "Houses")]
    task.inputs.gltsym = ["SYM: +Houses"]
    task.inputs.glt_label = [(1, "Houses")]
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)
