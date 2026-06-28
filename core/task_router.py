class TaskRouter:
    """
    يستقبل طلبات الواجهة
    ويوجهها إلى المحرك المناسب.
    """

    def __init__(self, engine_manager):
        self.engine_manager = engine_manager

    def route(self, engine_name):
        return self.engine_manager.get(engine_name)
