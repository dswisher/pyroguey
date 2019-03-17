"""Fighter component."""


class Fighter:
    """Fighter component."""

    def __init__(self, hp, defense, power):
        """Constructor."""
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.power = power

    def take_damage(self, amount):
        """Take damange."""
        results = []

        self.hp -= amount

        if self.hp <= 0:
            results.append({'dead': self.owner})

        return results

    def attack(self, target):
        """Attack the specified entity."""
        results = []

        damage = self.power - target.fighter.defense

        if damage > 0:
            target.fighter.take_damage(damage)
            results.append({'message': '{0} attacks {1} for {2} hit points.'.format(self.owner.name.capitalize(), target.name, str(damage))})
            results.extend(target.fighter.take_damage(damage))
        else:
            results.append({'message': '{0} attacks {1} but does no damage.'.format(self.owner.name.capitalize(), target.name)})

        return results
