import logging
import os
import re
import typing as t
from typing import Optional
from typing import Type

import a2.dataset
import a2.utils.constants
import a2.utils.testing
import a2.utils.utils
import numpy as np
import pandas as pd

xarray, xarray_dataset_type, xarray_dataarray_type = a2.utils.utils._import_xarray_and_define_xarray_type(
    __file__, also_return_dataarray=True
)


def _get_dataset_backend():
    backend = os.environ.get("A2_DATASET_BACKEND", "xarray")
    if backend not in a2.utils.constants.TYPE_DATASET_BACKEND:
        raise NotImplementedError(f"{backend=} not recognized!")
    return backend


def _using_xarray():
    return "xarray" == _get_dataset_backend()


def _using_pandas():
    return "pandas" == _get_dataset_backend()


def is_same_type_data_array(ds: xarray_dataset_type, field: t.Hashable, which_type: type = str):
    return all(isinstance(x, which_type) for x in ds[field].values)


def is_nan(
    ds: xarray_dataset_type,
    field: t.Union[str, t.Hashable],
    dims: Optional[t.Tuple] = None,
):
    """
    Test element-wise for nan-values and returns boolean mask as DataArray

    If DataArray consists only of strings, "nan" is assumed to be a nan-value.
    Parameters:
    ----------
    ds: dataset
    field: Key variable to check for nans
    dims: Dimensions of field

    Returns
    -------
    Boolean DataArray
    """
    if _using_xarray():
        if dims is None:
            dims = ds[field].coords.dims
        if is_same_type_data_array(ds, field):
            is_na = xarray.DataArray(ds[field].values == "nan", dims=dims)
        else:
            is_na = xarray.DataArray(pd.isna(ds[field].values), dims=dims)
    elif _using_pandas():
        is_na = ds[field].isna()
    return is_na


def ds_shape(ds, variable=None):
    if _using_xarray():
        if variable is None:
            variable = "index"
        shape = np.shape(ds[variable])
    elif _using_pandas():
        shape = ds.shape
    return shape


def drop_nan(
    ds,
    columns,
    dims: Optional[t.Tuple] = None,
):
    if _using_xarray():

        def _compute_mask(ds, column, dims):
            if dims is None:
                dims = ds[column].coords.dims
            return xarray.DataArray(~is_nan(ds, column).values, dims=dims)

        mask = _compute_mask(ds, columns.pop(0), dims)
        for c in columns:
            mask = np.logical_and(mask, _compute_mask(ds, c, dims))
        logging.info(f"Dropping {np.sum(~mask.values)}/{len(ds.index)} nan-values.")
        return ds.where(mask, drop=True)
    elif _using_pandas():
        return ds.dropna(subset=columns)


def is_na(
    ds: xarray_dataset_type,
    field: str,
    check: t.Optional[t.List[str]] = None,
    dims: Optional[t.Tuple] = None,
):
    """
    Returns boolean data array that notes if either field in `check` is matched.

    Parameters:
    ----------
    ds: Dataset
    field: Key variable to check for na values
    check: Values to check for that are considered 'na'
    dims: Dimensions of field

    Returns
    -------
    dict of json response
    """
    if dims is None:
        dims = ds[field].coords.dims
    if check is None:
        check = ["nan", ""]
    conditions = []
    if "nan" in check:
        conditions.append(is_nan(ds, field, dims=dims))
        check.remove("nan")
    for c in check:
        conditions.append(xarray.DataArray(ds[field] == c, dims=dims))
    combine = conditions[0]
    for cond in conditions:
        combine = np.logical_or(combine, cond)
    return combine


def print_tweet_sample(
    ds: xarray_dataset_type,
    n_sample: int = 5,
    n: int | None = None,
    fancy: bool = True,
    field_name_tweets: str = "text",
    additional_fields: list | None = [],
):
    """load tweets in filename and print random n_sample or n tweets from
    beginning of file"""
    fields = [field_name_tweets]
    if additional_fields is not None:
        fields += additional_fields
    print_sample(np.array([ds[key].values for key in fields]).T, n_sample=n_sample, n=n, fancy=fancy)


def print_sample(
    data: t.Union[t.Sequence, np.ndarray],
    n_sample: int = 5,
    n: t.Optional[int] = None,
    fancy: bool = True,
):
    """print data sample of sequence"""
    size_data = len(data)
    index_list = get_sample_indices(n, n_sample, size_data)
    for i in index_list:
        if fancy:
            print("------------------------------")
        print(data[i])


def get_sample_indices(n: t.Optional[int], n_sample: int, size_data: int) -> list:
    """Draws sample indices:
    n is None: returns `n_sample` randomly drawn values from size_data
    n < 0: returns range(size_data)
    else: returns range(n)
    """
    if n is None:
        index_list = list(a2.utils.utils.get_random_indices(n_sample=n_sample, size_data=size_data))
    elif n < 0:
        index_list = [i for i in range(size_data)]
    else:
        index_list = [i for i in range(n if n < size_data else size_data)]
    return index_list


def print_tweet_groupby(
    ds: xarray_dataset_type,
    group_by: t.Union[str, xarray_dataarray_type],
    n_sample: int = 5,
    n: Optional[int] = None,
    n_groups: int = 20,
    ds_grouped: Optional[xarray_dataset_type] = None,
    fancy: bool = True,
    fields_to_print: list = ["text"],
) -> xarray_dataset_type:
    """
    Print example tweets created per authors sorted by most active
    authors and source of post.

    Necessary grouping and summing steps are very costly such that the
    resulting dataset of this operation is returned
    by this function and can be provided as an argument `authors` to
    speed up additional prints

    Example:
        group_by_source = a2.dataset.utils_dataset.print_tweet_groupby(
            ds_tweets, "source", n_groups=10
        )
    Parameters:
    ----------
    ds: dataset
    n_sample: size of randomly selected tweets to printed per author
    n: number of tweets printed as ordered in dataset
    n_groups: number of authors shown
    authors: return value of this function, when provided for additional
             printing of same dataset, speeds up process considerably

    Returns
    -------
    dict of json response
    """
    ds_grouped, sort_by = dataset_groupby(ds, group_by, ds_grouped)
    group_by_variable_name = list(ds_grouped.coords.variables.keys())[0]
    for i, (number_tweets_per_group, group_name) in enumerate(
        zip(
            ds_grouped[sort_by].values,
            ds_grouped[group_by_variable_name].values,
        )
    ):
        if i >= n_groups:
            break
        if fancy:
            print("------------------------------")
        print(f"{group_name} --> {number_tweets_per_group}")
        if isinstance(group_by, str):
            mask = ds[group_by].values == group_name
        elif isinstance(group_by, xarray.DataArray):
            mask = group_by.values == group_name
        else:
            raise ValueError(f"wrong type group_by: {group_by}")
        if "source" in ds:
            unique_sources = np.unique(ds["source"].loc[mask].values)
            source_to_print = unique_sources[0] if len(unique_sources) else unique_sources
            print(f"source: {source_to_print}")
        ds_sample = a2.dataset.load_dataset.reset_index_coordinate(ds).sel(index=mask)
        index_list = get_sample_indices(
            n,
            n_sample,
            ds_sample.index.shape[0] if ds_sample.index.shape else 0,
        )
        info_text = info_tweets_to_text(
            a2.dataset.load_dataset.reset_index_coordinate(ds_sample).sel(index=index_list),
            fields=fields_to_print,
            fancy=fancy,
        )
        print(info_text)
    return ds_grouped


def get_keywords_default():
    header = (
        "🏔️ OR 🏔️ OR ☀️ OR ☀️ OR 🌞 OR ⛅ OR ⛈️ OR ⛈️ OR 🌤️ OR 🌤️ OR 🌥️ OR 🌥️ OR"
        " 🌦️ OR 🌦️ OR 🌧️ OR 🌧️ OR 🌨️ OR 🌨️ OR 🌩️ OR 🌩️ OR ☔ OR ⛄"
        " OR blizzard OR cloudburst OR downpour OR drizzle OR flash"
        " flood OR flood OR flood stage OR forecast OR freezing rain"
        " OR hail OR ice storm OR lightning OR precipitation OR rain"
        " OR rain gauge OR rain shadow OR rainbands OR rain shower OR"
        " snow OR snow shower OR snowstorm OR sun OR sunny OR thunder"
        " OR thunderstorm"
    )
    keywords = header.split(" OR ")
    return keywords


def dataset_groupby(
    ds: xarray_dataset_type,
    group_by: t.Union[str, xarray_dataarray_type],
    ds_grouped: t.Union[xarray_dataset_type, None] = None,
) -> t.Tuple[xarray_dataset_type, t.Hashable]:
    if ds_grouped is None:
        ds_grouped_unsorted = ds.groupby(group_by).count()
        sort_by = get_variable_name_first(ds_grouped_unsorted)
        ds_grouped = ds_grouped_unsorted.sortby(sort_by, ascending=False)
    else:
        sort_by = get_variable_name_first(ds_grouped)
    return ds_grouped, sort_by


def filter_tweets(ds: xarray_dataset_type, terms: list[str], min_tweets_per_author: int = 0):
    """
    Filter out tweets if include terms

    Tweets including any term are filtered out if its author used
    the term in more tweets than `min_tweets_per_author`.
    Parameters:
    ----------
    ds: dataset
    terms: List of strings with terms.
    min_tweets_per_author:

    Returns
    -------
    filtered dataset
    """
    tweet_id_name = "tweet_id" if "tweet_id" in ds.variables else "id"
    initial_n_tweets = ds["index"].shape[0]
    if "author_id" not in ds.variables.keys():
        raise ValueError("Missing variable 'author_id' in ds!")
    for te in terms:
        where = ds.where(ds.text.str.contains(f"{te}", flags=re.IGNORECASE), drop=True)
        if not where["index"].shape[0]:
            continue
        counts = where.groupby("author_id").count().sortby(tweet_id_name, ascending=False)
        logging.info("------------------------")
        logging.info(
            f"found {np.sum(counts[tweet_id_name].values)} tweets from"
            f" {counts[tweet_id_name].shape[0]} author_ids's with term {te}"
        )
        for author, n in zip(counts["author_id"].astype(int).values, counts[tweet_id_name].values):
            sample = np.random.choice(
                ds["text"].loc[ds.author_id.values == author].values,
                10 if n > 10 else n,
                replace=False,
            )
            logging.info("------------------------")
            logging.info(f"{author} posted {n} tweets with term: {te}")
            logging.info(f"sample: {sample}")
            if n > min_tweets_per_author:
                ds = ds.where(~(ds.author_id == author), drop=True)
    final_n_tweets = ds["index"].shape[0]
    logging.info(f"removed {initial_n_tweets-final_n_tweets} tweets")
    return ds


def print_variables(ds: xarray_dataset_type):
    for k, v in ds.variables.items():
        print(f"{k} --> {v}")


def info_tweets_to_text(ds: xarray_dataset_type, fields: t.Optional[t.Sequence[str]] = None, fancy=False):
    if fields is None:
        fields = [
            "text",
            "latitude_rounded",
            "longitude_rounded",
            "created_at",
            "tp",
            "raining",
        ]
    unique_fields = np.intersect1d(list(set(fields)), list(set(ds.variables.keys())))
    to_print = ""
    for tweet in zip(*[ds[f].values for f in unique_fields]):
        if fancy:
            to_print += "------------------------------\n"
        for label, value in zip(unique_fields, tweet):
            to_print += f"{label}: {value}\n"
    return to_print


def add_precipitation_memory_efficient(
    ds_tweets,
    ds_weather_filenames,
    key_longitude="longitude_rounded",
    key_latitude="latitude_rounded",
    key_time_tweets="time_half",
    key_time_precipitation="time_half",
    key_precipitation_tweets="tp_new",
    key_precipitation_precipitation="tp_h",
):
    if not isinstance(ds_weather_filenames, list):
        ds_weather_filenames = [ds_weather_filenames]
    for filename in ds_weather_filenames:
        ds_precipitation = a2.dataset.load_dataset.load_tweets_dataset(filename, raw=True)
        ds_tweets = add_precipitation_to_tweets(
            ds_tweets,
            ds_precipitation,
            key_longitude=key_longitude,
            key_latitude=key_latitude,
            key_time_tweets=key_time_tweets,
            key_time_precipitation=key_time_precipitation,
            key_precipitation_tweets=key_precipitation_tweets,
            key_precipitation_precipitation=key_precipitation_precipitation,
        )
    return ds_tweets


def add_precipitation_to_tweets(
    ds_tweets,
    ds_precipitation,
    key_longitude="longitude_rounded",
    key_latitude="latitude_rounded",
    key_time_tweets="time_half",
    key_time_precipitation="time_half",
    key_precipitation_tweets="tp_new",
    key_precipitation_precipitation="tp_h",
):
    """
    adds precipitation columns to twitter dataset

    Parameters:
    ----------
    ds_twit: twitter dataset
    ds_prec: precipitation dataset
    key_longitude: name of longitude field in both datasets
    key_latitude: name of latitude field in both datasets
    key_time_tweets: name of time field in Tweets datasets
    key_time_precipitation: name of time field in precipitation datasets
    key_precipitation_tweets: name of precipitation field in Tweets dataset
    key_precipitation_precipitation: name of precipitation field in
                                     precipitation datasets

    Returns
    -------
    twitter dataset with precipitation column added
    """
    a2.utils.testing.assert_presence_variables(ds_tweets, ["longitude", "latitude", "created_at"])
    a2.utils.testing.assert_presence_variables(
        ds_precipitation,
        ["longitude", "latitude", key_precipitation_precipitation],
    )
    if key_precipitation_tweets not in ds_tweets.variables.keys():
        ds_tweets = a2.dataset.utils_dataset.initialize_variable(ds_tweets, key_precipitation_tweets, dtype=object)
    if "time" not in ds_tweets.variables.keys():
        ds_tweets["time"] = (["index"], ds_tweets.created_at.values)
    ds_tweets = add_field(ds_tweets, key_time_tweets, coordinates=["index"])
    ds_tweets = add_field(ds_tweets, key_longitude, coordinates=["index"])
    ds_tweets = add_field(ds_tweets, key_latitude, coordinates=["index"])

    ds_precipitation = add_field(ds_precipitation, key_time_precipitation)
    ds_precipitation = add_field(ds_precipitation, key_longitude, rename_coordinate="longitude")
    ds_precipitation = add_field(ds_precipitation, key_latitude, rename_coordinate="latitude")
    mask = (ds_tweets[key_time_tweets] >= ds_precipitation[key_time_tweets].values.min()) & (
        ds_tweets[key_time_tweets] <= ds_precipitation[key_time_tweets].values.max()
    )
    time = ds_tweets[key_time_tweets].loc[mask]
    longitude = ds_tweets[key_longitude].loc[mask]
    latitude = ds_tweets[key_latitude].loc[mask]
    ds_tweets[key_precipitation_tweets].loc[mask] = ds_precipitation.sel(
        {
            key_longitude: longitude,
            key_latitude: latitude,
            key_time_precipitation: time,
        }
    )[key_precipitation_precipitation].values
    number_nan_values = np.sum(a2.dataset.utils_dataset.is_nan(ds_tweets, key_precipitation_tweets))
    logging.info(f"found {number_nan_values} nan-values in precipitation dataset")
    return ds_tweets


def add_field(
    ds: xarray_dataset_type,
    variable: t.Hashable,
    coordinates: Optional[list] = None,
    overwrite: bool = False,
    rename_coordinate: Optional[str] = None,
):
    if coordinates is None:
        coordinates = list(ds.coords)
    if variable in ds and not overwrite:
        return ds
    if rename_coordinate is not None and not isinstance(rename_coordinate, str):
        raise Exception(f"rename_coordinate: {rename_coordinate} should be field name of " "dataset or None!")
    if variable == "longitude_rounded":
        values = np.round(ds["longitude"].astype(float).values, decimals=1)
    elif variable == "latitude_rounded":
        values = np.round(ds["latitude"].astype(float).values, decimals=1)
    elif variable == "time_half":
        values = pd.to_datetime(ds.time.values + pd.Timedelta("30min")).round("1h") - pd.Timedelta("30min")
    elif variable == "time_h":
        values = pd.to_datetime(ds.time).round("1h").values
    else:
        raise ValueError(f"Variable {variable} not implemented!")

    if rename_coordinate is not None:
        ds = ds.rename({rename_coordinate: variable})
        ds[rename_coordinate] = (
            variable,
            ds[variable].values,
        )
        ds = add_coordinates(ds, variable, values)
    else:
        ds[variable] = (coordinates, values)

    return ds


def add_coordinates(ds: xarray_dataset_type, key: t.Hashable, values: np.ndarray) -> xarray_dataset_type:
    ds[key] = values
    return ds


def add_variable(
    ds: xarray_dataset_type,
    key: t.Hashable,
    values: np.ndarray,
    coordinate: list | None = None,
    type_values: Type | None = None,
) -> xarray_dataset_type:
    if type_values is None:
        type_values = values.dtype
    if _using_xarray():
        if coordinate is None:
            coordinate = ["index"]
        ds[key] = (coordinate, np.array(values, dtype=type_values))
    elif _using_pandas():
        ds[key] = np.array(values, dtype=type_values)
    return ds


def select_rows_by_index(
    ds: xarray_dataset_type,
    indices,
):
    if _using_xarray():
        ds = ds.sel(index=indices)
    elif _using_pandas():
        ds = ds.iloc[indices]
    return ds


def drop_rows(
    ds: xarray_dataset_type,
    condition: np.ndarray,
) -> xarray_dataset_type:
    if _using_xarray():
        ds = ds.where(condition, drop=True)
    elif _using_pandas():
        ds = ds.loc[condition]
    return ds


def initialize_variable(
    ds: xarray_dataset_type,
    field: str,
    coordinates=["index"],
    values=np.nan,
    dtype: type = float,
) -> xarray_dataset_type:
    variable_name_first = get_variable_name_first(ds)
    ds[field] = (
        coordinates,
        np.full(ds[variable_name_first].values.shape[0], values, dtype=dtype),
    )
    return ds


def get_variable_name_first(ds: xarray_dataset_type) -> t.Hashable:
    if _using_xarray():
        first_variable = list(ds.variables.keys())[0]
    elif _using_pandas():
        first_variable = ds.columns[0]
    return first_variable


def array_elements_to_str(array: np.ndarray) -> np.ndarray:
    return np.array(str(x) for x in array)


def assert_keys_in_dataset(ds, keys):
    if _using_xarray():
        variables = ds.variables.keys()
    elif _using_pandas():
        variables = ds.columns
    not_found = [k for k in keys if k not in variables]
    if not not_found:
        return True
    else:
        raise ValueError(f"Couldn't find keys {not_found}!")


def divide_ds_by_unique_values(ds, key_divide_by, keys_values):
    ds = ds.sortby(key_divide_by)
    ds = a2.dataset.load_dataset.reset_index_coordinate(ds)
    _, indices, counts = np.unique(ds[key_divide_by].values.astype(int), return_index=True, return_counts=True)
    index_list = [[i for _ in range(c)] for i, c in zip(indices, counts)]
    divided_values = []
    for k in keys_values:
        divided_values.append(
            [
                [ds[k].values[i + index_inner] for index_inner, i in enumerate(l)]
                for index_outer, l in enumerate(index_list)
            ]
        )
    return ds, divided_values


def construct_dataset(ds, data_vars, time=None):
    coords = ds.coords
    if time is not None:
        coords["time"] = time
    return xarray_dataset_type(data_vars=data_vars, coords=coords)


def merge_datasets_along_index(ds_top: xarray_dataset_type, ds_bottom: xarray_dataset_type) -> xarray_dataset_type:
    ds_bottom_reindexed = ds_bottom.copy()
    ds_top = ds_top.copy()

    ds_top = a2.dataset.load_dataset.reset_index_coordinate(ds_top)
    ds_bottom_reindexed = a2.dataset.load_dataset.reset_index_coordinate(ds_bottom_reindexed)

    start_index = ds_top.index.shape[0]
    ds_bottom_reindexed["index"] = range(start_index, start_index + ds_bottom_reindexed.index.shape[0])
    return xarray.merge([ds_top, ds_bottom_reindexed])
