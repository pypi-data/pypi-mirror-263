from fileformats.generic import Directory
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.auto.to_3d import To3D
import pytest


@pytest.mark.xfail
def test_to3d_1():
    task = To3D()
    task.inputs.in_folder = Directory.sample(seed=1)
    task.inputs.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_to3d_2():
    task = To3D()
    task.inputs.out_file = "dicomdir.nii"
    task.inputs.in_folder = "."
    task.inputs.filetype = "anat"
    task.inputs.datatype = "float"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)
