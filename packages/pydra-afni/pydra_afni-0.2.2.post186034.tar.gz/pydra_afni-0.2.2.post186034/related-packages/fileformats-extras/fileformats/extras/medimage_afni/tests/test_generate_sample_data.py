import pytest
from fileformats.medimage_afni import (
    OneD,
    ThreeD,
    R1,
    All1,
    Dset,
    Head,
)


@pytest.mark.xfail(reason="generate_sample_data not implemented")
def test_generate_sample_oned_data():
    assert isinstance(OneD.sample(), OneD)


@pytest.mark.xfail(reason="generate_sample_data not implemented")
def test_generate_sample_threed_data():
    assert isinstance(ThreeD.sample(), ThreeD)


@pytest.mark.xfail(reason="generate_sample_data not implemented")
def test_generate_sample_r1_data():
    assert isinstance(R1.sample(), R1)


@pytest.mark.xfail(reason="generate_sample_data not implemented")
def test_generate_sample_all1_data():
    assert isinstance(All1.sample(), All1)


@pytest.mark.xfail(reason="generate_sample_data not implemented")
def test_generate_sample_dset_data():
    assert isinstance(Dset.sample(), Dset)


@pytest.mark.xfail(reason="generate_sample_data not implemented")
def test_generate_sample_head_data():
    assert isinstance(Head.sample(), Head)
