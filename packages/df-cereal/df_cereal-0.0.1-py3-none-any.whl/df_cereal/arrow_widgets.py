from .df_widget import BaseWidget
from traitlets import Unicode, Dict, Any, Bytes, Bool

class Base64Widget(BaseWidget):
    _view_name = Unicode('Base64WidgetView').tag(sync=True)
    df_base64 = Any("").tag(sync=True)

class BytesWidget(BaseWidget):
    _view_name = Unicode('BytesWidgetView').tag(sync=True)
    df_arrow_bytes = Bytes().tag(sync=True)

class SimpleBytesBenchmarkWidget(BaseWidget):
    _view_name = Unicode('BytesBenchmarkWidgetView').tag(sync=True)
    df_arrow_bytes = Bytes().tag(sync=True)
    timing_info = Dict({}).tag(sync=True)
    do_calc = Bool(True).tag(sync=True)
