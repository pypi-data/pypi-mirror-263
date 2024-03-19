# Copyright 2022 Sony Semiconductor Israel, Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from typing import Callable

from model_compression_toolkit.logger import Logger
from model_compression_toolkit.constants import PYTORCH
from model_compression_toolkit.target_platform_capabilities.target_platform import TargetPlatformCapabilities
from model_compression_toolkit.core.common.mixed_precision.kpi_tools.kpi import KPI
from model_compression_toolkit.core.common.framework_info import FrameworkInfo
from model_compression_toolkit.core.common.mixed_precision.kpi_tools.kpi_data import compute_kpi_data
from model_compression_toolkit.core.common.quantization.core_config import CoreConfig
from model_compression_toolkit.core.common.mixed_precision.mixed_precision_quantization_config import MixedPrecisionQuantizationConfig
from model_compression_toolkit.constants import FOUND_TORCH

if FOUND_TORCH:
    from model_compression_toolkit.core.pytorch.default_framework_info import DEFAULT_PYTORCH_INFO
    from model_compression_toolkit.core.pytorch.pytorch_implementation import PytorchImplementation
    from model_compression_toolkit.target_platform_capabilities.constants import DEFAULT_TP_MODEL
    from torch.nn import Module

    from model_compression_toolkit import get_target_platform_capabilities

    PYTORCH_DEFAULT_TPC = get_target_platform_capabilities(PYTORCH, DEFAULT_TP_MODEL)


    def pytorch_kpi_data(in_model: Module,
                         representative_data_gen: Callable,
                         core_config: CoreConfig = CoreConfig(),
                         target_platform_capabilities: TargetPlatformCapabilities = PYTORCH_DEFAULT_TPC) -> KPI:
        """
        Computes KPI data that can be used to calculate the desired target KPI for mixed-precision quantization.
        Builds the computation graph from the given model and target platform capabilities, and uses it to compute the KPI data.

        Args:
            in_model (Model): PyTorch model to quantize.
            representative_data_gen (Callable): Dataset used for calibration.
            core_config (CoreConfig): CoreConfig containing parameters for quantization and mixed precision
            target_platform_capabilities (TargetPlatformCapabilities): TargetPlatformCapabilities to optimize the PyTorch model according to.

        Returns:

            A KPI object with total weights parameters sum and max activation tensor.

        Examples:

            Import a Pytorch model:

            >>> from torchvision import models
            >>> module = models.mobilenet_v2()

            Create a random dataset generator:

            >>> import numpy as np
            >>> def repr_datagen(): yield [np.random.random((1, 3, 224, 224))]

            Import mct and call for KPI data calculation:

            >>> import model_compression_toolkit as mct
            >>> kpi_data = mct.core.pytorch_kpi_data(module, repr_datagen)

        """

        if not isinstance(core_config.mixed_precision_config, MixedPrecisionQuantizationConfig):
            Logger.error("KPI data computation can't be executed without MixedPrecisionQuantizationConfig object."
                         "Given quant_config is not of type MixedPrecisionQuantizationConfig.")

        fw_impl = PytorchImplementation()

        return compute_kpi_data(in_model,
                                representative_data_gen,
                                core_config,
                                target_platform_capabilities,
                                DEFAULT_PYTORCH_INFO,
                                fw_impl)

else:
    # If torch is not installed,
    # we raise an exception when trying to use this function.
    def pytorch_kpi_data(*args, **kwargs):
        Logger.critical('Installing torch is mandatory when using pytorch_kpi_data. '
                        'Could not find Tensorflow package.')  # pragma: no cover
