import src.example1 as ex

def test_add_munbers_pass():
	assert ex.add_numbers(10,20) == 30
	
def test_add_munbers_fail():
	assert ex.add_numbers(10,20) == 50