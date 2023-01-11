from ariadne import convert_kwargs_to_snake_case

from controllers import VerificationController


@convert_kwargs_to_snake_case
def verify_resolver(_, info, password, rules):
    return VerificationController(password=password, rules=rules).execute()
