from fileformats.generic import File
from fileformats.medimage.nifti import Nifti1
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.auto.outlier_count import OutlierCount
import pytest


@pytest.mark.xfail
def test_outliercount_1():
    task = OutlierCount()
    task.inputs.in_file = Nifti1.sample(seed=0)
    task.inputs.mask = File.sample(seed=1)
    task.inputs.qthr = 0.001
    task.inputs.autoclip = False
    task.inputs.automask = False
    task.inputs.fraction = False
    task.inputs.interval = False
    task.inputs.save_outliers = False
    task.inputs.outliers_file = File.sample(seed=8)
    task.inputs.legendre = False
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_outliercount_2():
    task = OutlierCount()
    task.inputs.in_file = Nifti1.sample(seed=0)
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)
