# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
"""Optimization stuff. In particular, optimizers (DAdaptAdam), schedulers
and Exponential Moving Average.
"""

# flake8: noqa
from .dadam import DAdaptAdam
from .ema import ModuleDictEMA
