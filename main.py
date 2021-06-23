import logging

from IScore import IScore, PrefixSuffixScore
from logger import logger, init_logger

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    init_logger(logging.INFO)

    inputs = {}
    inputs_prompts = ['Please provide text: ', 'Please provide prefix: ', 'Please provide suffix: ']

    for i in range(len(inputs_prompts)):
        inputs[i] = (input(inputs_prompts[i]))

    text = inputs[0]
    prefix = inputs[1]
    suffix = inputs[2]

    score_engine: IScore = PrefixSuffixScore()
    score_engine.configure(__prefix=prefix, __suffix=suffix)
    score_pattern, score = score_engine.calculate_text_score(text)

    logger.info(f"Max prefix score for '{text}' prefix '{prefix}' and suffix '{suffix}' is '{score}', and the "
                f"pattern is '{score_pattern}'")
