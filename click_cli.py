import click
from utils import *
@click.command()
@click.option('id', type=int, default=1)
@click.option('--path', type=str, default='sample_data/sample_data_1.csv')
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
            click.echo(f'id \t{id} \t file name\t{file} \n')
    if excel and id:
        print(export_to_excel(int(id)))