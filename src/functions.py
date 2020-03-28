#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 15:54:38 2020

@author: skuarch
"""

from variables import *


def convert_states_in_numbers(df):
    data_frame = df
    states_list = set(df['state'].values.tolist())

    for state in states_list:
          data_frame.replace(state, states_dict[state], inplace=True)

    return data_frame