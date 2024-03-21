import re
import os
import pyray as pr

from spacerescue.render import resource_manager
from spacerescue.render.widget import Widget
from spacerescue.tools.math import clamp


class Console(Widget):

    RESOURCE_MANAGER = resource_manager.get_instance("scene")

    FONT_SPACING = 2
    FONT_SIZE = 28
    FONT_COLOR = pr.Color(255, 255, 255, 255)
    FOOTER_SIZE = FONT_SIZE + FONT_SPACING
    BG_COLOR = pr.Color(64, 191, 182, 192)

    def __init__(
        self,
        id: str,
        position: pr.Vector2,
        size: pr.Vector2,
        buffers: list[str],
        caption: str = "",
        first_buffer: int = 0,
        border_size : int = 10
    ):
        super().__init__(id, self._get_bound(position, size, border_size, len(caption) > 0))
        self.caption = caption
        self.buffers = [self._align_text(b, self.size.x) for b in buffers]
        self.buffer_text = self.buffers[first_buffer]
        self.buffer_line = 0
        self.border_size = border_size
        
        self.scanline = Console.RESOURCE_MANAGER.load_texture("scanline")
        pr.set_texture_wrap(self.scanline, pr.TextureWrap.TEXTURE_WRAP_REPEAT)
        self.font = Console.RESOURCE_MANAGER.load_font("mono_font28")

    def update(self):
        pos = pr.get_mouse_position()
        if pr.check_collision_point_rec(pos, self.bound):
            for i in range(0, 10):
                if pr.is_key_pressed(pr.KeyboardKey.KEY_F1 + i) and i < len(
                    self.buffers
                ):
                    self.buffer_text = self.buffers[i]
                    self.buffer_line = 0

            if (
                pr.is_key_pressed(pr.KeyboardKey.KEY_UP)
                or pr.get_mouse_wheel_move() > 0
            ):
                self.buffer_line = clamp(
                    self.buffer_line - 1, 0, len(self.buffer_text) - self.size.y - 1
                )

            if (
                pr.is_key_pressed(pr.KeyboardKey.KEY_DOWN)
                or pr.get_mouse_wheel_move() < 0
            ):
                self.buffer_line = clamp(
                    self.buffer_line + 1, 0, len(self.buffer_text) - self.size.y - 1
                )

    def draw(self):
        pr.draw_rectangle_rec(self.bound, Console.BG_COLOR)

        if len(self.caption) > 0:
            pr.begin_scissor_mode(
                int(self.bound.x + self.border_size),
                int(self.bound.y + self.border_size),
                int(self.bound.width - self.border_size * 2),
                int(self.bound.height - self.border_size * 2 - self.border_size - Console.FOOTER_SIZE),
            )
        else:
            pr.begin_scissor_mode(
                int(self.bound.x + self.border_size),
                int(self.bound.y + self.border_size),
                int(self.bound.width - self.border_size * 2),
                int(self.bound.height - self.border_size * 2),
            )
        for i in range(-int(self.size.y), int(self.size.y)):
            j = int(self.buffer_line + i)
            if 0 <= j < len(self.buffer_text):
                pos = pr.Vector2(
                    self.bound.x + self.border_size,
                    self.bound.y + self.border_size + i * Console.FONT_SIZE,
                )
                text = self.buffer_text[j]
                if text.startswith("!"):
                    _, image_path = self._accept_image(text)
                    self._draw_image(image_path, pos)
                else:
                    pr.draw_text_ex(
                        self.font,
                        text,
                        pos,
                        Console.FONT_SIZE,
                        Console.FONT_SPACING,
                        Console.FONT_COLOR,
                    )
        pr.end_scissor_mode()

        pos = pr.Vector2(
            self.bound.x + self.border_size,
            self.bound.y + self.bound.height - Console.FONT_SIZE - self.border_size,
        )
        pr.draw_text_ex(
            self.font,
            self.caption,
            pos,
            Console.FONT_SIZE,
            Console.FONT_SPACING,
            Console.FONT_COLOR,
        )

        pr.draw_texture_pro(
            self.scanline,
            pr.Rectangle(0, 0, self.bound.width, self.bound.height),
            self.bound,
            pr.vector2_zero(),
            0.0,
            pr.WHITE,  # type: ignore
        )

    def _get_bound(
        self, position: pr.Vector2, size: pr.Vector2, border_size: int, with_caption: bool
    ) -> pr.Rectangle:
        if with_caption:
            self.size = pr.Vector2(
                (size.x - border_size * 2)
                // ((Console.FONT_SIZE + Console.FONT_SPACING) / 2),
                (size.y - border_size - Console.FOOTER_SIZE - border_size * 2)
                // Console.FONT_SIZE,
            )
        else:
            self.size = pr.Vector2(
                (size.x - border_size * 2)
                // ((Console.FONT_SIZE + Console.FONT_SPACING) / 2),
                (size.y - border_size * 2) // Console.FONT_SIZE,
            )
        return pr.Rectangle(position.x, position.y, size.x, size.y)

    def _align_text(self, text: str, col: int) -> list[str]:
        buffer = []
        line = ""
        for word in re.split(r"[^\S\r\n]+|\n", text):
            if word == "":
                buffer.append(line)
                buffer.append("")
                line = ""
            elif word == "*":
                buffer.append(line)
                line = word.replace("_", " ") + " "
            elif word.startswith("!"):
                caption, image_path = self._accept_image(word)
                self._load_image(caption, image_path, buffer)
            elif len(line + " " + word) >= col:
                buffer.append(line)
                line = word + " "
            else:
                line += word + " "
        buffer.append(line)
        return buffer

    def _accept_image(self, word: str):
        m = re.match(r"!\[(.+)\]\((.+)\)", word)
        assert m is not None
        return m.group(1), m.group(2)

    def _load_image(self, caption: str, image_path: str, buffer):

        # If image not found, replace by the caption

        if not os.path.exists(image_path):
            buffer.append(caption)
            return

        texture = Console.RESOURCE_MANAGER.load_texture_from_image_path(image_path)

        # Add place hoder for the image in the text

        buffer.append(f"![{caption}]({image_path})")
        for i in range(1, texture.height // Console.FONT_SIZE):
            buffer.append("")

    def _draw_image(self, image_path: str, pos: pr.Vector2):
        texture = Console.RESOURCE_MANAGER.load_texture_from_image_path(image_path)
        pr.draw_texture_pro(
            texture,
            pr.Rectangle(
                0,
                0,
                texture.width,
                texture.height,
            ),
            pr.Rectangle(
                int(pos.x),
                int(pos.y),
                texture.width,
                texture.height,
            ),
            pr.vector2_zero(),
            0.0,
            pr.WHITE,  # type: ignore
        )
