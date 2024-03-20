from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.auto.cat_matvec import CatMatvec
import pytest


@pytest.mark.xfail
def test_catmatvec_1():
    task = CatMatvec()
    task.inputs.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_catmatvec_2():
    task = CatMatvec()
    task.inputs.in_file = [("structural.BRIK::WARP_DATA", "I")]
    task.inputs.out_file = "warp.anat.Xat.1D"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(plugin=PassAfterTimeoutWorker)
    print("RESULT: ", res)
