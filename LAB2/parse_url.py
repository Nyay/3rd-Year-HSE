import re

tan = 'Простая до http://us.battle.net/sc2/en/blog/20944009 невозможного идея, до которой ' \
      'https://github.com/jachris/cook почему-то первым дошёл не Amazon, а интернет-магазин Boxed: они начали' \
      ' предлагать  https://techcrunch.com/2017/08/01/boxed-smart-stockup/ для дозаказа товары www.leningradspb.ru' \
      ' "регулярного потребления" на основе частоты ваших заказов.'


class URLParser:

    def __init__(self, argument):
        self.text = argument
        self.html_links = []

    def html_search(self):
        self.html_links = re.findall('(?:(?:www\.)|(?:https?:\/\/))(?:[\w\.]+)\.(?:[a-z]{2,6}\.?)', self.text)
        return self.html_links

    def __repr__(self):
        return str(self.html_links)

txt = URLParser(tan)
