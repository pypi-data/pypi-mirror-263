# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['travdata',
 'travdata.cli',
 'travdata.cli.cmds',
 'travdata.datatypes',
 'travdata.datatypes.core',
 'travdata.extraction',
 'travdata.tableconverters',
 'travdata.tableconverters.core',
 'travdata.travellermap']

package_data = \
{'': ['*']}

install_requires = \
['progress>=1.6,<2.0',
 'ruamel-yaml>=0.18.6,<0.19.0',
 'tabula-py[jpype]>=2.9.0,<3.0.0']

entry_points = \
{'console_scripts': ['travdata_cli = travdata.cli.cli:main']}

setup_kwargs = {
    'name': 'travdata',
    'version': '0.1.0',
    'description': 'Data utility code for Mongoose Traveller TTRPG.',
    'long_description': "= Traveller Data Utils\n\nPython library and assorted tools for assisting with the Mongoose Traveller\nTTRPG system.\n\nThe extracted data is *not* for redistribution, as it is almost certainly\nsubject to copyright (I am not a lawyer - but it's safer to assume caution over\ndistribution). This utility (and its output) is intended as an aid to those who\nlegally own a copy of the Mongoose Traveller materials, and wish to make use of\nthe data for their own direct purposes. It is the sole responsibility of the\nuser of this program to use the extracted data in a manner that respects the\npublisher's IP rights.\n\nIMPORTANT: Do not distribute the data extracted PDF files without explicit\npermission from the copyright holder.\n\nThe purpose of this tool is to extract the data for usage by the legal owner of\na copy of the original materal that it was extracted from.\n\n== Usage\n\nThis package is primarily intended for the provided CLI tools, but API access is\nalso possible.\n\nFor any usage of the CLI or API that involves extracting CSV data from PDFs, the\nJava Runtime Environment (JRE) must be installed on the system.\n\n=== CLI `tools/extractcsvtables.py`\n\nThis tool extracts CSV files from tables in the given PDF, based on the given\nconfiguration files that specifies the specifics of how those tables can be\nturned into useful CSV data. As such, it only supports extraction of tables from\nknown PDF files, where the individual tables have been configured.\n\nThe general form of the command is:\n\n[source,shell]\n----\ntravdata_cli extractcsvtables CONFIG_DIR INPUT.PDF OUT_DIR\n----\n\nWhere:\n\n`CONFIG_DIR`:: is the path to the directory containing a `config.yaml` file, and\nsubdirectories and `*.tabula-template.json` files. This contains information\nguiding the extraction, and is specific to the PDF being read from.\n`INPUT.PDF`:: is the path to the PDF file to read tables from.\n`OUT_DIR`:: is the path to a (potentially not existing) directory to output the\nresulting CSV files. This will result in containing a directory and file\nstructure that mirrors that in `CONFIG_DIR`, but will contain `.csv` rather than\n`.tabula-template.json` files.\n\nAt the present time, the only supported input PDF file is the Mongoose Traveller\nCore Rulebook 2022, and not all tables are yet supported for extraction.\n\n== Developing\n\nSee development.adoc for more information on developing and adding more tables\nto the configuration.\n",
    'author': 'John Beisley',
    'author_email': 'johnbeisleyuk@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/huin/travdata',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
