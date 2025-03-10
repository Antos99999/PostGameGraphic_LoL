import unittest


def process_timeline(timeline):
    VoidGrubsCounter = 0
    BlueVoidsGrubs = 0
    RedVoidsGrubs = 0
    BlueMonsters = 0
    RedMonsters = 0
    FirstVoidBrubs = False
    SecondVoidBrubs = False
    blue3Monsters = False
    red3Monsters = False

    for frame in timeline['info']['frames']:
        for evt in frame['events']:
            if not blue3Monsters and not red3Monsters:
                if evt["type"] == "ELITE_MONSTER_KILL" and evt["monsterType"] == "HORDE":
                    if evt["teamId"] == 100:
                        VoidGrubsCounter += 1
                        BlueVoidsGrubs += 1
                        if VoidGrubsCounter == 3:
                            FirstVoidBrubs = True
                        if VoidGrubsCounter == 6:
                            SecondVoidBrubs = True
                        if FirstVoidBrubs and BlueVoidsGrubs == 3:
                            BlueMonsters += 1
                        if FirstVoidBrubs:
                            FirstVoidBrubs = False
                            BlueVoidsGrubs = 0
                            RedVoidsGrubs = 0
                        if SecondVoidBrubs and BlueVoidsGrubs == 3:
                            BlueMonsters += 1
                    elif evt["teamId"] == 200:
                        VoidGrubsCounter += 1
                        RedVoidsGrubs += 1
                        if VoidGrubsCounter == 3:
                            FirstVoidBrubs = True
                        if VoidGrubsCounter == 6:
                            SecondVoidBrubs = True
                        if FirstVoidBrubs and RedVoidsGrubs == 3:
                            RedMonsters += 1
                        if FirstVoidBrubs:
                            FirstVoidBrubs = False
                            RedVoidsGrubs = 0
                            BlueVoidsGrubs = 0
                        if SecondVoidBrubs and RedVoidsGrubs == 3:
                            RedMonsters += 1

    return BlueMonsters, RedMonsters


class TestProcessTimeline(unittest.TestCase):

    def test_single_blue_kill(self):
        timeline = {'info': {'frames': [{'events': [{
            'type': 'ELITE_MONSTER_KILL', 'monsterType': 'HORDE', 'teamId': 100
        }]}]}}
        self.assertEqual((0,0),process_timeline(timeline))

    def test_three_blue_kills(self):
        timeline = {'info': {'frames': [{'events': [{
            'type': 'ELITE_MONSTER_KILL', 'monsterType': 'HORDE', 'teamId': 100
        }] * 3}]}}
        self.assertEqual((1, 0),process_timeline(timeline))

    def test_six_red_kills(self):
        timeline = {'info': {'frames': [{'events': [{
            'type': 'ELITE_MONSTER_KILL', 'monsterType': 'HORDE', 'teamId': 200
        }] * 6}]}}
        self.assertEqual((0,2), process_timeline(timeline))

    def test_mixed_kills(self):
        timeline = {'info': {'frames': [{'events': [
            {'type': 'ELITE_MONSTER_KILL', 'monsterType': 'HORDE', 'teamId': 100},
            {'type': 'ELITE_MONSTER_KILL', 'monsterType': 'HORDE', 'teamId': 100},
            {'type': 'ELITE_MONSTER_KILL', 'monsterType': 'HORDE', 'teamId': 100},
            {'type': 'ELITE_MONSTER_KILL', 'monsterType': 'HORDE', 'teamId': 100},
            {'type': 'ELITE_MONSTER_KILL', 'monsterType': 'HORDE', 'teamId': 100},
            {'type': 'ELITE_MONSTER_KILL', 'monsterType': 'HORDE', 'teamId': 100},
        ]}]}}
        self.assertEqual((2, 0), process_timeline(timeline))

        if __name__ == "__main__":
            unittest.main()
