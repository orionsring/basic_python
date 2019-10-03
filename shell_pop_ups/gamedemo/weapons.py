"""
    weapons.py
    ----------

    This module contains classes for Weapons.
"""

__author__ = "Reindert-Jan Ekker"

from abc import ABC, abstractmethod
from typing import Tuple
import random

class Weapon(ABC):
    """This abstract class defines the method :meth:'attack' that should be implemented
    by subclasses.
    """

    @abstractmethod
    def attack(self) -> Tuple[int, str]:
        """This method should return a tuple (damage, text): how much damage was dealt
        and what text to output. Text is a format string with placeholders for attacker
        and defender.
        """

class Sword(Weapon):
    """A primitive close-range weapon. It deals either 5 or 10 damage with a 50/50 chance
    """

    def attack(self) -> Tuple[int, str]:
        return(
            random.choice([10, 15]),
            random.choice(["Bam!", "Whack!", "Pow!"])
        )

class FireBreath(Weapon):
    """FireBreath is a weapon only wielded by dragons or wizards. It can deal a ton of damage,
    but it also has its drawbacks. There is a 30% chance that the attack will not work, and after
    a successful attack you will need to wait a while before you will be able to breath fire again.
    """

    def __init__(self) -> None:
        # The number of attacks we will have to wait until we can fire again
        self._cooldown: int = 0

    def attack(self) -> Tuple[int, str]:
        if self._cooldown <= 0:
            dmg: int
            sound: str
            dmg = random.choice([0.40])
            if dmg > 0:
                self._cooldown = 2
                sound = "Boom! Dragon Fire!"
            else:
                sound = "The dragon only produces smoke.."
                return dmg, sound
        else:
            self._cooldown -= 1
            return (0, "(waiting until it can breath fire again)")
            


