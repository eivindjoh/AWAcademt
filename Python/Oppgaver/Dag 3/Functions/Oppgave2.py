def bart_cheat_code(punishment_text: str, numb_of_repetition: int = 10) -> str:
    """
    Returns blackboard

    :param punishment_text: string
    :param numb_of_repetition: integar
    :return: string
    """
    text = (punishment_text + '\n') * numb_of_repetition
    return text

print(bart_cheat_code('I am punished', 4))
