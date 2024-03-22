import json
from typing import Optional, Tuple, Union

import click
from click.core import Context as ClickContext
from gable.client import GableClient
from gable.helpers.check import CheckDataAssetDetailedResponseUnion
from gable.helpers.data_asset import (
    gather_pyspark_asset_data,
    get_abs_project_root_path,
)
from gable.helpers.emoji import EMOJI
from gable.helpers.repo_interactions import get_git_repo_info
from gable.helpers.shell_output import shell_linkify
from gable.openapi import (
    CheckComplianceDataAssetsPySparkRequest,
    CheckDataAssetCommentMarkdownResponse,
    ErrorResponse,
    ErrorResponseDeprecated,
    IngestDataAssetResponse,
    PySparkAsset,
    RegisterDataAssetPySparkRequest,
    ResponseType,
)
from loguru import logger


def register_pyspark_data_asset(
    ctx: ClickContext,
    spark_job_entrypoint: str,
    project_root: str,
    connection_string: Optional[str],
    csv_schema_file: Optional[str],
    dry_run: bool,
) -> Tuple[Union[IngestDataAssetResponse, ErrorResponseDeprecated], bool, int]:
    git_ssh_repo, sca_results_dict = gather_pyspark_asset_data(
        get_abs_project_root_path(project_root),
        spark_job_entrypoint,
        csv_schema_file,
        connection_string,
        ctx.obj.client,
    )
    if sca_results_dict is {}:
        raise click.ClickException(
            f"{EMOJI.RED_X.value} No data assets found to register! You can use the --debug or --trace flags for more details.",
        )
    logger.info(
        f"{EMOJI.GREEN_CHECK.value} Pyspark data asset(s) found:\n{json.dumps(sca_results_dict, indent=4)}"
    )
    assets = [
        PySparkAsset(
            schema=event_schema,
            git_host=git_ssh_repo,
            project_name=project_root,
            spark_entrypoint=spark_job_entrypoint,
            spark_table=event_name,
        )
        for event_name, event_schema in sca_results_dict.items()
    ]
    request = RegisterDataAssetPySparkRequest(
        dry_run=dry_run,
        assets=assets,
    )
    # click doesn't let us specify the type of ctx.obj.client in the Context:
    client: GableClient = ctx.obj.client
    return client.post_data_asset_register_pyspark(request)


def check_compliance_pyspark_data_asset(
    ctx: ClickContext,
    spark_job_entrypoint: str,
    project_root: str,
    connection_string: Optional[str],
    csv_schema_file: Optional[str],
    response_type: ResponseType,
) -> Union[
    ErrorResponse,
    CheckDataAssetCommentMarkdownResponse,
    list[CheckDataAssetDetailedResponseUnion],
]:
    git_ssh_repo, sca_results_dict = gather_pyspark_asset_data(
        get_abs_project_root_path(project_root),
        spark_job_entrypoint,
        csv_schema_file,
        connection_string,
        ctx.obj.client,
    )
    if sca_results_dict is {}:
        raise click.ClickException(
            f"{EMOJI.RED_X.value} No data assets found to register! You can use the --debug or --trace flags for more details.",
        )
    assets = [
        PySparkAsset(
            schema=event_schema,
            git_host=git_ssh_repo,
            project_name=project_root,
            spark_entrypoint=spark_job_entrypoint,
            spark_table=event_name,
        )
        for event_name, event_schema in sca_results_dict.items()
    ]
    request = CheckComplianceDataAssetsPySparkRequest(
        assets=assets, responseType=response_type
    )
    # click doesn't let us specify the type of ctx.obj.client in the Context:
    client: GableClient = ctx.obj.client
    return client.post_check_compliance_data_assets_pyspark(request)
