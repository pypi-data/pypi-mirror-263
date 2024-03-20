from fileformats.medimage.nifti import Nifti1
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.auto.t_norm import TNorm
import pytest


@pytest.mark.xfail
def test_tnorm_1():
    task = TNorm()
    task.inputs.in_file = Nifti1.sample(seed=0)
    task.inputs.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_tnorm_2():
    task = TNorm()
    task.inputs.in_file = Nifti1.sample(seed=0)
    task.inputs.out_file = "rm.errts.unit errts+tlrc"
    task.inputs.norm2 = True
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)
