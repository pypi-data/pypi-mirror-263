import pandas as pd

from dvcx.lib.dataset import Dataset
from dvcx.lib.webdataset import WebDataset
from dvcx.lib.webdataset_meta import MergeParquetAndNpz
from dvcx.query.schema import C, DatasetRow
from dvcx.sql.functions import path

threads = 8

wds = (
    Dataset("gcs://dvcx-datacomp-small/shards")
    .filter(C.name.glob("0000000*.tar"))
    .generate(WebDataset(extensions=["json"]), parallel=threads)
)

meta = (
    Dataset("gcs://dvcx-datacomp-small/metadata")
    .filter(C.name.glob("0020f*"))
    .aggregate(
        MergeParquetAndNpz(), partition_by=path.file_stem(C.name), parallel=threads
    )
    .select_except(*DatasetRow.schema.keys())
)

res = wds.join(meta, "uid")

ds_name = "laion_wds"
res.save(ds_name)

df = Dataset(name=ds_name).limit(50).to_pandas()
with pd.option_context("display.max_columns", None):
    print(df)
