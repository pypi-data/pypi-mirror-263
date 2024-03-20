from fileformats.medimage.nifti import Nifti1
from fileformats.medimage_afni import OneD
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.auto.synthesize import Synthesize
import pytest


@pytest.mark.xfail
def test_synthesize_1():
    task = Synthesize()
    task.inputs.cbucket = Nifti1.sample(seed=0)
    task.inputs.matrix = OneD.sample(seed=1)
    task.inputs.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_synthesize_2():
    task = Synthesize()
    task.inputs.cbucket = Nifti1.sample(seed=0)
    task.inputs.matrix = OneD.sample(seed=1)
    task.inputs.select = ["baseline"]
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)
