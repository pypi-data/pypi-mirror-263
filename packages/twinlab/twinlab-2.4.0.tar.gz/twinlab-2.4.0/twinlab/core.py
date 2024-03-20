# Standard imports
import io
import os
from pprint import pprint
from typing import Dict, List, Optional

import pandas as pd

# Third-party imports
from typeguard import typechecked

# Project imports
from . import api, utils

# Parameters
# NOTE: For developer debugging purposes, turn to True to see more verbosity and logging from the API
DEBUG = False


@typechecked
def set_api_key(api_key: str, verbose: bool = False) -> None:
    """
    # Set API key

    Set the user API key for their `twinLab` cloud account.

    ## Arguments:

    - `api_key`: `str`. API key for the `twinLab` cloud.
    - `verbose`: `bool`, `optional`. Determining level of information returned to the user.

    ## Example:

    ```python
    import twinlab as tl

    tl.set_api_key("12345")
    ```
    """
    os.environ["TWINLAB_API_KEY"] = api_key
    if verbose:
        print("API key: {}".format(api_key))


@typechecked
def set_server_url(url: str, verbose: bool = False) -> None:
    """
    # Set server URL

    Set the URL from which `twinLab` is being served from.

    ## Arguments:

    - `url`: `str`. URL for the `twinLab` cloud.
    - `verbose`: `bool`, `optional`. Determining level of information returned to the user.

    ## Example:

    ```python
    import twinlab as tl

    tl.set_server_url("https://twinlab.digilab.co.uk")
    ```
    """
    os.environ["TWINLAB_URL"] = url
    if verbose:
        print("Server URL: {}".format(url))


@typechecked
def get_server_url(verbose: bool = False) -> str:
    """
    # Get the server URL

    Fetch the URL from which `twinLab` is being served from.

    ## Arguments:

    - `verbose`: `bool`, `optional`. Determining level of information returned to the user.

    ## Returns:

    - `str` containing the server URL.

    ## Example:

    ```python
    import twinlab as tl

    tl.get_server_url()
    ```
    """
    server_url = os.getenv("TWINLAB_URL")
    if verbose:
        print("Server URL: {}".format(server_url))
    return server_url


@typechecked
def get_api_key(verbose: bool = False) -> str:
    """
    # Get the user API key

    Get a user API key for their`twinLab` cloud account.

    ## Arguments:

    - `verbose`: `bool`, `optional`. Determining level of information returned to the user.

    ## Returns:

    - `str` containing the server API key.

    ## Example:

    ```python
    import twinlab as tl

    tl.get_api_key()
    ```
    """
    api_key = os.getenv("TWINLAB_API_KEY")
    if verbose:
        print("API key: {}".format(api_key))
    return api_key


@typechecked
def user_information(verbose: bool = False) -> Dict:
    """
    # User information

    Get information about the user.

    ## Arguments:

    - `verbose`: `bool`, `optional`. Determining level of information returned to the user.

    ## Returns:

    - `dict` containing user information.

    ## Example:

    ```python
    import twinlab as tl

    user_info = tl.user_information()
    print(user_info)
    ```
    """
    _, response = api.get_user(verbose=DEBUG)
    user_info = response
    if verbose:
        print("User information:")
        pprint(user_info, compact=True, sort_dicts=False)
    return user_info


@typechecked
def versions(verbose: bool = False) -> Dict[str, str]:
    """
    # twinLab versions

    Get information about the twinLab version being used.

    ## Arguments:

    - `verbose`: `bool`, `optional`. Determining level of information returned to the user.

    ## Returns:

    - `dict` containing version information.

    ## Example:

    ```python
    import twinlab as tl

    version_info = tl.versions()
    print(version_info)
    ```
    """
    _, response = api.get_versions(verbose=DEBUG)
    version_info = response
    if verbose:
        print("Version information:")
        pprint(version_info, compact=True, sort_dicts=False)
    return version_info


@typechecked
def list_datasets(verbose: bool = False) -> List[str]:
    """
    # List datasets

    List datasets that have been uploaded to the user's `twinLab` cloud account.

    ## Arguments:

    - `verbose`: `bool`, `optional`. Determining level of information returned to the user.

    ## Returns:

    - `list` of `str` dataset IDs.

    ## Example:

    ```python
    import pandas as pd
    import twinlab as tl

    datasets = tl.list_datasets()
    print(datasets)
    ```
    """
    _, response = api.list_datasets(verbose=DEBUG)
    datasets = utils.get_value_from_body("datasets", response)
    if verbose:
        print("Datasets:")
        pprint(datasets, compact=True, sort_dicts=False)
    return datasets


@typechecked
def list_emulators(verbose: bool = False) -> Optional[List[str]]:
    """
    # List emulators

    List emulators that have been set up in the user's `twinLab` cloud account.

    ## Arguments:
    - `verbose`: `bool`, `Optional`. Determine the level of information returned to the user. If True, user will see the run time, start time, and status of an emulator.

    ## Returns:
    - A `list` of `str` emulator IDs where `train` has been called.

    ## Example:

    ```python
    import twinlab as tl

    emulators = tl.list_emulators()
    print(emulators)
    ```
    """

    _, response = api.list_models(verbose=DEBUG)
    emulators = utils.get_value_from_body("model_information", response)

    # Standardise dictionary for failed cases
    for emulator in emulators:
        if "run_time" not in emulator:
            emulator["run_time"] = "NaN"
        if "start_time" not in emulator:
            emulator["start_time"] = "NaN"

    # Create dictionary of cuddly response
    status_dict = {
        "success": "Successfully trained emulators:",
        "in_progress": "Emulators currently training:",
        "failed": "Emulators that failed to train:",
    }

    verbose_keys = ("model", "start_time", "run_time")
    if verbose:
        for status, nice_status in status_dict.items():
            emus = [emu for emu in emulators if emu["status"] == status]
            # Sort through dictionary via success, in_progress, failed
            emus = [dict((key, emu[key]) for key in verbose_keys) for emu in emus]
            emus = sorted(emus, key=lambda d: d["start_time"])
            # List models in order from starting time
            if emus:
                # Only print list if there are available emulators to list
                print(nice_status)
                pprint(emus)
    # Return a simple list of trained emulators for backwards compatability
    return [emulator["model"] for emulator in emulators]


@typechecked
def list_example_datasets(verbose: bool = False) -> list:
    """
    # List example datasets

    List example datasets that are available for loading from the `twinLab` cloud.

    ## Arguments:

    - `verbose`: `bool`, `Optional`. Determining level of information returned to the user.

    ## Returns:

    - A `list` of `str` dataset IDs.

    ## Example:

    ```python
    import twinlab as tl

    example_datasets = tl.list_example_datasets()
    print(example_datasets)
    """
    _, response = api.list_example_datasets(verbose=verbose)
    datasets = utils.get_value_from_body("datasets", response)
    if verbose:
        print("Example datasets:")
        pprint(datasets, compact=True, sort_dicts=False)

    return datasets


def load_example_dataset(dataset_id: str, verbose: bool = False) -> pd.DataFrame:
    """
    # Load example dataset

    Download an example dataset from the `twinLab` cloud.
    Available datasets: biscuits, gardening, fusion

    ## Arguments:

    - `dataset_id`: `str`. The ID of the dataset to download.
    - `verbose`: `bool`, `Optional`. Determining level of information returned to the user.

    ## Returns:

    - A `pandas.DataFrame` containing the example dataset.

    ## Example:

    ```python
    import twinlab as tl

    df = tl.download_example_dataset("biscuits")
    print(df)

    """
    _, response = api.load_example_dataset(dataset_id, verbose=verbose)
    csv = utils.get_value_from_body("dataset", response)
    csv = io.StringIO(csv)
    df = pd.read_csv(csv, sep=",")
    if verbose:
        print("Example dataset:")
        pprint(df, compact=True, sort_dicts=False)
    print("Dataframe downloaded successfully")
    return df
