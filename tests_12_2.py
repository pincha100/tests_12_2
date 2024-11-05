import unittest

# Подключаем необходимые классы для тестов
class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants[:]:  # Копия списка участников для итерации
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return finishers

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        # Создаем участников
        self.runner_usain = Runner("Usain", speed=10)
        self.runner_andrey = Runner("Andrey", speed=9)
        self.runner_nik = Runner("Nik", speed=3)

    @classmethod
    def tearDownClass(cls):
        for race_name, results in cls.all_results.items():
            readable_results = {place: runner.name for place, runner in results.items()}
            print(f"{race_name}: {readable_results}")

    def test_usain_nik_race(self):
        tournament = Tournament(90, self.runner_usain, self.runner_nik)
        results = tournament.start()
        self.__class__.all_results["Usain vs Nik"] = results
        self.assertTrue(list(results.values())[-1] == "Nik")

    def test_andrey_nik_race(self):
        tournament = Tournament(90, self.runner_andrey, self.runner_nik)
        results = tournament.start()
        self.__class__.all_results["Andrey vs Nik"] = results
        self.assertTrue(list(results.values())[-1] == "Nik")

    def test_full_race(self):
        tournament = Tournament(90, self.runner_usain, self.runner_andrey, self.runner_nik)
        results = tournament.start()
        self.__class__.all_results["Usain vs Andrey vs Nik"] = results
        self.assertTrue(list(results.values())[-1] == "Nik")

if __name__ == '__main__':
    unittest.main()
