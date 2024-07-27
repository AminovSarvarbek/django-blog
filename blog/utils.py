from itertools import groupby
from operator import attrgetter


def blog_list_by_year_month(blogs):
    key_func = lambda x: (x.date.year, x.date.month)
    blogs = sorted(blogs, key=key_func, reverse=True)
    return {key: list(group) for key, group in groupby(blogs, key_func)}