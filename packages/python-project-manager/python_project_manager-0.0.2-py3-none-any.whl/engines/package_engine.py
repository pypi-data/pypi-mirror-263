import re
import toml

class PackageEngine():
    def config_setup(self, config):
        self.__default_scripts(config)
        self.__create_toml(config)
        return config
    
    def __default_scripts(self, config):
        project_name = re.sub(r' |-', '_', config['project_name'])
        verison = config['version']
        default_scripts = {
            'dev': 'python src/app.py',
            'build': 'python -m build',
            'install': f'pip install dist/{project_name}-{verison}-py3-none-any.whl -U',
            'uninstall': f'pip uninstall dist/{project_name}-{verison}-py3-none-any.whl',
        }
        config['scripts'] = default_scripts
    
    def __create_toml(self, config):
        toml_config = {
            'build-system': {
                'requires': ['setuptools', 'wheel'],
                'build-backend': 'setuptools.build_meta'
            },

            'project': {
                'name': config['project_name'],
                'version': config['version'],
                'description': 'A Python package.',
                'authors': [],
                'readme': 'README.md',
                'keywords': []
            }
        }
        with open('pyproject.toml', 'w') as f:
            toml.dump(toml_config, f)