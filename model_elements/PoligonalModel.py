from model_elements.Poligon import Poligon
from model_elements.Texture import Texture


class PoligonalModel:
    def __init__(self, poligons: Poligon, textures: Texture) -> None:
        self.poligons = poligons
        self.textures = textures
