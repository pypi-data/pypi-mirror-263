from fileformats.generic import File
from fileformats.medimage.nifti import Nifti1
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.auto.re_ho import ReHo
import pytest


@pytest.mark.xfail
def test_reho_1():
    task = ReHo()
    task.inputs.in_file = Nifti1.sample(seed=0)
    task.inputs.mask_file = File.sample(seed=3)
    task.inputs.label_set = File.sample(seed=7)
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_reho_2():
    task = ReHo()
    task.inputs.in_file = Nifti1.sample(seed=0)
    task.inputs.out_file = "reho.nii.gz"
    task.inputs.neighborhood = "vertices"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)
