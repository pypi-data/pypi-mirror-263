from abc import abstractmethod
from .package_engine.package_engine import PackageEngine

class ENGINE:
    PACKAGE = 'package'
    
    def get_engine(engine: str):
        if engine == ENGINE.PACKAGE:
            return PackageEngine()
        else:
            raise ValueError(f'Engine {engine} not supported.')
        
class BaseEngine:
    @abstractmethod
    def default_scripts(self):
        pass