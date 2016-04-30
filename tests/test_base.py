from unittest import TestCase

from rounds.base import Round, Subround, TargetType


class TestSubround(TestCase):
    def test_names(self):
        target_type = TargetType('60cm 10 zone')
        subround = Subround(arrows=60, per_end=3, distance=20, unit='yards', target_type=target_type)
        description = '60 arrows shot in 3s at 20 yards, 60cm 10 zone'
        self.assertEqual(str(subround), description)
        self.assertEqual(repr(subround), '<Subround: {}>'.format(description))

    def test_equality(self):
        target_type = TargetType('60cm 10 zone')
        one = Subround(arrows=60, per_end=3, distance=20, unit='yards', target_type=target_type)
        two = Subround(arrows=60, per_end=3, distance=20, unit='yards', target_type=target_type)
        self.assertEqual(one, two)


class TestRound(TestCase):
    def test_names(self):
        target_type = TargetType('60cm 10 zone')
        subround = Subround(arrows=60, per_end=3, distance=20, unit='yards', target_type=target_type)
        name = 'Portsmouth'
        portsmouth = Round(name, subrounds=[subround], scoring_type='AGB Indoor')
        self.assertEqual(str(portsmouth), name)
        self.assertEqual(repr(portsmouth), '<Round: {}>'.format(name))

    def test_equality_simple(self):
        target_type = TargetType('60cm 10 zone')
        subround = Subround(arrows=60, per_end=3, distance=20, unit='yards', target_type=target_type)
        portsmouth = Round('Portsmouth', subrounds=[subround], scoring_type='AGB Indoor')
        wallingford = Round('Wallingford', subrounds=[subround], scoring_type='AGB Indoor')
        self.assertEqual(portsmouth, wallingford)

    def test_equality_subrounds(self):
        target_type = TargetType('122cm 10 zone')
        eighty = Subround(arrows=72, per_end=6, distance=80, unit='yards', target_type=target_type)
        sixty = Subround(arrows=48, per_end=6, distance=60, unit='yards', target_type=target_type)
        fifty = Subround(arrows=24, per_end=6, distance=50, unit='yards', target_type=target_type)
        hereford = Round('Hereford', subrounds=[eighty, sixty, fifty], scoring_type='AGB imperial outdoor')
        bristol = Round('Bristol I', subrounds=[eighty, sixty, fifty], scoring_type='AGB imperial outdoor')
        self.assertEqual(hereford, bristol)
