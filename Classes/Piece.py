from abc import ABC, abstractmethod


class Piece(ABC):
    name = "piece"
    description = "description"

    @abstractmethod
    def beats_victim_piece(self, pos_x, pos_y, victim_x, victim_y):
        pass
