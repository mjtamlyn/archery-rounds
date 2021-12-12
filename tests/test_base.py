from unittest import TestCase

from rounds.base import Round, Pass, TargetType


class TestPass(TestCase):
    def test_names(self):
        target_type = TargetType('60cm 10 zone')
        pass_1 = Pass(arrows=60, per_end=3, distance=20, unit='yards', target_type=target_type)
        description = '60 arrows shot in 3s at 20 yards, 60cm 10 zone'
        self.assertEqual(str(pass_1), description)

    def test_equality(self):
        target_type = TargetType('60cm 10 zone')
        one = Pass(arrows=60, per_end=3, distance=20, unit='yards', target_type=target_type)
        two = Pass(arrows=60, per_end=3, distance=20, unit='yards', target_type=target_type)
        self.assertEqual(one, two)

    def test_comparable(self):
        target_type = TargetType('60cm 10 zone')
        one = Pass(arrows=60, per_end=3, distance=20, unit='yards', target_type=target_type)
        two = Pass(arrows=30, per_end=6, distance=20, unit='yards', target_type=target_type)
        self.assertTrue(one.is_comparable(two))
        self.assertTrue(two.is_comparable(one))


class TestRound(TestCase):
    def test_names(self):
        target_type = TargetType('60cm 10 zone')
        pass_1 = Pass(arrows=60, per_end=3, distance=20, unit='yards', target_type=target_type)
        name = 'Portsmouth'
        portsmouth = Round(name, passes=[pass_1], scoring_type='AGB Indoor')
        self.assertEqual(str(portsmouth), name)

    def test_equality_simple(self):
        target_type = TargetType('60cm 10 zone')
        pass_1 = Pass(arrows=60, per_end=3, distance=20, unit='yards', target_type=target_type)
        portsmouth = Round('Portsmouth', passes=[pass_1], scoring_type='AGB Indoor')
        wallingford = Round('Wallingford', passes=[pass_1], scoring_type='AGB Indoor')
        self.assertEqual(portsmouth, wallingford)

    def test_equality_passes(self):
        target_type = TargetType('122cm 10 zone')
        eighty = Pass(arrows=72, per_end=6, distance=80, unit='yards', target_type=target_type)
        sixty = Pass(arrows=48, per_end=6, distance=60, unit='yards', target_type=target_type)
        fifty = Pass(arrows=24, per_end=6, distance=50, unit='yards', target_type=target_type)
        hereford = Round('Hereford', passes=[eighty, sixty, fifty], scoring_type='AGB imperial outdoor')
        bristol = Round('Bristol I', passes=[eighty, sixty, fifty], scoring_type='AGB imperial outdoor')
        self.assertEqual(hereford, bristol)

    def test_equality_normalization_needed(self):
        target_type = TargetType('60cm 10 zone')
        full = Pass(arrows=60, per_end=3, distance=20, unit='yards', target_type=target_type)
        half = Pass(arrows=30, per_end=3, distance=20, unit='yards', target_type=target_type)
        portsmouth = Round('Portsmouth', passes=[full], scoring_type='AGB Indoor')
        wallingford = Round('2x20y', passes=[half, half], scoring_type='AGB Indoor')
        self.assertEqual(portsmouth, wallingford)
