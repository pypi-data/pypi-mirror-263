from fileformats.medimage.nifti import Nifti1
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.auto.edge_3 import Edge3
import pytest


@pytest.mark.xfail
def test_edge3_1():
    task = Edge3()
    task.inputs.in_file = Nifti1.sample(seed=0)
    task.inputs.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_edge3_2():
    task = Edge3()
    task.inputs.in_file = Nifti1.sample(seed=0)
    task.inputs.out_file = "edges.nii"
    task.inputs.datum = "byte"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)
