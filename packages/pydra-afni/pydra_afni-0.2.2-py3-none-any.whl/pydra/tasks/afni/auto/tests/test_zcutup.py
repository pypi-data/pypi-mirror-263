from fileformats.medimage.nifti import Nifti1
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.auto.z_cut_up import ZCutUp
import pytest


@pytest.mark.xfail
def test_zcutup_1():
    task = ZCutUp()
    task.inputs.in_file = Nifti1.sample(seed=0)
    task.inputs.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_zcutup_2():
    task = ZCutUp()
    task.inputs.in_file = Nifti1.sample(seed=0)
    task.inputs.out_file = "functional_zcutup.nii"
    task.inputs.keep = "0 10"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)
