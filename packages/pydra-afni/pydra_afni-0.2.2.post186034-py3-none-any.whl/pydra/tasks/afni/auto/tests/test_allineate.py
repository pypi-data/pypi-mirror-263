from fileformats.datascience.data import TextMatrix
from fileformats.generic import File
from fileformats.medimage.nifti import Nifti1
from fileformats.text import TextFile
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.auto.allineate import Allineate
import pytest


@pytest.mark.xfail
def test_allineate_1():
    task = Allineate()
    task.inputs.in_file = Nifti1.sample(seed=0)
    task.inputs.reference = Nifti1.sample(seed=1)
    task.inputs.in_param_file = File.sample(seed=4)
    task.inputs.in_matrix = TextMatrix.sample(seed=6)
    task.inputs.weight_file = File.sample(seed=29)
    task.inputs.source_mask = File.sample(seed=32)
    task.inputs.master = File.sample(seed=43)
    task.inputs.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_allineate_2():
    task = Allineate()
    task.inputs.in_file = Nifti1.sample(seed=0)
    task.inputs.out_file = "functional_allineate.nii"
    task.inputs.in_matrix = TextMatrix.sample(seed=6)
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_allineate_3():
    task = Allineate()
    task.inputs.in_file = Nifti1.sample(seed=0)
    task.inputs.reference = Nifti1.sample(seed=1)
    task.inputs.allcostx = "out.allcostX.txt"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_allineate_4():
    task = Allineate()
    task.inputs.in_file = Nifti1.sample(seed=0)
    task.inputs.reference = Nifti1.sample(seed=1)
    task.inputs.nwarp_fixmot = ["X", "Y"]
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)
