import copy


class TargetType(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Target: {}>'.format(self.name)


class Subround(object):
    def __init__(self, arrows, per_end, distance, unit, target_type):
        self.arrows = arrows
        self.per_end = per_end
        # TODO: look at using a distances lib
        # would allow 90m < 100y
        self.distance = distance
        self.unit = unit
        self.target_type = target_type

    def __str__(self):
        return '{arrows} arrows shot in {per_end}s at {distance} {unit}, {target_type}'.format(**self.__dict__)

    def __repr__(self):
        return '<Subround: {}>'.format(str(self))

    def __eq__(self, other):
        return (
            isinstance(other, Subround)
            and self.arrows == other.arrows
            and self.distance == other.distance
            and self.unit == other.unit
            # TODO: this line needs to be one category higher, or we need face types within target_type
            # e.g. 40cm Spots == 40cm full face
            # but Bray != Portsmouth
            and self.target_type == other.target_type
        )

    def is_comparable(self, other):
        return (
            isinstance(other, Subround)
            and self.distance == other.distance
            and self.unit == other.unit
            # TODO: this line needs to be one category higher, or we need face types within target_type
            # e.g. 40cm Spots == 40cm full face
            # but Bray != Portsmouth
            and self.target_type == other.target_type
        )


class Round(object):
    def __init__(self, name, subrounds, scoring_type):
        self.name = name
        # TODO: name variants/short_name
        self.subrounds = subrounds
        self.scoring_type = scoring_type

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Round: {}>'.format(self.name)

    def __eq__(self, other):
        """Two rounds are equal if they involve the same number of arrows, at the same faces, with the same rules."""
        if not isinstance(other, Round):
            return False
        subrounds = self.normalized_subrounds()
        other_subrounds = other.normalized_subrounds()
        return (
            self.scoring_type == other.scoring_type
            and subrounds == other_subrounds
        )

    def normalized_subrounds(self):
        """Collate subrounds with only one subround per setup."""
        # TODO: Also normalise distance order?
        normalized = []
        current = None
        for sr in self.subrounds:
            if current is None or not current.is_comparable(sr):
                normalized.append(copy.copy(sr))
            else:
                normalized[-1].arrows += sr.arrows
            current = sr
        return normalized
