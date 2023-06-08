import pandas as pd
import starfile
import dynamotable
import typer

from eulerangles import convert_eulers
from collections import OrderedDict
from pathlib import Path
from typing import Optional

from ._io_converter import IOConverter

cli = typer.Typer(add_completion=False)
@cli.command(name='relion2dynamo')
def relion2dynamo_cli(
    relion_star_file: Path = typer.Option(...),
    dynamo_table_file: Optional[Path] = typer.Option(None)
    ):
    """
    Converts a RELION STAR file into a Dynamo table file.
    
    Parameters
    ----------
    
    relion_star_file: Path 
        Path to the RELION star file to be converted.
    dynamo_table_file: Optional[Path]
        Desired file name for the output Dynamo table.
    """

    # Read STAR file
    relion_star = starfile.read(relion_star_file)
    
    # If exists, remove optics table 
    if isinstance(relion_star,OrderedDict):
        try: 
            relion_particles = pd.DataFrame.from_dict(relion_star['particles'])
            relion_optics = pd.DataFrame.from_dict(relion_star['optics'])
        except KeyError:
            raise RuntimeError("Cannot find data_particles or data_optics in star file")    
    
    # Initialise empty dict for dynamo
    dynamo_data = {}

    # Get XYZ positions and put into data
    unbinned_pixel_size = relion_optics['rlnTomoTiltSeriesPixelSize'].values[0]
    
    for axis in ('x', 'y', 'z'):
        relion_coordinate_heading = 'rlnCoordinate' + axis.upper()
        relion_shift_heading = 'rlnOrigin' + axis.upper() + 'Angst'
        relion_shift = relion_particles[relion_shift_heading] / unbinned_pixel_size
        dynamo_data[axis] = relion_particles[relion_coordinate_heading] - relion_shift 

    # Get euler angles and convert to dynamo convention (only if eulers present in STAR file)
    if 'rlnAngleRot' in relion_particles.columns:
        eulers_relion = relion_particles[['rlnAngleRot', 'rlnAngleTilt', 'rlnAnglePsi']].to_numpy()			       
        eulers_dynamo = convert_eulers(eulers_relion,
                                       source_meta='relion',
                                       target_meta='dynamo')				       
	
        dynamo_data['tdrot'] = eulers_dynamo[:, 0]
        dynamo_data['tilt'] = eulers_dynamo[:, 1]
        dynamo_data['narot'] = eulers_dynamo[:, 2]
    
    # Add tomo to Dynamo table    
    dynamo_data['tomo'] = relion_particles['rlnTomoName'].str.split('_').str[1]
        
    # Add object number to Dynamo table
    if 'rlnObjectNumber' in relion_particles.columns:
        dynamo_data['reg'] = relion_particles['rlnObjectNumber']

    # Add class number to Dynamo table
    if 'rlnClassNumber' in relion_particles.columns:
        dynamo_data['class'] = relion_particles['rlnClassNumber']

    # Convert to DataFrame
    df = pd.DataFrame.from_dict(dynamo_data)

    # Write table file
    io_names = IOConverter(
        input_star = relion_star_file, 
        output_name = dynamo_table_file
    )
    dynamotable.write(df, io_names.output_name)
    return
