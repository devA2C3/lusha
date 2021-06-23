import abc

import constants
from logger import logger
from string_utils import slice_right, slice_left


class IScore(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def configure(self, **kwargs):
        """Use it to configure the Score instance"""
        raise NotImplementedError("Please implement 'configure' method")

    @abc.abstractmethod
    def calculate_text_score(self, text: str) -> int:
        """Calculates the given text score and return it"""
        raise NotImplementedError("Please implement 'calculate_text_score' method")


class PrefixSuffixScore(IScore):

    def __init__(self):
        self.__suffix = constants.INVALID_SUFFIX
        self.__prefix = constants.INVALID_PREFIX
        self.__all_scores = {}

    def configure(self, **kwargs):
        # In real world would do it with more verifications
        for key, value in kwargs.items():
            if key == "__prefix":
                self.__prefix = value
            elif key == "__suffix":
                self.__suffix = value

    def calculate_text_score(self, text):

        logger.debug(f"Calculating text score for string '{text}', prefix '{self.__prefix}' suffix '{self.__suffix}'")

        self.__all_scores = {}

        for start_index in range(0, len(text)):
            for end_index in range(start_index + 1, len(text) + 1):
                current_substring = text[start_index:end_index]
                logger.debug(f"Checking the substring '{current_substring}'")

                prefix_score = self.__get_current_prefix_score(current_substring, self.__prefix)

                suffix_score = self.__get_current_suffix_score(current_substring, self.__suffix)

                current_text_score = prefix_score + suffix_score
                self.__store_current_score(current_substring, current_text_score)

        return self.__calculate_final_score()

    def __get_current_prefix_score(self, substring, prefix):
        # calc the pre_text_pattern_score
        score = min(len(prefix), len(substring))

        logger.debug(f"Max possible prefix score for '{substring}' and prefix '{prefix}' is {score}")

        while score > 0 and slice_right(substring, score) != slice_left(prefix, score):
            score -= 1

        pattern = slice_right(prefix, score)
        logger.debug(f"Prefix score for string '{substring}' and prefix '{prefix}' is {score} for pattern '{pattern}'")

        return score

    def __get_current_suffix_score(self, substring, suffix):

        score = min(len(suffix), len(substring))
        logger.debug(f"Max possible suffix score for '{substring}' and suffix '{suffix}' is {score}")

        while score > 0 and slice_left(substring, score) != slice_right(suffix, score):
            score -= 1

        pattern = slice_right(suffix, score)
        logger.debug(f"Suffix score for '{substring}' and suffix '{suffix}' is {score} for pattern '{pattern}'")

        return score

    def __store_current_score(self, substring, text_score):
        if not text_score in self.__all_scores:
            self.__all_scores[text_score] = []

        logger.debug(f"Appending substring '{substring}' to the prefix score '{text_score}'")
        self.__all_scores[text_score].append(substring)

    def __calculate_final_score(self):

        result = constants.INVALID_RESULT

        maximum_pattern_score = max(self.__all_scores.keys())
        all_patterns_with_score = self.__all_scores[maximum_pattern_score]
        if len(all_patterns_with_score) > 1:
            all_patterns_with_score.sort()

        result = all_patterns_with_score[0]

        return result, maximum_pattern_score
