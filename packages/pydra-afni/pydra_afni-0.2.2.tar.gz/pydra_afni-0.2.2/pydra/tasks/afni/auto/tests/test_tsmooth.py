from fileformats.generic import File
from fileformats.medimage.nifti import Nifti1
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.auto.t_smooth import TSmooth
import pytest


@pytest.mark.xfail
def test_tsmooth_1():
    task = TSmooth()
    task.inputs.in_file = Nifti1.sample(seed=0)
    task.inputs.custom = File.sample(seed=9)
    task.inputs.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_tsmooth_2():
    task = TSmooth()
    task.inputs.in_file = Nifti1.sample(seed=0)
    task.inputs.adaptive = 5
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)
