from fileformats.generic import File
from fileformats.medimage.nifti import Nifti1
from fileformats.medimage_afni import OneD
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.auto.retroicor import Retroicor
import pytest


@pytest.mark.xfail
def test_retroicor_1():
    task = Retroicor()
    task.inputs.in_file = Nifti1.sample(seed=0)
    task.inputs.card = OneD.sample(seed=2)
    task.inputs.resp = OneD.sample(seed=3)
    task.inputs.cardphase = File.sample(seed=6)
    task.inputs.respphase = File.sample(seed=7)
    task.inputs.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_retroicor_2():
    task = Retroicor()
    task.inputs.in_file = Nifti1.sample(seed=0)
    task.inputs.card = OneD.sample(seed=2)
    task.inputs.resp = OneD.sample(seed=3)
    task.inputs.outputtype = "NIFTI"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)
