from pathlib import Path

import typer
from amsdal.migration.file_migration_generator import FileMigrationGenerator
from amsdal.migration.schemas_loaders import JsonClassSchemaLoader
from rich import print

from amsdal_cli.commands.generate.enums import SOURCES_DIR
from amsdal_cli.commands.migrations.app import sub_app
from amsdal_cli.commands.migrations.constants import MIGRATIONS_DIR_NAME
from amsdal_cli.utils.cli_config import CliConfig


@sub_app.command(name='init')
def initialize(
    ctx: typer.Context,
) -> None:
    """
    Create initial migration files for the project.
    """
    cli_config: CliConfig = ctx.meta['config']
    app_source_path = cli_config.app_directory / SOURCES_DIR

    schema_loader = JsonClassSchemaLoader(app_source_path / 'models')

    migrations_dir: Path = cli_config.app_directory / SOURCES_DIR / MIGRATIONS_DIR_NAME
    generator = FileMigrationGenerator(
        schema_loader=schema_loader,
        app_migrations_path=migrations_dir,
    )

    try:
        generator.init_migrations()
    except RuntimeError as err:
        print(f'[yellow]{err}[/yellow]')
