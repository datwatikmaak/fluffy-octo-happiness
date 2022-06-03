names = "Julian Bob PyBites Dante Martin Rodolfo".split()
countries = "Australia Spain Global Argentina USA Mexico".split()


def enumerate_names_countries():
    """Outputs:
    1. Julian     Australia
    2. Bob        Spain
    3. PyBites    Global
    4. Dante      Argentina
    5. Martin     USA
    6. Rodolfo    Mexico"""
    print(
        "\n".join(
            [
                f"{i}. {name:<10} {country}"
                for i, (name, country) in enumerate(zip(names, countries), 1)
            ]
        )
    )


enumerate_names_countries()
