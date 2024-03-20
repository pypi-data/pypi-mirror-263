from fileformats.generic import File
from fileformats.medimage.nifti import Nifti1
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.auto.refit import Refit
import pytest


@pytest.mark.xfail
def test_refit_1():
    task = Refit()
    task.inputs.in_file = Nifti1.sample(seed=0)
    task.inputs.duporigin_file = File.sample(seed=5)
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_refit_2():
    task = Refit()
    task.inputs.in_file = Nifti1.sample(seed=0)
    task.inputs.deoblique = True
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_refit_3():
    task = Refit()
    task.inputs.in_file = Nifti1.sample(seed=0)
    task.inputs.atrfloat = ("IJK_TO_DICOM_REAL", "'1 0.2 0 0 -0.2 1 0 0 0 0 1 0'")
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)
