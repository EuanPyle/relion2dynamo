from pathlib import Path
from typing import Optional

class IOConverter:
    def __init__(self, input_star: Path, output_name: Optional[Path] = None):
        self.input_star: Path = input_star
        if output_name is not None:
            self.output_name: str = output_name
        else:
            self.output_name: str = self.generate_output_file_name(self.input_star) 
    
    def generate_output_file_name(self, input_star: Path) -> Path:
        """
	Generate output file name as identical to input file name with .tbl extention
	"""
        output_name = input_star.stem + '.tbl'
        return output_name
    
    


