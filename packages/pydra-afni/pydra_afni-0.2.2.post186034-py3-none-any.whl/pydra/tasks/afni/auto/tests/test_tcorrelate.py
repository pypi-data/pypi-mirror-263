from fileformats.medimage.nifti import Nifti1
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.auto.t_correlate import TCorrelate
import pytest


@pytest.mark.xfail
def test_tcorrelate_1():
    task = TCorrelate()
    task.inputs.xset = Nifti1.sample(seed=0)
    task.inputs.yset = Nifti1.sample(seed=1)
    task.inputs.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_tcorrelate_2():
    task = TCorrelate()
    task.inputs.xset = Nifti1.sample(seed=0)
    task.inputs.yset = Nifti1.sample(seed=1)
    task.inputs.out_file = "functional_tcorrelate.nii.gz"
    task.inputs.pearson = True
    task.inputs.polort = -1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)
