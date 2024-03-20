import click
import datetime
from .main import document_hash, embed_signature

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    pass

@cli.command()
@click.option('-i', '--input_file', type=str, help='File input', required=True)
@click.option('-r', '--reason', type=str, help='Reason', required=True)
@click.option('-e', '--email', type=str, help='Email', required=True)
@click.option('-z', '--zeros', type=str, help='Zeros')
@click.option('-zf', '--zeros_file', type=str, help='Zeros file', default = None)
@click.option('-a', '--aligned', type=int, help='Aligned', default=0)
def hash(input_file, email, reason, zeros, zeros_file, aligned):
    """Hash document to sign"""
    logo = """
    +------------------------+
    | Testing for paperlogic |
    +------------------------+
    """

    date = datetime.datetime.utcnow()
    date = date.strftime("D:%Y%m%d%H%M%S+00'00'")

    udct = {
        'sigflags': 3,
        'contact': email,
        'reason': reason,
        # 'signaturebox': (0, 0, 0, 0),  # Invisible signature
        "signingdate": date,
    }

    if not zeros and zeros_file:
        zeros = open(zeros_file, 'r').read()

    document_hashed, datas = document_hash(
        input_file, 
        udct, 
        algomd='sha256', 
        aligned=int(aligned), 
        zeros=zeros.encode()
    )

    document_hashed_file = "document_hashed.txt"
    with open(document_hashed_file, 'w') as f:
        f.write(document_hashed)
    click.echo(f"Document hashed file: {document_hashed_file}")

    datas_file = "datas.txt"
    with open(datas_file, 'wb') as f:
        f.write(datas)
    click.echo(f"Data signature file: {datas_file}")
    
    click.echo(logo)

@cli.command()
@click.option('-i', '--input_file', type=str, help='File input', required=True)
@click.option('-o', '--output_file', type=str, help='File output', required=True)
@click.option('-z', '--zeros', type=str, help='Zeros')
@click.option('-zf', '--zeros_file', type=str, help='Zeros file', default = None)
@click.option('-a', '--aligned', type=int, help='Aligned', default=0)
@click.option('-c', '--contents', type=str, help='Contents')
@click.option('-cf', '--contents_file', type=str, help='Contents file', default = None)
@click.option('-s', '--datas_file', type=str, help='Data signature file', required=True)
def sign(input_file, output_file, zeros, zeros_file, aligned, contents, contents_file, datas_file):
    """Embed signature contents to document"""
    logo = """
    +------------------------+
    | Testing for paperlogic |
    +------------------------+
    """

    if not zeros and zeros_file:
        zeros = open(zeros_file, 'rb').read()

    if not contents and contents_file:
        contents = open(contents_file, 'rb').read()

    datas = open(datas_file, 'rb').read()

    embed_signature(input_file, output_file, zeros, datas, contents)
    
    click.echo(logo)