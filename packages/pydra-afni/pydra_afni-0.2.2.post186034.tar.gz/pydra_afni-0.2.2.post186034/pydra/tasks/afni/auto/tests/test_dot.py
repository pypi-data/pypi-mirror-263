from fileformats.generic import File
from fileformats.medimage.nifti import Nifti1
from fileformats.text import TextFile
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.auto.dot import Dot
import pytest


@pytest.mark.xfail
def test_dot_1():
    task = Dot()
    task.inputs.in_files = [Nifti1.sample(seed=0)]
    task.inputs.mask = File.sample(seed=2)
    task.inputs.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_dot_2():
    task = Dot()
    task.inputs.in_files = [Nifti1.sample(seed=0)]
    task.inputs.out_file = "out.mask_ae_dice.txt"
    task.inputs.dodice = True
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)
