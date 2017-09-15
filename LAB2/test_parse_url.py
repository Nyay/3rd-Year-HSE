import pytest

import re
from parse_url import URLParser

tan = 'Простая до http://us.battle.net/sc2/en/blog/20944009 невозможного идея, до которой ' \
      'https://github.com/jachris/cook почему-то первым дошёл не Amazon, а интернет-магазин Boxed: они начали' \
      ' предлагать  https://techcrunch.com/2017/08/01/boxed-smart-stockup/ для дозаказа товары www.leningradspb.ru' \
      ' "регулярного потребления" на основе частоты ваших заказов.'


def test_upload():
    txt = URLParser(tan)
    assert txt.html_search() == ['http://us.battle.net', 'https://github.com', 'https://techcrunch.com', 'www.leningradspb.ru']