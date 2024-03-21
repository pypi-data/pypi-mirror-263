import json
import os

from .engines.engines import ENGINE

def init(project_name, engine):
    create_config(project_name, engine)
    create_app_py()

def create_config(project_name, engine):
    config = {
        'project_name': project_name,

        'src_dir': 'src',
        'dist_dir': 'dist',
        'build_dir': 'build',

        'engine': engine,

        'scripts': ENGINE.get_engine(engine).default_scripts(),
        'smart_cd': True
    }
    with open('.proj.config', 'w') as f:
        json.dump(config, f, indent=4)

def create_app_py():
    if not os.path.exists('src'):
        os.makedirs('src')

    with open('src/app.py', 'w') as f:
        f.write('import os\n\n')
        f.write('def app():\n')
        f.write('    print(os.getcwd())\n')
        f.write('    print("Hello World.")\n\n')
        f.write('if __name__ == "__main__":\n')
        f.write('    app()')