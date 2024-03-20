from fileformats.medimage.nifti import Nifti1
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.auto.zcat import Zcat
import pytest


@pytest.mark.xfail
def test_zcat_1():
    task = Zcat()
    task.inputs.in_files = [Nifti1.sample(seed=0)]
    task.inputs.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_zcat_2():
    task = Zcat()
    task.inputs.in_files = [Nifti1.sample(seed=0)]
    task.inputs.out_file = "cat_functional.nii"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)
