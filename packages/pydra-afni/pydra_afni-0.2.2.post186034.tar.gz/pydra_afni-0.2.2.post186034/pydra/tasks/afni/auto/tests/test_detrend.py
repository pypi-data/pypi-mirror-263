from fileformats.medimage.nifti import Nifti1
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.auto.detrend import Detrend
import pytest


@pytest.mark.xfail
def test_detrend_1():
    task = Detrend()
    task.inputs.in_file = Nifti1.sample(seed=0)
    task.inputs.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_detrend_2():
    task = Detrend()
    task.inputs.in_file = Nifti1.sample(seed=0)
    task.inputs.outputtype = "AFNI"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)
