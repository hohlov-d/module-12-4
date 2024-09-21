import unittest
import logging
import module_12_4 as mod


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            h1 = mod.Runner('Tom', -3)
            h1.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError as err:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    def test_run(self):
        try:
            h2 = mod.Runner(1111, 5)
            h2.run()
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)



if __name__ == '__main__':
    unittest.main()
logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')
