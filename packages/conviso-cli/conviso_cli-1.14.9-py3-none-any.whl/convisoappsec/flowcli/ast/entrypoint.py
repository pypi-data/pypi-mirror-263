from copy import deepcopy as clone

import click
import git
from convisoappsec.flowcli import help_option
from convisoappsec.flowcli.common import CreateDeployException, DeployFormatter, PerformDeployException, project_code_option, asset_id_option
from convisoappsec.flowcli.deploy.create.context import pass_create_context
from convisoappsec.flowcli.deploy.create.with_.values import values
from convisoappsec.flowcli.requirements_verifier import RequirementsVerifier
from convisoappsec.flowcli.sast import sast
from convisoappsec.flowcli.sca import sca
from convisoappsec.logger import LOGGER


def get_default_params_values(cmd_params):
    """ Further information in https://click.palletsprojects.com/en/8.1.x/api/?highlight=params#click.Command.params

    Args:
        cmd_params (List[click.core.Parameter]):

    Returns:
        dict: default params values dictionarie
    """
    default_params = {}
    for param in cmd_params:
        unwanted = param.name in ['help', 'verbosity']
        if not unwanted:
            default_params.update({param.name: param.default})
    return default_params


def parse_params(ctx_params: dict, expected_params: list):
    """ Parse the params from the context extracting the expected params values to the context.

    Args:
        ctx_params (dict): context params: Further information at https://click.palletsprojects.com/en/8.1.x/api/?highlight=context%20param#click.Context.params
        expected_params (list): Further information at https://click.palletsprojects.com/en/8.1.x/api/?highlight=params#click.Command.params

    Returns:
        dict: parsed_params: parsed params as key and value
    """
    parsed_params = get_default_params_values(expected_params)
    for param in ctx_params:
        if param in parsed_params:
            parsed_params.update({param: ctx_params.get(param)})
    return parsed_params


def perform_sast(context) -> None:
    """Setup and runs the "sast run" command.

    Args:
        context (<class 'click.core.Context'>): clonned context
    """
    sast_run = sast.commands.get('run')

    specific_params = {
        "deploy_id": context.obj.deploy['id'],
        "start_commit": context.obj.deploy['previous_commit'],
        "end_commit": context.obj.deploy['current_commit'],
    }
    context.params.update(specific_params)
    context.params = parse_params(context.params, sast_run.params)
    try:
        LOGGER.info(
            'Running SAST on deploy ID "{deploy_id}"'
            .format(deploy_id=context.params["deploy_id"])
        )
        sast_run.invoke(context)

    except Exception as err:
        raise click.ClickException(str(err)) from err


def perform_sca(context) -> None:
    """Setup and runs the "sca run" command.

    Args:
        context (<class 'click.core.Context'>): clonned context
    """
    sca_run = sca.commands.get('run')
    context.params.update({"deploy_id": context.obj.deploy['id']})
    context.params = parse_params(context.params, sca_run.params)
    try:
        LOGGER.info(
            'Running SCA on deploy ID "{deploy_id}"'
            .format(deploy_id=context.params["deploy_id"])
        )
        sca_run.invoke(context)

    except Exception as err:
        raise click.ClickException(str(err)) from err


def validate_git_repo(context):
    """
    Validates the repository to ensure that it will not lose the git history reference.

    Args:
        context (<class 'click.core.Context'>)

    Returns:
        context object
    """
    repository_dir = context.params['repository_dir']
    previous_commit = context.params['previous_commit']

    repo = git.Repo(repository_dir)
    commits = list(repo.iter_commits())
    previous_commit_is_in_commits = any(commit.hexsha == previous_commit for commit in commits)
    if previous_commit_is_in_commits:
        return

    merge_commits = [commit for commit in commits if len(commit.parents) > 1]

    if merge_commits:
        # get first commit from the last merge to ensure nothing will be lost when the scans run.
        last_merge_commit = merge_commits[-1]
        first_parent_commit = last_merge_commit.parents[0]
        context.params['previous_commit'] = first_parent_commit.hexsha

    # But we won't always have the first commit of a merge,
    # If that happens there's nothing to do but get the commit right below the head
    second_latest_commit = commits[1]
    context.params['previous_commit'] = second_latest_commit.hexsha

    return


def perform_deploy(context):
    """Setup and runs the "deploy create with values" command.

    Args:
        context (<class 'click.core.Context'>): clonned context

    Returns:
        dict: deploy
         int: deploy.id
         int: deploy.project_id
         str: deploy.current_tag
         str: deploy.previous_tag
         str: deploy.current_commit
         str: deploy.previous_commit
         str: deploy.created_at
    """
    context.obj.output_formatter = DeployFormatter(
        format=DeployFormatter.DEFAULT
    )
    context.params = parse_params(context.params, values.params)
    try:
        LOGGER.info("Creating new deploy ...")
        validate_git_repo(context)
        created_deploy = values.invoke(context)

        if created_deploy:
            return created_deploy

        raise CreateDeployException("Deploy not created.")

    except CreateDeployException as err:
        raise PerformDeployException(err)

    except Exception as err:
        raise click.ClickException(str(err)) from err

@click.command(
    context_settings=dict(
        allow_extra_args=True,
        ignore_unknown_options=True
    )
)
@asset_id_option(
    required=False
)
@project_code_option(
    help="Not required when --no-send-to-flow option is set",
    required=False
)
@click.option(
    "--send-to-flow/--no-send-to-flow",
    default=True,
    show_default=True,
    required=False,
    help="""Enable or disable the ability of send analysis result
    reports to flow. When --send-to-flow option is set the --project-code
    option is required""",
    hidden=True
)
@click.option(
    '-r',
    '--repository-dir',
    default=".",
    show_default=True,
    type=click.Path(exists=True, resolve_path=True),
    required=False,
    help="""The source code repository directory.""",
)
@click.option(
    "-c",
    "--current-commit",
    required=False,
    help="If no value is given the HEAD commit of branch is used. [DEPLOY]",
)
@click.option(
    "-p",
    "--previous-commit",
    required=False,
    help="""If no value is given, the value is retrieved from the lastest
    deploy at flow application. [DEPLOY]""",
)
@click.option(
    "--company-id",
    required=False,
    envvar=("CONVISO_COMPANY_ID", "FLOW_COMPANY_ID"),
    help="Company ID on Conviso Platform",
)
@click.option(
    '--asset-name',
    required=False,
    envvar=("CONVISO_ASSET_NAME", "FLOW_ASSET_NAME"),
    help="Provides a asset name.",
)
@click.option(
    '--vulnerability-auto-close',
    default=False,
    is_flag=True,
    hidden=True,
    help="Enable auto fixing vulnerabilities on cp.",
)
@help_option
@pass_create_context
@click.pass_context
def run(context, create_context, **kwargs):
    """ AST - Application Security Testing. Unifies deploy issue, SAST and SCA analyses.  """
    try:
        prepared_context = RequirementsVerifier.prepare_context(clone(context), from_ast=True)
        prepared_context.obj.deploy = perform_deploy(clone(prepared_context))
        perform_sast(clone(prepared_context))
        perform_sca(clone(prepared_context))

    except PerformDeployException as err:
        LOGGER.warning(err)

    except Exception as err:
        raise click.ClickException(str(err)) from err


@click.group()
def ast():
    pass


ast.add_command(run)
