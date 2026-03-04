# 19) AppConfig
# Create AppConfig with:
# - class attribute: language = "en"
# - attribute: theme
# - method: describe() -> "language=<language>, theme=<theme>"


class AppConfig:
    language = "en"

    def __init__(self, theme: str) -> None:
        self._theme = theme

    @property
    def theme(self):
        return self._theme

    @theme.setter
    def theme(self, new_theme):
        if new_theme == "":
            raise ValueError("Theme cannot be empty!")

        self._theme = new_theme

    def describe(self):
        return f"language=<{AppConfig.language}>, theme=<{self.theme}>"


if __name__ == "__main__":
    app1 = AppConfig("Dark")
    print(app1.describe())
