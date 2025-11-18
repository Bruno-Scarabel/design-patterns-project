# Padrão Observer (Comportamental)
# Exemplo baseado no catálogo Refactoring Guru
# Implementação feita com o auxílio do ChatGPT (GPT-5)

from typing import List

# ---- Subject (Sujeito) ----
class NewsPublisher:
    def __init__(self):
        self.subscribers: List['Subscriber'] = []
        self.latest_news = None

    def attach(self, subscriber):
        self.subscribers.append(subscriber)

    def detach(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify(self):
        for sub in self.subscribers:
            sub.update(self.latest_news)

    def add_news(self, news: str):
        print(f"\n📰 Nova notícia publicada: {news}")
        self.latest_news = news
        self.notify()

# ---- Observer (Observador) ----
class Subscriber:
    def __init__(self, name: str):
        self.name = name

    def update(self, news: str):
        print(f"📢 {self.name} recebeu a atualização: '{news}'")

# ---- Exemplo de uso ----
if __name__ == "__main__":
    publisher = NewsPublisher()

    # Cria observadores
    ana = Subscriber("Ana")
    bruno = Subscriber("Bruno")
    carla = Subscriber("Carla")

    # Registra observadores
    publisher.attach(ana)
    publisher.attach(bruno)
    publisher.attach(carla)

    # Publica notícias
    publisher.add_news("Design Patterns são incríveis!")
    publisher.add_news("Python 3.13 lançado!")
