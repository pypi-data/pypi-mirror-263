from fileformats.generic import File
from fileformats.medimage.nifti import Nifti1
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.auto.calc import Calc
import pytest


@pytest.mark.xfail
def test_calc_1():
    task = Calc()
    task.inputs.in_file_a = Nifti1.sample(seed=0)
    task.inputs.in_file_b = Nifti1.sample(seed=1)
    task.inputs.in_file_c = File.sample(seed=2)
    task.inputs.other = File.sample(seed=9)
    task.inputs.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_calc_2():
    task = Calc()
    task.inputs.in_file_a = Nifti1.sample(seed=0)
    task.inputs.in_file_b = Nifti1.sample(seed=1)
    task.inputs.out_file = "functional_calc.nii.gz"
    task.inputs.expr = "a*b"
    task.inputs.outputtype = "NIFTI"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_calc_3():
    task = Calc()
    task.inputs.in_file_a = Nifti1.sample(seed=0)
    task.inputs.out_file = "rm.epi.all1"
    task.inputs.expr = "1"
    task.inputs.overwrite = True
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)
