import json
import os

from engines.base_engine import Engine

def init(project_name, engine):
    create_config(project_name, engine)
    create_app_py()

def create_config(project_name, engine_type):
    engine: Engine = Engine.get_engine(engine_type)
    config = {
        'project_name': project_name,

        'src-dir': 'src',
        'dist-dir': 'dist',
        'build-dir': 'build',
        
        'version': '0.0.0',

        'engine': engine_type
    }
    config = engine.config_setup(config)
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