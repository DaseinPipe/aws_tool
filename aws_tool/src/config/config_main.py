
import os
from aws_tool.src import stylesheets

__config_folder_path = os.path.dirname(os.path.realpath(__file__))

_stylesheets_folder_path = os.path.dirname(os.path.abspath(stylesheets.__file__))


stylesheet_path = os.path.join(_stylesheets_folder_path,'EasyCode.qss')

UNKNOWN = 'UNKNOWN'
