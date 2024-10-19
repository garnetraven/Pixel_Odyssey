from globals import *

class Atlas:
    def __init__(self, file_path: str, size: tuple, textures: dict):
        self.file_path = file_path
        self.size = size
        self.textures = textures

class AtlasTexture:
    def __init__(self, name: str, position: tuple, size: tuple, type: str = "default") -> None:
        self.name = name
        self.position = position
        self.size = size
        self.type = type

class Texture:
    def __init__(self, name: str, size: tuple, file_path: str, type: str = "default") -> None:
        self.name = name
        self.size = size
        self.file_path = file_path
        self.type = type


player_textures = {
    'player_static':Texture('player_static', (TILESIZE, TILESIZE*2), ""),
}
