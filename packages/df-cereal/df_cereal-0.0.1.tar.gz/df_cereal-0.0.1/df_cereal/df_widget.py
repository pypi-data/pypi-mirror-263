#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Paddy Mullen.
# Distributed under the terms of the Modified BSD License.

"""
TODO: Add module docstring
"""

import pandas as pd
import json

from ipywidgets import DOMWidget
from traitlets import Unicode, Any
from ._frontend import module_name, module_version

def pd_to_obj(df:pd.DataFrame):
    obj = json.loads(df.to_json(orient='table', indent=2, default_handler=str))

    if isinstance(df.index, pd.MultiIndex):
        old_index = df.index
        temp_index = pd.Index(df.index.to_list(), tupleize_cols=False)
        df.index = temp_index
        obj = json.loads(df.to_json(orient='table', indent=2, default_handler=str))
        df.index = old_index
    else:
        obj = json.loads(df.to_json(orient='table', indent=2, default_handler=str))
    return obj['data']

class BaseWidget(DOMWidget):
    """
    Repetitious code needed to make Jupyter communicate properly with any BuckarooWidget in this package
    
    """

    _model_module = Unicode(module_name).tag(sync=True)
    _view_module  = Unicode(module_name).tag(sync=True)

    _model_module_version = Unicode(module_version).tag(sync=True)
    _view_module_version  = Unicode(module_version).tag(sync=True)

    _model_name = Unicode('ReactWidgetModel').tag(sync=True)
    
class DFWidget(BaseWidget):

    _view_name = Unicode('SimpleDFWidgetView').tag(sync=True)
    df_data = Any([]).tag(sync=True)

    '''

    df_data = List([
        {'a':  5  , 'b':20, 'c': 'Paddy'},
        {'a': 58.2, 'b': 9, 'c': 'Margaret'}]).tag(sync=True)
    '''
    
    def __init__(self, df):
        super().__init__()
        self.df_data = self._df_to_obj(df)

    def _df_to_obj(self, df:pd.DataFrame):
        return pd_to_obj(df)

class PolarsDFWidget(DFWidget):

    def _df_to_obj(self, df):
        # I want to this, but then row numbers are lost
        #return pd_to_obj(self.sampling_klass.serialize_sample(df).to_pandas())
        return pd_to_obj(df.to_pandas())

