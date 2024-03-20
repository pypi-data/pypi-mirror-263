from .pypi.pypi_engine import PypiEngine

class ENGINE:
    PYPI = 'pypi'
    
    def get_engine(engine: str):
        if engine == ENGINE.PYPI:
            return PypiEngine()
        else:
            raise ValueError(f'Engine {engine} not supported.')