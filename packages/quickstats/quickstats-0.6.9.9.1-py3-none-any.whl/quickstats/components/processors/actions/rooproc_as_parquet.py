from typing import Optional, List

import numpy as np

from .rooproc_output_action import RooProcOutputAction

from quickstats.utils.common_utils import is_valid_file
from quickstats.utils.data_conversion import ConversionMode
from quickstats.interface.root import RDataFrameBackend

class RooProcAsParquet(RooProcOutputAction):

    def _execute(self, rdf:"ROOT.RDataFrame", processor:"quickstats.RooProcessor", **params):
        filename = params['filename']
        if processor.cache and is_valid_file(filename):
            processor.stdout.info(f"Cached output `{filename}`.")
            return rdf, processor
        processor.stdout.info(f'Saving output "{filename}".')
        columns = params.get('columns', None)
        columns = self.get_valid_columns(rdf, processor, columns=columns,
                                         mode=ConversionMode.REMOVE_NON_STANDARD_TYPE)
        import awkward as ak
        # NB: RDF Dask/Spark does not support GetColumnType yet
        if processor.backend not in [RDataFrameBackend.DASK, RDataFrameBackend.SPARK]:
            array = ak.from_rdataframe(rdf, columns=columns)
        else:  
            array = ak.Array(rdf.AsNumpy(columns))
        ak.to_parquet(array, filename)
        return rdf, processor