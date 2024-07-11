from uuid import UUID


def get_organisation_id_ok():
    return UUID('12345678-1234-5678-1234-567812345678')


def get_organisation_id_not_found():
    return UUID('12345678-1234-5678-1234-567812345678')
