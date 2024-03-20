from fileformats.generic import File
from fileformats.medimage.nifti import Nifti1
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.engine.specs import MultiInputObj
from pydra.tasks.afni.auto.local_bistat import LocalBistat
import pytest


@pytest.mark.xfail
def test_localbistat_1():
    task = LocalBistat()
    task.inputs.in_file1 = Nifti1.sample(seed=0)
    task.inputs.in_file2 = Nifti1.sample(seed=1)
    task.inputs.mask_file = File.sample(seed=4)
    task.inputs.weight_file = File.sample(seed=6)
    task.inputs.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_localbistat_2():
    task = LocalBistat()
    task.inputs.in_file1 = Nifti1.sample(seed=0)
    task.inputs.in_file2 = Nifti1.sample(seed=1)
    task.inputs.neighborhood = ("SPHERE", 1.2)
    task.inputs.stat = "pearson"
    task.inputs.outputtype = "NIFTI"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)
