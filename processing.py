def get_list_dict(user_dicts: list[dict], state_param: str = 'EXECUTED') -> list[dict]:
    new_dict: list[dict] = []
    for user_dict in user_dicts:
        if user_dict['state'] == state_param:
            new_dict.append(user_dict)
    return new_dict
