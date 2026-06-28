class EngineManager:
    """
    مسؤول عن تسجيل محركات الذكاء الاصطناعي
    وإدارتها وتشغيلها.
    """

    def __init__(self):
        self.engines = {}

    def register(self, name, engine):
        self.engines[name] = engine

    def get(self, name):
        return self.engines.get(name)

    def exists(self, name):
        return name in self.engines

    def list_engines(self):
        return list(self.engines.keys())
