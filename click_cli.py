#!/usr/bin/python3
import click
from utils import *
@click.command()
@click.option('--id', type=int, default=0)
@click.option('--path', type=str)
@click.option('--excel', help='Export dataset by  given id to excel', is_flag=True)
@click.option('--pdf', help='Export dataset by given id to pdf', is_flag=True)
@click.option('--delete', help='Delete dataset by given id', is_flag=True)
@click.option('--describe', help='Describe dataset by given id', is_flag=True)
@click.option('--stats', help='Give stats of dataset by given id ', is_flag=True)
@click.option('--list', help='Show available datasets', is_flag=True)

def cli_app(id=None, path=None, excel=None, pdf=None,
            delete=None, describe=None, stats=None, list=None):
    
    if list:
        list_datasets()
        for id, file in enumerate(list_datasets()):
            click.echo(f'id-> \t{id} \t file name->\t{file} \n')
    if excel and id is not None:
        click.echo(export_to_excel(int(id)))
    if pdf and id is not None:
        click.secho(export_to_pdf(int(id)), fg='green')
    if describe and id is not None:
        click.echo(describe_dataset(int(id)))
    if stats and id is not None:
        click.echo(single_dataset(int(id)))
    if delete and id is not None:
        click.secho(delete_dataset(int(id)), fg='blue')
    if path:
        click.secho(upload_dataset(path),fg='green')

if __name__ == '__main__':
    cli_app()