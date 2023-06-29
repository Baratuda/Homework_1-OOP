
import re
def validate_phone_number(number_len):
    def decorator(func):
        def inner(*args, **kwargs):
            new_args = []
            for arg in args:
                new_arg = None
                result = len(re.findall(r'^\+375\d{2}\d{7}',arg))
                if result != 0 and len(arg)==number_len:
                    new_arg = arg
                new_args.append(new_arg)
            res = func(*new_args, **kwargs)
            return res
        return inner
    return decorator


@validate_phone_number(number_len = 13)
def register_phone_number(phone1, phone2):
     return phone1,phone2


print(register_phone_number('+375445466680','+375445784523'))