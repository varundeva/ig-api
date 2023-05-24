def mask_phone(phone):
    return phone[:4] + '*' * (len(phone) - 4)
