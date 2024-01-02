from datetime import datetime


def ontrack_reading(books_goal: int, books_read: int,
                    day_of_year: int = None) -> bool:

    
    if day_of_year is None:
        day_of_year = int(datetime.now().strftime("%j"))

    books_left = books_goal - books_read
    if books_left <= 0:
        return True

    days_per_book = 365/books_goal


    days_left = 365 - day_of_year

    rate = days_left/books_left

    return rate > days_per_book







