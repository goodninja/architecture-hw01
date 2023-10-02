from model_elements.PoligonalModel import PoligonalModel
from model_elements.Flash import Flash
from model_elements.Camera import Camera


class Scene:
    def __init__(self, id: int, models: PoligonalModel, flashes: Flash, cameras: Camera) -> None:
        self.id = id
        self.models = models
        self.flashes = flashes
        self.cameras = cameras

    def method_1(data: None) -> None:
        pass

    def method_2(data1: None, data2: None) -> None:
        pass
