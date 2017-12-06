import pandas as pd
import numpy as np
import numpy.testing as npt

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

def test_two_way_data():
	student_perf = pd.read_table('data/student-por.csv', sep = ';')
	exp = pd.crosstab(student_perf.traveltime, student_perf.reason, margins=False)
	obs = two_way(student_perf, 'traveltime', 'reason')
	npt.assert_array_equal(exp, obs)

def test_two_way_simple():
	d = {'col1': [1, 2, 3, 3, 2, 1], 'col2': [1, 1, 2, 2, 2, 2]}
	df = pd.DataFrame(data=d)
	exp = pd.crosstab(df.col1, df.col2, margins=False)
	obs = two_way(df, 'col1', 'col2')
	npt.assert_array_equal(exp, obs)

