from typing import Optional, List

import numpy as np

from .rooproc_output_action import RooProcOutputAction

from quickstats import module_exist
from quickstats.utils.common_utils import is_valid_file
from quickstats.utils.data_conversion import ConversionMode
from quickstats.interface.root import RDataFrameBackend

class RooProcAsNumpy(RooProcOutputAction):
    
    def _execute(self, rdf:"ROOT.RDataFrame", processor:"quickstats.RooProcessor", **params):
        filename = params['filename']
        if processor.cache and is_valid_file(filename):
            processor.stdout.info(f"INFO: Cached output `{filename}`.")
            return rdf, processor
        processor.stdout.info(f'Saving output "{filename}".')
        columns = params.get('columns', None)
        columns = self.get_valid_columns(rdf, processor, columns=columns,
                                         mode=ConversionMode.REMOVE_NON_STANDARD_TYPE)
        array = None
        # NB: RDF Dask/Spark does not support GetColumnType yet
        if (module_exist('awkward') and \
            (processor.backend not in [RDataFrameBackend.DASK, RDataFrameBackend.SPARK])):
            try:
                import awkward as ak
                array = ak.from_rdataframe(rdf, columns=columns)
                array = ak.to_numpy(array)
            except:
                array = None
                processor.stdout.warning("Failed to convert output to numpy arrays with awkward backend. "
                                         "Falling back to use ROOT instead")
        if array is None:
            array = rdf.AsNumpy(columns)
        np.save(filename, array)
        return rdf, processor