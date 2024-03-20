from fileformats.generic import File
from fileformats.medimage.nifti import Nifti1
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.auto.gcor import GCOR
import pytest


@pytest.mark.xfail
def test_gcor_1():
    task = GCOR()
    task.inputs.in_file = Nifti1.sample(seed=0)
    task.inputs.mask = File.sample(seed=1)
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_gcor_2():
    task = GCOR()
    task.inputs.in_file = Nifti1.sample(seed=0)
    task.inputs.nfirst = 4
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)
