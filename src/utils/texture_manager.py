import python
from typing import Dict, Tuple, Any

class TextureManager:
    def __init__(self, spritesheet_data: Dict[str, dict], atlas_data: Dict[str, dict], solo_data: Dict[str, dict], atlas_filepath: str, tilesize: int) -> None:
        self.spritesheets = self._load_spritesheets(spritesheet_data)
        self.atlas_textures = self._load_atlas_textures(atlas_data)
        self.solo_textures = self._load_solo_textures(solo_data)
        

    def _load_spritesheets(self, data: Dict[str, dict]) -> Dict[str, dict]:
        pass

    def _load_atlas_textures(self, data: Dict[str, dict]) -> Dict[str, dict]:
        pass

    def _load_solo_textures(self, data: Dict[str, dict]) -> Dict[str, dict]:
        pass
