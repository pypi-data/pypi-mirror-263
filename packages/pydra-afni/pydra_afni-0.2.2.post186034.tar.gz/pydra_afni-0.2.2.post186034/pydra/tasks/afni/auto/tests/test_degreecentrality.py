from fileformats.generic import File
from fileformats.medimage.nifti import Nifti1
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.auto.degree_centrality import DegreeCentrality
import pytest


@pytest.mark.xfail
def test_degreecentrality_1():
    task = DegreeCentrality()
    task.inputs.in_file = Nifti1.sample(seed=0)
    task.inputs.mask = Nifti1.sample(seed=3)
    task.inputs.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_degreecentrality_2():
    task = DegreeCentrality()
    task.inputs.in_file = Nifti1.sample(seed=0)
    task.inputs.sparsity = 1  # keep the top one percent of connections
    task.inputs.mask = Nifti1.sample(seed=3)
    task.inputs.out_file = "out.nii"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)
