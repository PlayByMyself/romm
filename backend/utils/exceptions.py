class PlatformsNotFoundException(Exception):
    def __init__(self):
        self.message = f"Platforms not found"
        super().__init__(self.message)

    def __repr__(self) -> str:
        return self.message


class RomsNotFoundException(Exception):
    def __init__(self, platform: str):
        self.message = f"Roms not found for platform {platform}"
        super().__init__(self.message)

    def __repr__(self) -> str:
        return self.message


class RomNotFoundError(Exception):
    def __init__(self, rom: str, platform: str):
        self.message = f"Rom {rom} not found for platform {platform}"
        super().__init__(self.message)

    def __repr__(self) -> str:
        return self.message


class RomAlreadyExistsException(Exception):
    def __init__(self, rom_name: str):
        self.message = f"Can't rename: {rom_name} already exists"
        super().__init__(self.message)

    def __repr__(self) -> str:
        return self.message