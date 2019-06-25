import pytest

def test_len_leapwacom():
    with open('data/LeapData', 'r') as f:
        content_leap = f.readlines()
    with open('data/WacomData', 'r') as g:
        content_wacom = g.readlines()
    assert len(content_leap) == len(content_wacom),"Using threading to obtain synchronised Leap and Wacom readings: Length of the Leap and Wacom data files should be same"