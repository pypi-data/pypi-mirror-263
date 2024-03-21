from ..engines import BaseEngine

class PackageEngine(BaseEngine):
    def default_scripts(self):
        return {
            'dev': 'python src/app.py',
            'build': 'python setup.py sdist bdist_wheel',
        }