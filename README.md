Archery rounds
==============

Python library providing definitions of archery rounds.

```python
>>> from rounds.wa import wa_1440_90
>>> wa_1440_90
... <Round: World Archery 1440 round (90m)>
>>> wa_1440_90.scoring_type
... <Scoring: WA Outdoors (Xs, 10+X)>
>>> wa_1440_90.arrows
... 144
>>> wa_1440_90.subrounds
... [
...     <Subround: 36 arrows shot in 6s at 90m on a 122cm face>,
...     <Subround: 36 arrows shot in 6s at 70m on a 122cm face>,
...     <Subround: 36 arrows shot in 3s at 50m on a 80cm face>,
...     <Subround: 36 arrows shot in 3s at 30m on a 80cm face>,
... ]
>>> wa_1440_90.subrounds[0].target_type
... <Target: 122cm 10 zone WA target face>
>>> wa_1440_90.variants
... {
...     'shot-in-6s': <RoundVariant: 6 arrow ends at 50m and 30m>,
...     '30m-spot': <RoundVariant: Spot face at 30m>,
...     '50m-30m-spot': <RoundVariant: Spot faces at 50m and 30m>,
...     # ...
... }
>>> wa_1440_90.related_rounds
... [
...     <Round: Double World Archery 1440 round (90m)>
...     <Round: World Archery 1440 round (70m)>
...     <Round: World Archery 1440 round (60m)>
...     <Round: Archery GB Metric III (50m)>
...     <Round: Archery GB Metric IV (40m)>
...     <Round: Archery GB Metric V (30m)>
... ]
```
