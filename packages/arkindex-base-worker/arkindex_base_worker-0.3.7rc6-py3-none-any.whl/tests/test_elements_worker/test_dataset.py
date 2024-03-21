import json
import logging

import pytest
from apistar.exceptions import ErrorResponse

from arkindex_worker.models import Dataset
from arkindex_worker.worker.dataset import DatasetState
from tests.conftest import PROCESS_ID
from tests.test_elements_worker import BASE_API_CALLS


def test_list_process_datasets_readonly_error(mock_dataset_worker):
    # Set worker in read_only mode
    mock_dataset_worker.worker_run_id = None
    assert mock_dataset_worker.is_read_only

    with pytest.raises(
        AssertionError, match="This helper is not available in read-only mode."
    ):
        mock_dataset_worker.list_process_datasets()


def test_list_process_datasets_api_error(responses, mock_dataset_worker):
    responses.add(
        responses.GET,
        f"http://testserver/api/v1/process/{PROCESS_ID}/datasets/",
        status=500,
    )

    with pytest.raises(
        Exception, match="Stopping pagination as data will be incomplete"
    ):
        next(mock_dataset_worker.list_process_datasets())

    assert len(responses.calls) == len(BASE_API_CALLS) + 5
    assert [
        (call.request.method, call.request.url) for call in responses.calls
    ] == BASE_API_CALLS + [
        # The API call is retried 5 times
        ("GET", f"http://testserver/api/v1/process/{PROCESS_ID}/datasets/"),
        ("GET", f"http://testserver/api/v1/process/{PROCESS_ID}/datasets/"),
        ("GET", f"http://testserver/api/v1/process/{PROCESS_ID}/datasets/"),
        ("GET", f"http://testserver/api/v1/process/{PROCESS_ID}/datasets/"),
        ("GET", f"http://testserver/api/v1/process/{PROCESS_ID}/datasets/"),
    ]


def test_list_process_datasets(
    responses,
    mock_dataset_worker,
):
    expected_results = [
        {
            "id": "process_dataset_1",
            "dataset": {
                "id": "dataset_1",
                "name": "Dataset 1",
                "description": "My first great dataset",
                "sets": ["train", "val", "test"],
                "state": "open",
                "corpus_id": "corpus_id",
                "creator": "test@teklia.com",
                "task_id": "task_id_1",
            },
            "sets": ["test"],
        },
        {
            "id": "process_dataset_2",
            "dataset": {
                "id": "dataset_2",
                "name": "Dataset 2",
                "description": "My second great dataset",
                "sets": ["train", "val"],
                "state": "complete",
                "corpus_id": "corpus_id",
                "creator": "test@teklia.com",
                "task_id": "task_id_2",
            },
            "sets": ["train", "val"],
        },
        {
            "id": "process_dataset_3",
            "dataset": {
                "id": "dataset_3",
                "name": "Dataset 3 (TRASHME)",
                "description": "My third dataset, in error",
                "sets": ["nonsense", "random set"],
                "state": "error",
                "corpus_id": "corpus_id",
                "creator": "test@teklia.com",
                "task_id": "task_id_3",
            },
            "sets": ["random set"],
        },
    ]
    responses.add(
        responses.GET,
        f"http://testserver/api/v1/process/{PROCESS_ID}/datasets/",
        status=200,
        json={
            "count": 3,
            "next": None,
            "results": expected_results,
        },
    )

    for idx, dataset in enumerate(mock_dataset_worker.list_process_datasets()):
        assert isinstance(dataset, Dataset)
        assert dataset == {
            **expected_results[idx]["dataset"],
            "selected_sets": expected_results[idx]["sets"],
        }

    assert len(responses.calls) == len(BASE_API_CALLS) + 1
    assert [
        (call.request.method, call.request.url) for call in responses.calls
    ] == BASE_API_CALLS + [
        ("GET", f"http://testserver/api/v1/process/{PROCESS_ID}/datasets/"),
    ]


@pytest.mark.parametrize(
    ("payload", "error"),
    [
        # Dataset
        (
            {"dataset": None},
            "dataset shouldn't be null and should be a Dataset",
        ),
        (
            {"dataset": "not Dataset type"},
            "dataset shouldn't be null and should be a Dataset",
        ),
    ],
)
def test_list_dataset_elements_wrong_param_dataset(mock_dataset_worker, payload, error):
    with pytest.raises(AssertionError, match=error):
        mock_dataset_worker.list_dataset_elements(**payload)


@pytest.mark.parametrize(
    "sets",
    [
        ["set_1"],
        ["set_1", "set_2", "set_3"],
        ["set_1", "set_2", "set_3", "set_4"],
    ],
)
def test_list_dataset_elements_api_error(
    responses, mock_dataset_worker, sets, default_dataset
):
    default_dataset.selected_sets = sets
    query_params = (
        "?with_count=true"
        if sets == default_dataset.sets
        else "?set=set_1&with_count=true"
    )
    responses.add(
        responses.GET,
        f"http://testserver/api/v1/datasets/{default_dataset.id}/elements/{query_params}",
        status=500,
    )

    with pytest.raises(
        Exception, match="Stopping pagination as data will be incomplete"
    ):
        next(mock_dataset_worker.list_dataset_elements(dataset=default_dataset))

    assert len(responses.calls) == len(BASE_API_CALLS) + 5
    assert [
        (call.request.method, call.request.url) for call in responses.calls
    ] == BASE_API_CALLS + [
        # The API call is retried 5 times
        (
            "GET",
            f"http://testserver/api/v1/datasets/{default_dataset.id}/elements/{query_params}",
        ),
        (
            "GET",
            f"http://testserver/api/v1/datasets/{default_dataset.id}/elements/{query_params}",
        ),
        (
            "GET",
            f"http://testserver/api/v1/datasets/{default_dataset.id}/elements/{query_params}",
        ),
        (
            "GET",
            f"http://testserver/api/v1/datasets/{default_dataset.id}/elements/{query_params}",
        ),
        (
            "GET",
            f"http://testserver/api/v1/datasets/{default_dataset.id}/elements/{query_params}",
        ),
    ]


@pytest.mark.parametrize(
    "sets",
    [
        ["set_1"],
        ["set_1", "set_2", "set_3"],
        ["set_1", "set_2", "set_3", "set_4"],
    ],
)
def test_list_dataset_elements(
    responses,
    mock_dataset_worker,
    sets,
    default_dataset,
):
    default_dataset.selected_sets = sets

    dataset_elements = []
    for split in default_dataset.sets:
        index = split[-1]
        dataset_elements.append(
            {
                "set": split,
                "element": {
                    "id": str(index) * 4,
                    "type": "page",
                    "name": f"Test {index}",
                    "corpus": {},
                    "thumbnail_url": None,
                    "zone": {},
                    "best_classes": None,
                    "has_children": None,
                    "worker_version_id": None,
                    "worker_run_id": None,
                },
            }
        )
        if split == "set_1":
            dataset_elements.append({**dataset_elements[-1]})
            dataset_elements[-1]["element"]["name"] = f"Test {index} (bis)"

    # All sets are selected, we call the unfiltered endpoint once
    if default_dataset.sets == default_dataset.selected_sets:
        expected_results = dataset_elements
        responses.add(
            responses.GET,
            f"http://testserver/api/v1/datasets/{default_dataset.id}/elements/?with_count=true",
            status=200,
            json={
                "count": len(expected_results),
                "next": None,
                "results": expected_results,
            },
        )
        expected_calls = [
            f"http://testserver/api/v1/datasets/{default_dataset.id}/elements/?with_count=true"
        ]

    # Not all sets are selected, we call the filtered endpoint multiple times, once per set
    else:
        expected_results, expected_calls = [], []
        for selected_set in default_dataset.selected_sets:
            partial_results = [
                element
                for element in dataset_elements
                if element["set"] == selected_set
            ]
            expected_results += partial_results
            responses.add(
                responses.GET,
                f"http://testserver/api/v1/datasets/{default_dataset.id}/elements/?set={selected_set}&with_count=true",
                status=200,
                json={
                    "count": len(partial_results),
                    "next": None,
                    "results": partial_results,
                },
            )
            expected_calls += [
                f"http://testserver/api/v1/datasets/{default_dataset.id}/elements/?set={selected_set}&with_count=true"
            ]

    for idx, element in enumerate(
        mock_dataset_worker.list_dataset_elements(dataset=default_dataset)
    ):
        assert element == (
            expected_results[idx]["set"],
            expected_results[idx]["element"],
        )

    assert len(responses.calls) == len(BASE_API_CALLS) + len(expected_calls)
    assert [
        (call.request.method, call.request.url) for call in responses.calls
    ] == BASE_API_CALLS + [("GET", expected_call) for expected_call in expected_calls]


@pytest.mark.parametrize(
    ("payload", "error"),
    [
        # Dataset
        (
            {"dataset": None},
            "dataset shouldn't be null and should be a Dataset",
        ),
        (
            {"dataset": "not dataset type"},
            "dataset shouldn't be null and should be a Dataset",
        ),
    ],
)
def test_update_dataset_state_wrong_param_dataset(
    mock_dataset_worker, default_dataset, payload, error
):
    api_payload = {
        "dataset": Dataset(**default_dataset),
        "state": DatasetState.Building,
        **payload,
    }

    with pytest.raises(AssertionError, match=error):
        mock_dataset_worker.update_dataset_state(**api_payload)


@pytest.mark.parametrize(
    ("payload", "error"),
    [
        # DatasetState
        (
            {"state": None},
            "state shouldn't be null and should be a str from DatasetState",
        ),
        (
            {"state": "not dataset type"},
            "state shouldn't be null and should be a str from DatasetState",
        ),
    ],
)
def test_update_dataset_state_wrong_param_state(
    mock_dataset_worker, default_dataset, payload, error
):
    api_payload = {
        "dataset": Dataset(**default_dataset),
        "state": DatasetState.Building,
        **payload,
    }

    with pytest.raises(AssertionError, match=error):
        mock_dataset_worker.update_dataset_state(**api_payload)


def test_update_dataset_state_readonly_error(
    caplog, mock_dev_dataset_worker, default_dataset
):
    api_payload = {
        "dataset": Dataset(**default_dataset),
        "state": DatasetState.Building,
    }

    assert not mock_dev_dataset_worker.update_dataset_state(**api_payload)
    assert [(level, message) for _, level, message in caplog.record_tuples] == [
        (
            logging.WARNING,
            "Cannot update dataset as this worker is in read-only mode",
        ),
    ]


def test_update_dataset_state_api_error(
    responses, mock_dataset_worker, default_dataset
):
    responses.add(
        responses.PATCH,
        f"http://testserver/api/v1/datasets/{default_dataset.id}/",
        status=500,
    )

    with pytest.raises(ErrorResponse):
        mock_dataset_worker.update_dataset_state(
            dataset=default_dataset,
            state=DatasetState.Building,
        )

    assert len(responses.calls) == len(BASE_API_CALLS) + 5
    assert [
        (call.request.method, call.request.url) for call in responses.calls
    ] == BASE_API_CALLS + [
        # We retry 5 times the API call
        ("PATCH", f"http://testserver/api/v1/datasets/{default_dataset.id}/"),
        ("PATCH", f"http://testserver/api/v1/datasets/{default_dataset.id}/"),
        ("PATCH", f"http://testserver/api/v1/datasets/{default_dataset.id}/"),
        ("PATCH", f"http://testserver/api/v1/datasets/{default_dataset.id}/"),
        ("PATCH", f"http://testserver/api/v1/datasets/{default_dataset.id}/"),
    ]


def test_update_dataset_state(
    responses,
    mock_dataset_worker,
    default_dataset,
):
    dataset_response = {
        "name": "My dataset",
        "description": "A super dataset built by me",
        "sets": ["set_1", "set_2", "set_3"],
        "state": DatasetState.Building.value,
    }
    responses.add(
        responses.PATCH,
        f"http://testserver/api/v1/datasets/{default_dataset.id}/",
        status=200,
        json=dataset_response,
    )

    updated_dataset = mock_dataset_worker.update_dataset_state(
        dataset=default_dataset,
        state=DatasetState.Building,
    )

    assert len(responses.calls) == len(BASE_API_CALLS) + 1
    assert [
        (call.request.method, call.request.url) for call in responses.calls
    ] == BASE_API_CALLS + [
        (
            "PATCH",
            f"http://testserver/api/v1/datasets/{default_dataset.id}/",
        ),
    ]
    assert json.loads(responses.calls[-1].request.body) == {
        "state": DatasetState.Building.value
    }
    assert updated_dataset == Dataset(**{**default_dataset, **dataset_response})
