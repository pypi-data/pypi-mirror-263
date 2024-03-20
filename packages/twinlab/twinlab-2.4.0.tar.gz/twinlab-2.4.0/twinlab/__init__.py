# Version
from ._version import __version__

# General functions
# NOTE: Deprecated (v1)
from .client import (
    set_api_key,
    set_server_url,
    get_api_key,
    get_server_url,
    get_user_information,
    get_versions,
    list_datasets,
    list_campaigns,
)

# Dataset functions
# NOTE: Deprecated (v1)
from .client import (
    upload_dataset,
    query_dataset,
    view_dataset,
    delete_dataset,
)

# Campaign functions
# NOTE: Deprecated (v1)
from .client import (
    train_campaign,
    query_campaign,
    view_campaign,
    predict_campaign,
    sample_campaign,
    active_learn_campaign,
    solve_inverse_campaign,
    optimise_campaign,
    score_campaign,
    get_calibration_curve_campaign,
    delete_campaign,
)

# Prior class
from .prior import (
    Prior,
)

# Distribution class
from .distributions import (
    Distribution,
)

# Sampling methods
from .sampling import (
    Sampling,
)

# General functions
from .core import (
    versions,
    user_information,
    set_api_key,
    get_api_key,
    set_server_url,
    get_server_url,
    list_datasets,
    list_emulators,
    list_example_datasets,
    load_example_dataset,
)

from .dataset import Dataset

from .emulator import Emulator

from .params import (
    EstimatorParams,
    ModelSelectionParams,
    TrainParams,
    ScoreParams,
    BenchmarkParams,
    PredictParams,
    SampleParams,
    RecommendParams,
    CalibrateParams,
    DesignParams,
)

from .helper import load_dataset, load_params, get_sample, join_samples
