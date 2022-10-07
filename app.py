import os
import click
from view_creator.view_creator import View


component_dir = './src/components'
views_dir = './src/views'

@click.command()
@click.option("--name", help="Create a component with the specified name")
@click.option("--directory", help="This creates a component from the specified directory")
@click.option("--d", help="This creates a component from the specified directory")
@click.argument('name')
def create_component(name: str, directory: str, d: str):
    if not os.path.exists(component_dir):
        os.makedirs(component_dir, mode = 0o777)

    # Create a directory for the component
    if not os.path.exists(name):
        os.makedirs(component_dir + '/' + name)

    with open(f"{component_dir}/{name}/{name}.tsx", 'w') as fh:
        fh.write(View.generate_jsx_view_str(name))
    with open(f"{component_dir}/{name}/{name}.scss", "w") as fh:
        fh.write("")
    with open(f"{component_dir}/{name}/index.ts", "w") as fh:
        fh.write(View.generate_index_file(name))


@click.command()
@click.option("--name", help="The name of your view")
@click.option("--directory", help="The directory were you want your views")
@click.option("--d", help="The directory were you want your views")
@click.argument('name')
def create_view(name: str, directory: str, d: str):

    if not os.path.exists(views_dir):
        os.makedirs(views_dir, mode = 0o777)

    # Create a directory for the view
    if not os.path.exists(name):
        os.makedirs(views_dir + '/' + name)

    with open(f"{views_dir}/{name}/{name}.tsx", 'w') as fh:
        fh.write(View.generate_jsx_view_str(name))
    with open(f"{views_dir}/{name}/{name}.scss", "w") as fh:
        fh.write("")
    with open(f"{views_dir}/{name}/index.ts", "w") as fh:
        fh.write(View.generate_index_file(name))

@click.group()
def cli():
    pass


cli.add_command(create_component)
cli.add_command(create_view)

if __name__ == "__main__":
    cli()
