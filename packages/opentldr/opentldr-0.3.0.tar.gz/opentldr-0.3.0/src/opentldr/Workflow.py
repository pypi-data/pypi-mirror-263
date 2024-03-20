import papermill as pm

import logging
logging.basicConfig(format='OpenTLDR Logging: %(message)s')
_log=logging.getLogger("OpenTLDR")

# Pull environment variables from .env or os
from dotenv import load_dotenv
load_dotenv()

# disable warning for debugging of frozen packages
# seems to only matter when running under Jupyter
import os
os.environ["PYDEVD_DISABLE_FILE_VALIDATION"]="1"



class Workflow:

    # defaults can be overridden when creating workflow instance
    output_path:str = "./READ_ONLY_OUTPUT"
    workflow:list[str] = [
            "Step_0_Initialize.ipynb",
            "Step_1_Ingest.ipynb",
            "Step_1a_MockUI.ipynb",
            "Step_2_Connect.ipynb",
            "Step_3_Recommend.ipynb",
            "Step_4_Summarize.ipynb",
            "Step_5_Produce.ipynb",
            "Step_6_Evaluate.ipynb"
            ]
    parameters:dict = {
        "message":"Successfully passed parameters!"
        }

    def __init__(self, workflow:list[str], parameters:dict, output_path=None, database=None):
        if output_path is not None:
            self.output_path=output_path
        if workflow is not None:
            self.workflow=workflow
        if parameters is not None:
            self.parameters=parameters
        if database is not None:
            self.database=database
        self.ensure_path(self.output_path)

    def ensure_path(self,path):
        '''
        ensure_path(path) simply creates a directory if it is not there already.
        '''
        if not os.path.exists(path):
            os.makedirs(path)
            print("Created output directory: "+path)

    def execute_notebook(self, inNotebook:str):
        '''
        execute_notebook runs a single notebook file in PaperMill
        '''
        outNotebook:str = os.path.join(self.output_path,inNotebook.replace('/',"_"))
        pm.execute_notebook( inNotebook, outNotebook,
                         parameters=self.parameters)
    
    def run(self):
        '''
        run the defined workflow files in order in PaperMill
        '''
        for step in self.workflow:
            print("\nStarting "+step)
            self.execute_notebook(step)
            print("Completed "+step)
