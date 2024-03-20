from fileformats.medimage.nifti import Nifti1
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.auto.means import Means
import pytest


@pytest.mark.xfail
def test_means_1():
    task = Means()
    task.inputs.in_file_a = Nifti1.sample(seed=0)
    task.inputs.in_file_b = Nifti1.sample(seed=1)
    task.inputs.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_means_2():
    task = Means()
    task.inputs.in_file_a = Nifti1.sample(seed=0)
    task.inputs.in_file_b = Nifti1.sample(seed=1)
    task.inputs.out_file = "output.nii"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_means_3():
    task = Means()
    task.inputs.in_file_a = Nifti1.sample(seed=0)
    task.inputs.datum = "short"
    task.inputs.out_file = "output.nii"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)
