import logging

from IScore import IScore, PrefixSuffixScore
from logger import init_logger

test_cases = \
    [{'text': 'engine', 'prefix': 'raven', 'suffix': 'ginkgo', 'expected_score': 5, 'expected_pattern': 'engin'},
     {'text': 'nothing', 'prefix': 'bruno', 'suffix': 'ingenious', 'expected_score': 5, 'expected_pattern': 'nothing'},
     {'text': 'ab', 'prefix': 'b', 'suffix': 'a', 'expected_score': 1, 'expected_pattern': 'a'}
     ]


def test_prefix_suffix_score():
    init_logger(logging.INFO)
    test_score_engine: IScore = PrefixSuffixScore()

    for index in range(len(test_cases)):
        test_score_engine.configure(__prefix=test_cases[index]['prefix'],
                                    __suffix=test_cases[index]['suffix'])
        score_pattern, score = test_score_engine.calculate_text_score(test_cases[index]['text'])

        assert score_pattern == test_cases[index]['expected_pattern']
        assert score == test_cases[index]['expected_score']


if __name__ == '__main__':
    test_prefix_suffix_score()
