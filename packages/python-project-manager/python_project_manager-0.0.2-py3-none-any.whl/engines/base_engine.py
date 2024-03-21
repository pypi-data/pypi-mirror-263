from .package_engine import PackageEngine

class Engine:    
    PACKAGE = 'package'

    def get_engine(engine: str):
        if engine == Engine.PACKAGE:
            return PackageEngine()
        else:
            raise ValueError(f'Engine {engine} not supported.')

    def config_setup(self, config):
        raise NotImplementedError('config_setup not implemented')
    