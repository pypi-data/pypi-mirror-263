from fileformats.medimage.nifti import Nifti1
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.auto.mask_tool import MaskTool
import pytest


@pytest.mark.xfail
def test_masktool_1():
    task = MaskTool()
    task.inputs.in_file = [Nifti1.sample(seed=0)]
    task.inputs.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_masktool_2():
    task = MaskTool()
    task.inputs.in_file = [Nifti1.sample(seed=0)]
    task.inputs.outputtype = "NIFTI"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)
