import json
import logging
import os
import pathlib

import click
import dotenv
import fabric
import npc_lims

# import numpy as np
# from np_upload_validation import checksum, hpc, npc, timing_data, validation
from np_upload_validation import checksum, hpc, npc, validation

dotenv.load_dotenv()


logger = logging.getLogger(__name__)


@click.group()
@click.option("--debug/--no-debug", default=False)
def cli(debug: bool) -> None:
    click.echo(f"Debug mode is {'on' if debug else 'off'}")
    if debug:
        validation.logger.setLevel(logging.DEBUG)
        checksum.logger.setLevel(logging.DEBUG)
        hpc.logger.setLevel(logging.DEBUG)
        npc.logger.setLevel(logging.DEBUG)
        logger.setLevel(logging.DEBUG)


@cli.command()
@click.argument(
    "session_id",
    type=str,
)
@click.option(
    "--chunk-size",
    type=int,
    default=1000,
)
def validate_npc_session(
    session_id: str,
    chunk_size: int,
) -> None:
    # result = validation.validate_npc_session(
    #     session_id,
    #     chunk_size,
    # )
    # report = json.dumps(
    #     [validation_result.model_dump() for validation_result in result],
    #     indent=4,
    #     sort_keys=True,
    # )

    # if stdout:
    #     click.echo(report)
    # else:
    #     pathlib.Path(str(output_path)).write_text(report)
    for result in validation.validate_npc_session(
        session_id,
        chunk_size,
    ):
        try:
            click.echo(result.model_dump())
        except Exception as e:
            click.echo(message=f"Failed to validate: {e}", err=True)


# def _run_npc_session_validation_hpc(
#     session_id: str,
#     chunk_size: int,
#     memsize: int,
# ) -> tuple[str, str]:
#     username = os.environ["HPC_USERNAME"]
#     with fabric.Connection(
#         os.environ["HPC_HOST"],
#         user=username,
#         connect_kwargs={
#             "password": os.environ["HPC_PASSWORD"],
#         },
#     ) as con:
#         user_dir = f"/home/{username}"
#         return hpc.run_hpc_job(
#             con,
#             hpc.HPCJob(
#                 email_address=os.environ["HPC_EMAIL_ADDRESS"],
#                 entry_point=f"np-upload-validation --debug validate-npc-session {session_id} --chunk-size={chunk_size}",
#                 mem_size=memsize,
#             ),
#             f"{user_dir}/jobs",
#             f"{user_dir}/job-logs",
#             hpc.SIFContext(
#                 sif_loc_str=os.environ["HPC_SIF_PATH"],
#                 env_vars={
#                     "CODE_OCEAN_API_TOKEN": os.environ["CODE_OCEAN_API_TOKEN"],
#                     "CODE_OCEAN_DOMAIN": os.environ["CODE_OCEAN_DOMAIN"],
#                     "AWS_ACCESS_KEY_ID": os.environ["AWS_ACCESS_KEY_ID"],
#                     "AWS_SECRET_ACCESS_KEY": os.environ["AWS_SECRET_ACCESS_KEY"],
#                     "AWS_DEFAULT_REGION": os.environ["AWS_DEFAULT_REGION"],
#                 },
#             ),
#             "npc_cleanup",
#         )


def _trigger_hpc_job(
    entry_point: str,
    memsize: int,
) -> tuple[str, str]:
    username = os.environ["HPC_USERNAME"]
    with fabric.Connection(
        os.environ["HPC_HOST"],
        user=username,
        connect_kwargs={
            "password": os.environ["HPC_PASSWORD"],
        },
    ) as con:
        user_dir = f"/home/{username}"
        return hpc.run_hpc_job(
            con,
            hpc.HPCJob(
                email_address=os.environ["HPC_EMAIL_ADDRESS"],
                entry_point=entry_point,
                mem_size=memsize,
            ),
            f"{user_dir}/jobs",
            f"{user_dir}/job-logs",
            hpc.SIFContext(
                sif_loc_str=os.environ["HPC_SIF_PATH"],
                env_vars={
                    "CODE_OCEAN_API_TOKEN": os.environ["CODE_OCEAN_API_TOKEN"],
                    "CODE_OCEAN_DOMAIN": os.environ["CODE_OCEAN_DOMAIN"],
                    "AWS_ACCESS_KEY_ID": os.environ["AWS_ACCESS_KEY_ID"],
                    "AWS_SECRET_ACCESS_KEY": os.environ["AWS_SECRET_ACCESS_KEY"],
                    "AWS_DEFAULT_REGION": os.environ["AWS_DEFAULT_REGION"],
                },
            ),
            "npc_cleanup",
        )


@cli.command()
@click.argument(
    "session_id",
    type=str,
)
@click.option(
    "--chunk-size",
    type=int,
    default=1000,
)
@click.option(
    "--memsize",
    type=int,
    default=20,
)
def validate_npc_session_hpc(session_id: str, chunk_size: int, memsize: int) -> None:
    slurm_id, job_name = _trigger_hpc_job(
        (
            f"np-upload-validation --debug validate-npc-session {session_id} "
            f"--chunk-size={chunk_size}"
        ),
        memsize,
    )
    click.echo(f"Submitted job: {slurm_id} ({job_name})")


@cli.command()
@click.argument(
    "job_name",
    type=str,
)
def get_job_log(job_name: str) -> None:
    username = os.environ["HPC_USERNAME"]
    with fabric.Connection(
        os.environ["HPC_HOST"],
        user=username,
        connect_kwargs={
            "password": os.environ["HPC_PASSWORD"],
        },
    ) as con:
        user_dir = f"/home/{username}"
        log_content = hpc.get_remote_content(
            con,
            f"{user_dir}/job-logs/{job_name}.log",
        )
        click.echo(log_content)


__INTERNAL_JOB_LIMIT = 10  # not easy to parametrize to avoid spamming hpc too fast


@cli.command()
@click.argument(
    "validated_path",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        writable=True,
    ),
    default="np-upload-validation_validated.json",
)
@click.option(
    "--chunk-size",
    type=int,
    default=1000,
)
@click.option(
    "--memsize",
    type=int,
    default=20,
)
def batch_validate_npc_sessions(
    validated_path: click.Path, chunk_size: int, memsize: int
) -> None:
    if validated_path.exists:
        click.echo(f"Reading validated from {validated_path}")
        validated = json.loads(pathlib.Path(str(validated_path)).read_text())
    else:
        validated = {}

    for idx, info in enumerate(npc_lims.get_session_info()):
        if idx > __INTERNAL_JOB_LIMIT:
            click.echo(f"Reached job limit of {__INTERNAL_JOB_LIMIT}. Exiting.")
            break
        if not info.is_ephys:
            continue
        if not info.is_uploaded:
            continue

        if info.id in validated:
            click.echo(f"Skipping {info.id} as it is already validated.")
            continue

        slurm_id, job_name = _trigger_hpc_job(
            (
                f"np-upload-validation --debug validate-npc-session"
                f" {info.id} --chunk-size={chunk_size}"
            ),
            memsize,
        )
        validated[info.id] = {
            "slurm_id": slurm_id,
            "job_name": job_name,
        }
        click.echo(f"Submitted job: {slurm_id} ({job_name})")

    click.echo(f"Writing validated to {validated_path}")
    pathlib.Path(str(validated_path)).write_text(
        json.dumps(validated, indent=4, sort_keys=True)
    )


# @cli.command()
# @click.argument(
#     "raw_path",
#     type=pathlib.Path,
# )
# @click.argument(
#     "output_dir",
#     type=pathlib.Path,
# )
# @click.argument(
#     "channel_index",
#     type=int,
# )
# def memoize_raw_medians(
#     raw_path: pathlib.Path,
#     output_dir: pathlib.Path,
#     channel_index: int,
# ) -> None:
#     data = timing_data.timing_data_from_dat(raw_path.as_posix())
#     median = np.median(data.data[:, channel_index], axis=0)
#     np.save(output_dir / f"{channel_index}.npy", median)


# @cli.command()
# @click.argument(
#     "session_id",
#     type=str,
# )
# def batch_memorize_raw_medians(session_id: str) -> None:
#     pass


@cli.command()
@click.argument(
    "validated_path",
    type=click.Path(
        exists=False,
        file_okay=True,
        dir_okay=False,
        writable=True,
    ),
    default="np-upload-validation_validated.json",
)
@click.option(
    "--memsize",
    type=int,
    default=20,
)
def hpc_validate_arrays(validated_path, memsize) -> None:
    username = os.environ["HPC_USERNAME"]
    slurm_id, job_name = _trigger_hpc_job(
        (
            f"np-upload-validation --debug validate-array-shapes"
            f" {username} {pathlib.Path(validated_path).name}"
        ),
        memsize,
    )
    click.echo(f"Submitted job: {slurm_id} ({job_name})")


@cli.command()
@click.argument(
    "username",
    type=str,
)
@click.argument(
    "validated_path",
    type=click.Path(
        exists=False,
        file_okay=True,
        dir_okay=False,
        writable=True,
    ),
    default="np-upload-validation_validated.json",
)
def validate_array_shapes(username, validated_path) -> None:
    validated = []
    for info in npc_lims.get_session_info():
        if not info.is_ephys:
            continue
        if not info.is_uploaded:
            continue
        click.echo(f"Validating {info.id}")
        try:
            for isilon_data, s3_data in npc.generate_timing_data(info.id):
                try:
                    validated.append(
                        {
                            "id": info.id,
                            "isilon": [
                                {
                                    "path": str(d.path),
                                    "shape": d.data.shape,
                                    "dtype": str(d.data.dtype),
                                }
                                for d in isilon_data
                            ],
                            "s3": {
                                "path": str(s3_data.path),
                                "shape": s3_data.data.shape,
                                "dtype": str(s3_data.data.dtype),
                            },
                        }
                    )
                except Exception:
                    logger.debug(
                        (f"Error validating session: {info.id}"),
                        exc_info=True,
                    )
        except Exception:
            logger.debug(f"Error validating session: {info.id}", exc_info=True)

    output_path = f"/home/{username}/jobs/{pathlib.Path(validated_path).name}"
    click.echo(f"Writing validated to {output_path}")
    pathlib.Path(output_path).write_text(
        json.dumps(validated, indent=4, sort_keys=True)
    )


if __name__ == "__main__":
    cli()
