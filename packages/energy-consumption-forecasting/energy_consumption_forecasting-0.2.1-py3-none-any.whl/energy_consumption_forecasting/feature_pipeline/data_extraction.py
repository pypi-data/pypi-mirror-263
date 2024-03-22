import datetime
import os
from json import dump
from pathlib import Path
from typing import Any, Dict, Optional, Tuple

import httpx
import pandas as pd
from pydantic import HttpUrl, validate_call

from energy_consumption_forecasting.exceptions import log_exception
from energy_consumption_forecasting.logger import get_logger
from energy_consumption_forecasting.utils import get_env_var, save_json_data

logger = get_logger(name=Path(__file__).name)
ROOT_DIRPATH = Path(get_env_var(key="PROJECT_ROOT_DIR_PATH", default_value="."))


@log_exception(logger=logger)
@validate_call
def get_extraction_datetime(
    start_date_time: datetime.datetime,
    end_date_time: datetime.datetime,
) -> Tuple[str, str]:
    """
    This Function formats the datetime in a format that the API will accept.

    Parameters
    ----------
    start_date_time: datetime.datetime
        A starting date and time for extracting the data in datatype of
        datetime.datetime.

    end_date_time: datetime.datetime
        A ending date and time for extracting the data in datatype of
        datetime.datetime.

    Returns
    -------
    start_date_time: str
        A string of formatted starting date and time.

    end_date_time: str
        A string of formatted ending date and time.
    """

    # Checking if end date is greater than start date
    if start_date_time > end_date_time:
        raise Exception("End date needs to be greater than the start date")

    # Converting the date format for API query and
    # increasing the end date by 1 day as per the API guide
    start_date_time = start_date_time.strftime("%Y-%m-%dT%H:%M")
    end_date_time = (end_date_time + datetime.timedelta(days=1)).strftime(
        "%Y-%m-%dT%H:%M"
    )

    return start_date_time, end_date_time


@log_exception(logger=logger)
@validate_call
def extract_dataset_from_api(
    start_date_time: datetime.datetime,
    end_date_time: datetime.datetime,
    sort_data_asc: bool = True,
    dataset_name: str = "ConsumptionIndustry",
    base_url: HttpUrl = "https://api.energidataservice.dk/dataset/",
    meta_url: HttpUrl = "https://api.energidataservice.dk/meta/dataset/",
    save_dataset_metadata: bool = True,
) -> Optional[Tuple[pd.DataFrame, Dict[str, Any] | Path, Path]]:
    """
    This function extracts data using the API from the
    Denmark Energy Data Service website: "https://www.energidataservice.dk/".

    Parameters
    ----------
    start_date_time: datetime.datetime
        A starting date and time for extracting the data in datatype of
        datetime.datetime.

    end_date_time: datetime.datetime
        A ending date and time for extracting the data in datatype of
        datetime.datetime.

    sort_data_asc: bool, default=True
        Sort the data using the UTC datetime column, by default data is sorted
        in ascending order.

    dataset_name: str, default="ConsumptionIndustry"
        A string containing the dataset name that needs to be extracted from
        the website.
        You can find the dataset name under the section of Additional Info in
        Alias tag.

    base_url: str, default="https://api.energidataservice.dk/dataset/"
        The base URL for the data.

    meta_url: str, default="https://api.energidataservice.dk/meta/dataset/"
        The base URL for the metadata.

    save_dataset_metadata: bool, default=True
        Whether to save the dataset as a CSV file and metadata as a JSON file.

    Returns
    -------
    pd.DataFrame, Dict[str, Any] or Path, Path
        A tuple containing the dataset in pandas DataFrame and a Dict containing
        the metadata of the dataset.
        If save_dataset_metadata parameter is True, then filepath for both the
        data is returned as string along with the DataFrame and Dict.
    """

    data_url = f"{base_url}{dataset_name}?"
    meta_url = f"{meta_url}{dataset_name}?"
    sort = "HourUTC" if sort_data_asc else "HourUTC%20DESC"

    # Formatting the dates for the API parameters
    start, end = get_extraction_datetime(
        start_date_time=start_date_time, end_date_time=end_date_time
    )

    # Creating the parameters for the API request
    params = {
        "offset": 0,
        "start": start,
        "end": end,
        "sort": sort,
    }

    # Calling the API requests for dataset and metadata
    with httpx.Client() as client:
        logger.info(
            f"Sending API get request to: {data_url} and {meta_url} "
            f"with parameters: {params}."
        )

        data_response = client.get(url=data_url, params=params, timeout=None)
        meta_response = client.get(url=meta_url, timeout=None)

        logger.info(
            "Connection to the dataset API is done and response "
            f"received with status code: {data_response.status_code}."
        )
        logger.info(
            "Connection to the metadata API is done and response "
            f"received with status code: {meta_response.status_code}."
        )

        # Getting the data and metadata in json format for further processing
        json_data = data_response.json()
        json_meta = meta_response.json()

    # Getting the dataset from the JSON data and converting into dataframe
    json_data = json_data.get("records")
    dataset_df = pd.DataFrame.from_records(json_data)

    if save_dataset_metadata:
        data_dir = ROOT_DIRPATH / "data" / "raw_data"
        if not os.path.isdir(data_dir):
            os.makedirs(data_dir)

        start = start.replace(":", "-")
        end = end.replace(":", "-")
        data_filepath = data_dir / f"{dataset_name}_{start}_{end}.csv"
        meta_filepath = data_dir / f"{dataset_name}_metadata.json"

        logger.info(
            f'Saving the dataset "{data_filepath.name}" in '
            f'directory: "{data_dir.absolute()}".'
        )
        logger.info(
            f'Saving the metadata "{meta_filepath.name}" in '
            f'directory: "{data_dir.absolute()}".'
        )

        # Saving the dataset as a csv file and
        # meta data as JSON file in data directory
        dataset_df.to_csv(path_or_buf=data_filepath, index=False)
        save_json_data(data=json_meta, filepath=meta_filepath)

        logger.info(f'Dataset has been saved in csv file "{data_filepath.name}".')
        logger.info(f'Metadata has been saved in json file "{meta_filepath.name}".')

        return dataset_df, json_meta, data_filepath, meta_filepath

    return dataset_df, json_meta
