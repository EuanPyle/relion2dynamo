import click
import numpy as np
import pandas as pd
import starfile
import dynamotable
from eulerangles import convert_eulers

from .utils import sanitise_dynamo_table_filename, reextract_table_filename, normalize


def relion2dynamo(warp_star_file, output_dynamo_table_file):
    """
    Converts a Warp STAR file into a Dynamo table file.
    """
    # Read STAR file
    relion_star = starfile.read(warp_star_file)
    
    # Remove optics table
    relion_star = pd.DataFrame.from_dict(relion_star['particles']) 
    
    # Initialise empty dict for dynamo
    dynamo_data = {}

    # Get XYZ positions and put into data
    for axis in ('x', 'y', 'z'):
        relion_heading = 'rlnCoordinate' + axis.upper()
        dynamo_data[axis] = relion_star[relion_heading]

    # Get euler angles and convert to dynamo convention (only if eulers present in STAR file)
    if 'rlnAngleRot' in relion_star.columns:
        eulers_relion = relion_star[['rlnAngleRot', 'rlnAngleTilt', 'rlnAnglePsi']].to_numpy()
        eulers_dynamo = convert_eulers(eulers_relion,
                                       source_meta='relion',
                                       target_meta='dynamo')

        dynamo_data['tdrot'] = eulers_dynamo[:, 0]
        dynamo_data['tilt'] = eulers_dynamo[:, 1]
        dynamo_data['narot'] = eulers_dynamo[:, 2]
    
    # Add tomo to column
    
    dynamo_data['tomo'] = relion_star['rlnTomoName'].str.split('_').str[1]
        
    #add class number to table
    
    dynamo_data['class'] = relion_star['rlnClassNumber']
    
    #add cc to table
            
    dynamo_data['cc'] = normalize(relion_star)

    # Convert to DataFrame
    df = pd.DataFrame.from_dict(dynamo_data)

    # Write table file
    output_dynamo_table_file = sanitise_dynamo_table_filename(output_dynamo_table_file)
    click.echo(
        f"Writing out Dynamo table file '{output_dynamo_table_file}' and corresponding table map file with appropriate info...\n")
    dynamotable.write(df, output_dynamo_table_file)

    click.echo(f"\nDone! Converted Warp output '{warp_star_file}' into Dynamo input files")
    return


@click.command()
@click.option('--input_star_file', '-i', 'warp_star_file',
              prompt='Input Warp STAR file',
              type=click.Path(exists=True),
              required=True)
@click.option('--output_table_file', '-o', 'dynamo_table_file',
              type=click.Path(exists=False),
              prompt='Output dynamo table file')
def cli(warp_star_file, dynamo_table_file):
    relion2dynamo(warp_star_file, dynamo_table_file)
