from fileformats.medimage.nifti import Nifti1
from fileformats.medimage.nifti import NiftiGz
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.auto.brick_stat import BrickStat
import pytest


@pytest.mark.xfail
def test_brickstat_1():
    task = BrickStat()
    task.inputs.in_file = Nifti1.sample(seed=0)
    task.inputs.mask = NiftiGz.sample(seed=1)
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_brickstat_2():
    task = BrickStat()
    task.inputs.in_file = Nifti1.sample(seed=0)
    task.inputs.mask = NiftiGz.sample(seed=1)
    task.inputs.min = True
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)
