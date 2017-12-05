import pandas as pd

from p3functions import *

  
def test_make_indicators():
	d = {'col1': [1, 2], 'col2': [3, 4]}
	df = pd.DataFrame(data=d)
	names = {'ind1': ('col1', 2), 'ind2': ('col2', 3)}
	make_indicators(df,names)
	exp_d = {'col1': [1, 2], 'col2': [3, 4], 'ind1': [0, 1], 'ind2': [1,0]}
	exp = pd.DataFrame(data=exp_d)
	obs = df
	assert obs.equals(exp)
