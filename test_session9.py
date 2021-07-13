import pytest
from io import StringIO 
import sys
import session9
from session9 import *


n = create_nt_from_fakeprofile(10)
d = create_dict_from_fakeprofile(10)

def test_return_namedtuple():
    assert isinstance(n,tuple)==True, "Check NT Return Type"

def test_max_bloodgroup_nt():
    assert isinstance(max_bloodgroup_nt(n),str)==True, "Check BG NT Return Type"

def test_mean_currentlocation_nt():
    assert isinstance(mean_currentlocation_nt(n),tuple)==True, "Check CL NT Return Type"

def test_oldest_age_nt():
    assert isinstance(oldest_age_nt(n), int)==True, "Check NT OA Return Type"

def test_mean_age_nt():
    assert isinstance(mean_age_nt(n),float)==True, "Check NT MA Return Type"



def test_return_dict():
    assert isinstance(d,dict)==True, "Check Dict Return Type"

def test_max_bloodgroup_dict():
    assert isinstance(max_bloodgroup_dict(d),str)==True, "Check BG D Return Type"

def test_mean_currentlocation_dict():
    assert isinstance(mean_currentlocation_dict(d),tuple)==True, "Check CL D Return Type"

def test_oldest_age_dict():
    assert isinstance(oldest_age_dict(d),int)==True, "Check OA D Return Type"

def test_mean_age_dict():
    assert isinstance(mean_age_dict(d),float)==True, "Check MA D Return Type"



class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout


def test_se_blank_input():
    with Capturing() as output:
        stock_trades_days()
    assert any(["The opening" in o for o in output]),"Check proper doc for blank_input"

def test_se_zero_input():
    with Capturing() as output:
        stock_trades_days(0,0)
    assert any(["less than" in o for o in output]), "Check proper doc for zero_input"

def test_se_negative_input():
    with Capturing() as output:
        stock_trades_days(-1,-1)
    assert any(["less than" in o for o in output]), "Check proper doc for negative_input"

def test_se_create_fn_docexists():
    assert "faker" in stockexchange.__doc__, "Check proper doc for stock trade days function"
    
def test_se_days_trade_docexists():
    assert "days and trades" in stock_trades_days.__doc__, "Check proper doc for stock trade days function"

def test_se_company_proper_return():
    assert isinstance(initial.company,tuple), "Check company Return Type"

def test_se_symbol_proper_return():
    assert isinstance(initial.symbol,tuple), "Check symbol Return Type"

def test_se_openn_proper_return():
    assert isinstance(initial.openn,list), "Check openn Return Type"

def test_se_high_proper_return():
    assert isinstance(initial.high,list), "Check high Return Type"

def test_se_close_proper_return():
    assert isinstance(initial.close,list), "Check close  Return Type"

