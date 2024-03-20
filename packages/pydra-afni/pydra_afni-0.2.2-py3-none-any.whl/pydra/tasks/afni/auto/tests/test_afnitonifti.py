from fileformats.medimage_afni import ThreeD
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.auto.afn_ito_nifti import AFNItoNIFTI
import pytest


@pytest.mark.xfail
def test_afnitonifti_1():
    task = AFNItoNIFTI()
    task.inputs.in_file = ThreeD.sample(seed=0)
    task.inputs.pure = False
    task.inputs.denote = False
    task.inputs.oldid = False
    task.inputs.newid = False
    task.inputs.num_threads = 1
    task.inputs.outputtype = "NIFTI"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_afnitonifti_2():
    task = AFNItoNIFTI()
    task.inputs.in_file = ThreeD.sample(seed=0)
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)
