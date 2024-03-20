import pyarrow as pa
import pyarrow.feather as feather
import base64
import io

def arrow_to_bytes(table):
    fake_file = io.BytesIO()
    feather.write_feather(table, fake_file, compression='uncompressed')
    fake_file.seek(0)
    return fake_file.read()
    

def df_to_arrow_bytes(df):
    table = pa.Table.from_pandas(df)
    return arrow_to_bytes(table)
    
def df_to_base64(df):
    return base64.b64encode(df_to_arrow_bytes(df)).decode('utf8')
