from fileformats.generic import File
from fileformats.medimage.nifti import Nifti1
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.auto.undump import Undump
import pytest


@pytest.mark.xfail
def test_undump_1():
    task = Undump()
    task.inputs.in_file = Nifti1.sample(seed=0)
    task.inputs.mask_file = File.sample(seed=2)
    task.inputs.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_undump_2():
    task = Undump()
    task.inputs.in_file = Nifti1.sample(seed=0)
    task.inputs.out_file = "structural_undumped.nii"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)
