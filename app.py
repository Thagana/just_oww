import os
import click
from view_creator.view_creator import View

@click.command()
@click.option("--name", help="Create a component with the specified name")
@click.option("--directory", help="This creates a component from the specified directory")
@click.option("-d", help="This creates a component from the specified directory")
@click.argument('name')
def component(name: str, directory: str, d: str):
    # Base component directory
    component_dir = './src/components'
    if not os.path.exists(component_dir):
        os.makedirs(component_dir, mode = 0o777)

    if directory:
        component_dir = directory

    if d:
        component_dir = d 
    
    # Create a directory for the component
    if not os.path.exists(name):
        os.makedirs(component_dir + '/' + name)

    with open(f"{component_dir}/{name}/{name}.tsx", 'w') as fh:
        fh.write(View.generate_jsx_view_str(name))
    with open(f"{component_dir}/{name}/{name}.scss", "w") as fh:
        fh.write("")
    with open(f"{component_dir}/{name}/index.ts", "w") as fh:
        fh.write(View.generate_index_file(name))

@click.group()
def cli():
    pass


cli.add_command(component)

if __name__ == "__main__":
    cli()
