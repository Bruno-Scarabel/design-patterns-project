# Padrão Factory Method (Criacional)
# Exemplo baseado no catálogo Refactoring Guru
# Implementação feita com o auxílio do ChatGPT (GPT-5)

from abc import ABC, abstractmethod

# ---- Product (Produto) ----
class Button(ABC):
    @abstractmethod
    def render(self):
        pass

# ---- Concrete Products ----
class WindowsButton(Button):
    def render(self):
        print("🪟 Renderizando um botão estilo Windows.")

class HTMLButton(Button):
    def render(self):
        print("🌐 Renderizando um botão HTML.")

# ---- Creator (Criador) ----
class Dialog(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    def render_window(self):
        button = self.create_button()
        print("🧱 Janela criada. Agora renderizando o botão...")
        button.render()

# ---- Concrete Creators ----
class WindowsDialog(Dialog):
    def create_button(self) -> Button:
        return WindowsButton()

class WebDialog(Dialog):
    def create_button(self) -> Button:
        return HTMLButton()

# ---- Exemplo de uso ----
if __name__ == "__main__":
    platform = input("Escolha a plataforma (windows/web): ").lower()

    if platform == "windows":
        dialog = WindowsDialog()
    else:
        dialog = WebDialog()

    dialog.render_window()
