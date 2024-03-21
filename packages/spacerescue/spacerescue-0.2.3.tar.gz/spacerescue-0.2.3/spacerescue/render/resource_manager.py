from functools import cache

import pyray as pr

PATHS = {
    # MUSICS:
    "music": ["resources/sounds/music.mp3"],
    # SOUNDS
    "button_click": ["resources/sounds/buttonfx.wav"],
    # FONTS
    "mono_font28": ["resources/fonts/GelatinMonoTTF.ttf", 28, None, 0],
    # TEXTURES
    "particule": ["resources/textures/particule.png"],
    "deck": ["resources/textures/deck.png"], # deprecated
    "cockpit": ["resources/textures/cockpit.png"],
    "computer_console": ["resources/textures/computer_console.png"],
    "scanline": ["resources/textures/scanline.png"],
    "logo": ["resources/textures/logo.png"],
    "title": ["resources/textures/title.png"],
    "menu": ["resources/textures/menu.png"],
    # MODELS - STELLAR OBJECTS
    "asteroid": ["resources/models/stellar_objects/asteroid.obj"],
    "sun": ["resources/models/stellar_objects/sun.obj"],
    "venus": ["resources/models/stellar_objects/venus.obj"],
    "earth": ["resources/models/stellar_objects/earth.obj"],
    "mars": ["resources/models/stellar_objects/mars.obj"],
    "wormhole": ["resources/models/stellar_objects/wormhole.obj"],
    # MODELS - SPACESHIPS
    "ncc-1701": ["resources/models/spaceships/enterprice.obj"],
    # SHADERS
    "shader_bloom": [None, "resources/shaders/bloom.fs"],
    "shader_lighting": [
        "resources/shaders/lighting.vs",
        "resources/shaders/lighting.fs",
    ],
    "shader_alpha_discard": [None, "resources/shaders/alpha_discard.fs"],
}


class CacheEntry:

    def __init__(self, type, value):
        self.type = type
        self.value = value


class RecourseManager:

    def __init__(self):
        self.cache: dict[str, CacheEntry] = {}

    def unload_all(self):
        for entry in self.cache.values():
            if entry.type == "music":
                pr.unload_music_stream(entry.value)
            elif entry.type == "sound":
                while pr.is_sound_playing(entry.value):
                    pass
                pr.unload_sound(entry.value)
            elif entry.type == "font":
                pr.unload_font(entry.value)
            elif entry.type == "texture":
                pr.unload_texture(entry.value)
            elif entry.type == "model":
                pr.unload_model(entry.value)
            elif entry.type == "shader":
                pr.unload_shader(entry.value)
        self.cache = {}

    def load_music(self, name: str) -> pr.Music:
        entry = self.cache.get(name)
        if entry is None:
            entry = CacheEntry("music", pr.load_music_stream(*PATHS[name]))
            self.cache[name] = entry
        assert entry.type == "music"
        return entry.value

    def load_sound(self, name: str) -> pr.Sound:
        entry = self.cache.get(name)
        if entry is None:
            entry = CacheEntry("sound", pr.load_sound(*PATHS[name]))
            self.cache[name] = entry
        assert entry.type == "sound"
        return entry.value

    def load_font(self, name: str) -> pr.Font:
        entry = self.cache.get(name)
        if entry is None:
            entry = CacheEntry("font", pr.load_font_ex(*PATHS[name]))
            self.cache[name] = entry
        assert entry.type == "font"
        return entry.value

    def load_texture(self, name: str) -> pr.Texture:
        entry = self.cache.get(name)
        if entry is None:
            entry = CacheEntry("texture", pr.load_texture(*PATHS[name]))
            self.cache[name] = entry
        assert entry.type == "texture"
        return entry.value

    def load_model(self, name: str) -> pr.Model:
        entry = self.cache.get(name)
        if entry is None:
            entry = CacheEntry("model", pr.load_model(*PATHS[name]))
            self.cache[name] = entry
        assert entry.type == "model"
        return entry.value

    def load_shader(self, name: str) -> pr.Shader:
        entry = self.cache.get(name)
        if entry is None:
            entry = CacheEntry("shader", pr.load_shader(*PATHS[name]))
            self.cache[name] = entry
        assert entry.type == "shader"
        return entry.value

    def load_texture_from_image_path(self, image_path: str) -> pr.Texture:
        entry = self.cache.get(image_path)
        if entry is None:
            entry = CacheEntry("texture", pr.load_texture(image_path))
            self.cache[image_path] = entry
        assert entry.type == "texture"
        return entry.value


@cache
def get_instance(name: str = "singleton") -> RecourseManager:
    return RecourseManager()
