# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from jaxopt._src.objective import CompositeLinearFunction
from jaxopt._src.objective import least_squares
from jaxopt._src.objective import multiclass_logreg
from jaxopt._src.objective import multiclass_logreg_with_intercept
from jaxopt._src.objective import l2_multiclass_logreg
from jaxopt._src.objective import l2_multiclass_logreg_with_intercept
from jaxopt._src.objective import binary_logreg
from jaxopt._src.objective import multiclass_linear_svm_dual
