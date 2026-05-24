from midia import Midia


class Video(Midia):
    """
    Representa um vídeo educacional.
    Atributo adicional: resolucao (ex.: '1080p', '4K').
    """

    def __init__(self, titulo: str, duracao: float, resolucao: str):
        super().__init__(titulo, duracao)
        self.resolucao = resolucao

    def mostrar_info(self) -> None:
        print(f"[🎬 Vídeo]")
        super().mostrar_info()
        print(f"  Resolução: {self.resolucao}")

    def reproduzir(self) -> None:
        print(f"▶  Reproduzindo vídeo '{self.titulo}' em {self.resolucao}...")


class Podcast(Midia):
    """
    Representa um podcast educacional.
    Atributo adicional: apresentador.
    """

    def __init__(self, titulo: str, duracao: float, apresentador: str):
        super().__init__(titulo, duracao)
        self.apresentador = apresentador

    def mostrar_info(self) -> None:
        print(f"[🎙  Podcast]")
        super().mostrar_info()
        print(f"  Apresentador: {self.apresentador}")

    def reproduzir(self) -> None:
        print(f"🎧 Reproduzindo podcast '{self.titulo}'"
              f" com {self.apresentador}...")


class TextoNarrado(Midia):
    """
    Representa um texto narrado educacional.
    Atributo adicional: idioma.
    """

    def __init__(self, titulo: str, duracao: float, idioma: str):
        super().__init__(titulo, duracao)
        self.idioma = idioma

    def mostrar_info(self) -> None:
        print(f"[📖 Texto Narrado]")
        super().mostrar_info()
        print(f"  Idioma: {self.idioma}")

    def reproduzir(self) -> None:
        print(f"🔊 Reproduzindo texto narrado '{self.titulo}'"
              f" no idioma {self.idioma}...")
