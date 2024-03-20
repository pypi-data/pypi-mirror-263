from fileformats.medimage.nifti import Nifti1
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.auto.t_cat import TCat
import pytest


@pytest.mark.xfail
def test_tcat_1():
    task = TCat()
    task.inputs.in_files = [Nifti1.sample(seed=0)]
    task.inputs.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_tcat_2():
    task = TCat()
    task.inputs.in_files = [Nifti1.sample(seed=0)]
    task.inputs.out_file = "functional_tcat.nii"
    task.inputs.rlt = "+"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)
