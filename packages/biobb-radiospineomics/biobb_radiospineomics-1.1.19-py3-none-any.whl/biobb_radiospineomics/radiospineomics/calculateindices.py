#!/usr/bin/env python3

import pandas as pd
import radiomics
import yaml 

#from functions import calculate_indices

from biobb_radiospineomics.radiospineomics.common import calculate_indices

"""Module containing the Template class and the command line interface."""
import argparse
import shutil
from pathlib import PurePath
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.configuration import settings
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger



"""

Input for the BioBB for RadioSpineOmics: 

    - 3 masks in nrrd format (keep maintaining it as standard input, then in workflow can process via directory path);
    - 2D slice in nrrd format;
    - Shape Params config file in YML format;
    - Texture Params config file in YML format;

"""


# 1. Rename class as required
class CalculateIndices(BiobbObject):
    """
    | biobb_template Template
    | Short description for the `template <http://templatedocumentation.org>`_ module in Restructured Text (reST) syntax. Mandatory.
    | Long description for the `template <http://templatedocumentation.org>`_ module in Restructured Text (reST) syntax. Optional.

    Args:
        input_file_path1 (str): Description for the first input file path. File type: input. `Sample file <https://urlto.sample>`_. Accepted formats: top (edam:format_3881).
        input_file_path2 (str) (Optional): Description for the second input file path (optional). File type: input. `Sample file <https://urlto.sample>`_. Accepted formats: dcd (edam:format_3878).
        output_file_path (str): Description for the output file path. File type: output. `Sample file <https://urlto.sample>`_. Accepted formats: zip (edam:format_3987).
        properties (dic):
            * **boolean_property** (*bool*) - (True) Example of boolean property.
            * **binary_path** (*str*) - ("zip") Example of executable binary property.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_template.template.template import template

            prop = {
                'boolean_property': True
            }
            template(input_file_path1='/path/to/myTopology.top',
                    output_file_path='/path/to/newCompressedFile.zip',
                    input_file_path2='/path/to/mytrajectory.dcd',
                    properties=prop)

    Info:
        * wrapped_software:
            * name: Zip
            * version: >=3.0
            * license: BSD 3-Clause
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl

    """

    # 2. Adapt input and output file paths as required. Include all files, even optional ones
    def __init__(self, input_mask_path1, input_mask_path2, input_mask_path3, input_image_path1, output_file_path, properties=None, **kwargs) -> None:
        properties = properties or {}

        # 2.0 Call parent class constructor
        super().__init__(properties)
        self.locals_var_dict = locals().copy()

        # 2.1 Modify to match constructor parameters
        # Input/Output files
        self.io_dict = {
            'in': {'input_mask_path1': input_mask_path1, 'input_mask_path2': input_mask_path2, 'input_mask_path3': input_mask_path3, 'input_image_path1': input_image_path1},
            'out': {'output_file_path': output_file_path}
        }

        # 3. Include all relevant properties here as
        # self.property_name = properties.get('property_name', property_default_value)

        # Properties specific for BB
        #self.boolean_property = properties.get('boolean_property', True)
       # self.binary_path = properties.get('binary_path', 'zip')
        #self.resamplings = properties.get('resampling', [[0,0], [0.27, 0.27], [0.135, 0.135]])
        #self.binwidths = properties.get('binwidths', [1, 2, 4, 8, 16, 32, 64])
        self.properties = properties

        # Check the properties
        self.check_properties(properties)
        # Check the arguments
        #self.check_arguments()

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`Template <template.template.Template>` object."""

        # 4. Setup Biobb
        if self.check_restart():
            return 0
        #self.stage_files()

        # Creating temporary folder
        #self.tmp_folder = fu.create_unique_dir()
        #fu.log('Creating %s temporary folder' % self.tmp_folder, self.out_log)

        # 5. Include here all mandatory input files
        # Copy input_file_path1 to temporary folder
        #shutil.copy(self.io_dict['in']['input_file_path1'], self.tmp_folder)
        #for file_name, file_path in self.io_dict['in'].items():
        #    destination_path = os.path.join(self.tmp_folder, file_name)
        #    shutil.copy(file_path, destination_path)
        
        # 6. Prepare the command line parameters as instructions list
        #instructions = ['-j']
        #if self.boolean_property:
        #    instructions.append('-v')
        #    fu.log('Appending optional boolean property', self.out_log, self.global_log)

        # 7. Build the actual command line as a list of items (elements order will be maintained)
        #self.cmd = [self.binary_path,
        #            ' '.join(instructions),
        #            self.io_dict['out']['output_file_path'],
        #            str(PurePath(self.tmp_folder).joinpath(PurePath(self.io_dict['in']['input_file_path1']).name))]
        #fu.log('Creating command line with instructions and required arguments', self.out_log, self.global_log)

        # 8. Repeat for optional input files if provided
        #if self.io_dict['in']['input_file_path2']:
            # Copy input_file_path2 to temporary folder
        #    shutil.copy(self.io_dict['in']['input_file_path2'], self.tmp_folder)
            # Append optional input_file_path2 to cmd
        #    self.cmd.append(str(PurePath(self.tmp_folder).joinpath(PurePath(self.io_dict['in']['input_file_path2']).name)))
        #    fu.log('Appending optional argument to command line', self.out_log, self.global_log)

        # 9. Uncomment to check the command line
        # print(' '.join(cmd))

        # Run Biobb block
        self.run()

        # Copy files to host
        #self.copy_to_host()

        # Remove temporary file(s)
        #self.tmp_files.extend([
        #    self.stage_io_dict.get("unique_dir"),
        #    self.tmp_folder
        #])
        #self.remove_tmp_files()

        # Check output arguments
        #self.check_arguments(output_files_created=True, raise_exception=False)

        return self.return_code

    def run(self):
        fsu = []

        for key, value in self.io_dict['in'].items():
            if 'mask' in key:
                fsu.append(value)
            elif 'image' in key:
                fsu_image = value

        if not fsu:
            print("Error: No mask files found in the input dictionary.")
            exit()

        if not fsu_image:
            print("Error: No image file found in the input dictionary.")

        geometry_results = None
        try: 
            geometry_results = calculate_indices(fsu, fsu_image)
        except Exception as e: 
            print(f'Error extracting features for {fsu[1]}: {e}')

        if geometry_results is not None:
            geometry_results = pd.DataFrame(geometry_results, index=[0])
            geometry_results['id'] = fsu[1].split('/')[-1]
            geometry_results.to_csv(self.io_dict['out']['output_file_path'], index=False)
        else:
            print("No se pudo generar geometry_results debido a un error.")



def calculateindices(input_mask_path1: str, input_mask_path2: str, input_mask_path3: str, input_image_path1: str,  output_file_path: str, input_file_path2: str = None, properties: dict = None, **kwargs) -> int:
    """Create :class:`Template <template.template.Template>` class and
    execute the :meth:`launch() <template.template.Template.launch>` method."""

    return CalculateIndices(input_mask_path1=input_mask_path1,
                            input_mask_path2=input_mask_path2,
                            input_mask_path3=input_mask_path3,
                            input_image_path1=input_image_path1,
                            output_file_path=output_file_path,
                            properties=properties, **kwargs).launch()


def main():
    """Command line execution of this building block. Please check the command line documentation."""
    parser = argparse.ArgumentParser(description='Description for the template module.', formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
   # parser.add_argument('--config', required=False, help='Configuration file')
    # 10. Include specific args of each building block following the examples. They should match step 2
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('--input_mask_path1', required=True, help='')
    required_args.add_argument('--input_mask_path2', required=True, help='')
    required_args.add_argument('--input_mask_path3', required=True, help='')
    required_args.add_argument('--input_image_path1', required=True, help='')
    #parser.add_argument('--input_file_path2', required=False, help='Description for the second input file path (optional). Accepted formats: dcd.')
    required_args.add_argument('--output_file_path', required=True, help='Description for the output file path. Accepted formats: zip.')

    args = parser.parse_args()
    args.config = args.config or "{}"
    properties = settings.ConfReader(config=args.config).get_prop_dic()

    # 11. Adapt to match Class constructor (step 2)
    # Specific call of each building block
    calculateindices(input_mask_path1=args.input_mask_path1,
                     input_mask_path2=args.input_mask_path2,
                     input_mask_path3=args.input_mask_path3,
                     input_image_path1=args.input_image_path1,
                     output_file_path=args.output_file_path,
                     properties=properties)


if __name__ == '__main__':
    main()

# 12. Complete documentation strings
