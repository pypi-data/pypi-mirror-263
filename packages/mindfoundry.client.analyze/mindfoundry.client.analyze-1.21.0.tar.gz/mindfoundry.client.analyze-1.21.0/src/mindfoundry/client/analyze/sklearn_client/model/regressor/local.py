from typing import List, Optional

import attr

from ....swagger.api.models import create_regression_model
from ....swagger.models import (
    CreateRegressionRequest,
    DataPartitionMethod,
    ModelValidationMethod,
    NlpLanguage,
    RegressionModelType,
    RegressionScorers,
    TargetDistributions,
)
from ....swagger.types import UNSET
from ....utils import check_response
from ...connection import ConnectionLike, client_from_connectionlike
from ...data_set import DataLike, get_dataset_from_datalike
from ..shared import BaseModel, LocalModel, RemoteModel


@attr.s(auto_attribs=True)
class InitialConfig:
    scorer: RegressionScorers
    model_validation_method: ModelValidationMethod
    name: str
    description: Optional[str]
    number_of_evaluations: int
    nlp_language: NlpLanguage
    draft_mode: bool
    run_data_processing: bool
    model_types: Optional[List[RegressionModelType]]
    target_distribution: Optional[TargetDistributions]


class LocalRegressor(LocalModel):
    """
    A regressor that has not yet been saved to Analyze (and thus hasn't been fitted)
    """

    def __init__(
        self,
        connection: ConnectionLike,
        initial_config: InitialConfig,
    ):
        self._connection = connection
        self._client = client_from_connectionlike(connection)
        self._initial_config = initial_config

    def fit(
        self,
        data: DataLike,
        target: str,
        excluded_columns: Optional[List[str]] = None,
        *,
        # Regression specific fit parameters
        sample_weight: Optional[str] = None,
        order_by: Optional[str] = None,
        partition_by: Optional[str] = None,
        hold_out_percentage: Optional[float] = 10.0,
        no_mixing: Optional[List[str]] = None,
    ) -> BaseModel:
        # data_partition_method - determine based on whether there are orderby/partitionby/nomixing names
        if not order_by is None:
            data_partition_method = DataPartitionMethod.ORDERED
        elif not partition_by is None:
            data_partition_method = DataPartitionMethod.MANUAL
        elif not no_mixing is None:
            data_partition_method = DataPartitionMethod.NO_MIXING
        else:
            data_partition_method = DataPartitionMethod.RANDOM

        data_set = get_dataset_from_datalike(data, connection=self._connection)

        payload = CreateRegressionRequest(
            name=self._initial_config.name,
            data_set_id=data_set.data_set_id,
            target_distribution=self._initial_config.target_distribution or UNSET,
            target_column=target,
            score_to_optimize=self._initial_config.scorer,
            model_validation_method=self._initial_config.model_validation_method,
            data_partition_method=data_partition_method,
            hold_out_percentage=hold_out_percentage or UNSET,
            number_of_evaluations=self._initial_config.number_of_evaluations,
            description=self._initial_config.description or UNSET,
            excluded_columns=excluded_columns or UNSET,
            nlp_language=self._initial_config.nlp_language,
            draft_mode=self._initial_config.draft_mode,
            data_processing=self._initial_config.run_data_processing,
            no_mixing_columns=no_mixing or UNSET,
            partition_column=partition_by or UNSET,
            order_by_column=order_by or UNSET,
            weight_column=sample_weight or UNSET,
            model_types=self._initial_config.model_types or UNSET,
        )

        model_id = check_response(
            create_regression_model.sync_detailed(
                client=self._client, json_body=payload
            )
        ).id
        return RemoteModel(self._connection, model_id)
