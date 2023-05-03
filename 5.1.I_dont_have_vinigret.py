import datetime
import random
import re


def get_date():
    """
    get date from user
    :return: date in string format
    """
    date = input("Enter date (yyyy-mm-dd): ")
    while not re.match(r"^\d{4}-\d{2}-\d{2}$", date):
        date = input("Wrong date format, try again: ")
    return date


def get_date_array(date):
    """
    get date in string format and return it as array
    :param date: date in string format
    """
    return [int(x) for x in date.split("-")]


def main():
    """
    main function
    """
    try:
        # read data
        start_date = get_date_array(get_date())
        end_date = get_date_array(get_date())
        # change the string to date-time type
        start = datetime.datetime(*start_date)
        end = datetime.datetime(*end_date)

        if end < start:
            raise Exception("End date cannot be before start date")

        days = datetime.timedelta(days=random.randrange((end - start).days))
        print(start + days)

    except Exception as e:
        print(str(e))


if __name__ == '__main__':
     main()
