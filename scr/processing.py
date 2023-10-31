def get_list_dict(user_dicts: list[dict], state_param: str = "EXECUTED") -> list[dict]:
    new_dict: list[dict] = []
    for user_dict in user_dicts:
        if user_dict["state"] == state_param:
            new_dict.append(user_dict)
    return new_dict


def get_list_data_dict(user_dicts: list[dict], sort_order: bool = False) -> list[dict]:
    new_dict: list[dict] = []
    if sort_order:
        new_dict = sorted(user_dicts, key=lambda x: x["date"])
    else:
        new_dict = sorted(user_dicts, key=lambda x: x["date"], reverse=True)
    return new_dict
