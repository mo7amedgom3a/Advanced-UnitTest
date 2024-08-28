def catgorize_age(age):
    if age < 18:
        return 'child'
    elif age < 65:
        return 'adult'
    else:
        return 'senior'

