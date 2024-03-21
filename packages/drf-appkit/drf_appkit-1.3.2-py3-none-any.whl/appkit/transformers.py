def img_src(image_attachment, size):
    image = image_attachment.image

    if not image_attachment.warm:
        return image.url

    try:
        return image.thumbnail[size].url
    except KeyError:
        return image.url


def to_choices(choice_list, nullable=False):
    choices = []
    for item in choice_list:
        if isinstance(item, tuple):
            choice = {'value': str(item[0]), 'label': str(item[1])}
        else:
            choice = {'value': str(item), 'label': str(item)}
        choices.append(choice)

    if nullable:
        choices.insert(0, { 'label': '--- None ---', 'value': 'null' })

    return choices
