def get_user_info(request):
    """
    Function that gets the information about the user that made the http request
    :param request: an HttpRequest object
    :return a dictionary with information about the user
    """
    user = request.user
    user_groups = [group.name for group in user.groups.all()]

    if 'admin' in user_groups:
        user_type = 'admin'
    elif 'transportator' in user_groups:
        user_type = 'transportator'
    else:
        user_type = 'client'

    out = {'user': user,
           'user_groups': user_groups,
           'user_type': user_type
           }

    return out


def create_context(request=None, extract_user_info=True):
    """
    Function that creates the context with needed information
    :param request: HttpRequest object, default value is None
    :extract_user: boolean that indicates if the user_info should be added to the result, default value is True
    :return a dictionary with all the extracted fields
    """
    if extract_user_info and not request:
        raise ValueError("request must be set if extract_user_info is True")

    out = {}

    if extract_user_info:
        out.update(get_user_info(request))

    return out
