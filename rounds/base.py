import copy

import attr


@attr.s
class TargetType(object):
    name = attr.ib()

    def __str__(self):
        return self.name


@attr.s
class Pass(object):
    arrows = attr.ib(type=int)
    per_end = attr.ib(type=int)
    distance = attr.ib(type=int)
    unit = attr.ib(type=str)
    target_type = attr.ib()

    def __str__(self):
        return "{arrows} arrows shot in {per_end}s at {distance} {unit}, {target_type}".format(
            **self.__dict__
        )

    def is_comparable(self, other):
        return (
            isinstance(other, Pass)
            and self.distance == other.distance
            and self.unit == other.unit
            # TODO: this line needs to be one category higher, or we need face types within target_type
            # e.g. 40cm Spots == 40cm full face
            # but Bray != Portsmouth
            and self.target_type == other.target_type
        )


def normalize_passes(passes):
    """Collate passes with only one pass per setup."""
    # TODO: Also normalise distance order?
    normalized = []
    current = None
    for sr in passes:
        if current is None or not current.is_comparable(sr):
            normalized.append(copy.copy(sr))
        else:
            normalized[-1].arrows += sr.arrows
        current = sr
    return normalized


@attr.s
class Round(object):
    name = attr.ib(type=str, eq=False)
    passes = attr.ib(eq=normalize_passes)
    scoring_type = attr.ib()

    def __str__(self):
        return self.name
