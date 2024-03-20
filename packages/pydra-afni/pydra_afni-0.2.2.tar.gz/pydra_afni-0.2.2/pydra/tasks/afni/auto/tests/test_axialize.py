from fileformats.medimage.nifti import Nifti1
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.auto.axialize import Axialize
import pytest


@pytest.mark.xfail
def test_axialize_1():
    task = Axialize()
    task.inputs.in_file = Nifti1.sample(seed=0)
    task.inputs.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_axialize_2():
    task = Axialize()
    task.inputs.in_file = Nifti1.sample(seed=0)
    task.inputs.out_file = "axialized.nii"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)
