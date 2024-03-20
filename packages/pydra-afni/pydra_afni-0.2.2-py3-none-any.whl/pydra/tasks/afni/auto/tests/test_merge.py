from fileformats.medimage.nifti import Nifti1
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.auto.merge import Merge
import pytest


@pytest.mark.xfail
def test_merge_1():
    task = Merge()
    task.inputs.in_files = [Nifti1.sample(seed=0)]
    task.inputs.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_merge_2():
    task = Merge()
    task.inputs.in_files = [Nifti1.sample(seed=0)]
    task.inputs.out_file = "e7.nii"
    task.inputs.doall = True
    task.inputs.blurfwhm = 4
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)
