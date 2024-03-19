#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 13:53:36 2024

@author: mike
"""
import pandas as pd
import os
import pathlib

from npsfm import NPSFM

########################################################3
### Parameters

script_path = pathlib.Path(os.path.realpath(os.path.dirname(__file__)))
data_path = script_path.parent.parent.joinpath('data')


########################################################
### Test

ts_data = pd.read_csv(script_path.joinpath('test_data1.csv.zip'), index_col=0, parse_dates=True)['value']

nzsegment = 3076139
parameter = 'Nitrate'
feature = 'river'
version = 'v202401'
hopeful_state = 'A'

self = NPSFM(data_path)
limits = self.add_limits(parameter, feature, nzsegment)
stats = self.add_stats(ts_data)
attr_state = self.calc_state()

improve_ratio1 = self.calc_improvement_to_state(hopeful_state)
improve_ratio2 = self.calc_improvement_to_bottom_line()




























































