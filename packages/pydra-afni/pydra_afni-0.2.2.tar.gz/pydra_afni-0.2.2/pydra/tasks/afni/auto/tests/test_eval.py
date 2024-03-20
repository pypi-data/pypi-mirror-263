from fileformats.generic import File
from fileformats.medimage_afni import OneD
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.auto.eval import Eval
import pytest


@pytest.mark.xfail
def test_eval_1():
    task = Eval()
    task.inputs.in_file_a = OneD.sample(seed=0)
    task.inputs.in_file_b = OneD.sample(seed=1)
    task.inputs.in_file_c = File.sample(seed=2)
    task.inputs.other = File.sample(seed=9)
    task.inputs.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_eval_2():
    task = Eval()
    task.inputs.in_file_a = OneD.sample(seed=0)
    task.inputs.in_file_b = OneD.sample(seed=1)
    task.inputs.out_file = "data_calc.1D"
    task.inputs.out1D = True
    task.inputs.expr = "a*b"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)
