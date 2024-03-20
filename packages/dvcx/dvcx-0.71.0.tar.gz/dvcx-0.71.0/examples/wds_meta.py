import pandas as pd

from dvcx.lib.dataset import C, Dataset
from dvcx.lib.stream import FileStream
from dvcx.lib.webdataset_meta import LaionMeta, parse_wds_meta

ds = Dataset("s3://dvcx-datacomp-small", client_config={"aws_anon": True})
ds = ds.filter(C.name.glob("0020f*"))
ds = ds.apply(parse_wds_meta)

ds = ds.select(
    FileStream.name,
    FileStream.parent,
    LaionMeta.uid,
    LaionMeta.original_width,
    LaionMeta.face_bboxes,
    LaionMeta.b32_img,
    LaionMeta.dedup,
)

with pd.option_context("display.max_columns", None):
    print(ds.to_pandas())
