def get_profile(*, name="julian", profession="programmer"):
    return f"{name} is a {profession}"


kwargs = {"name": "julian", "profession": "programmer"}

print(get_profile(**kwargs))
