import urllib.parse as urlparse
import re
import bs4
BeautifulSoup = bs4.BeautifulSoup

class HtmlParser(object):

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/item/.*"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin('https://baike.baidu.com', new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        # <dd class = "lemmaWgt-lemmaTitle-title" >
        # <h1 > Python < /h1 >
        res_data = {}
        res_data['url'] = page_url

        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
        res_data['title'] = title_node.get_text()

        # <div class="lemma-summary" label-module="lemmaSummary">
        # <div class = "para" label-module = "para" > Python 是一个有条理的和强大的面向对象的程序设计语言，类似于Perl, Ruby, Scheme, 或 Java. < /div >
        # </div >
        summary_node = soup.find('div', class_="lemma-summary").find('div')
        res_data['summary'] = summary_node.get_text()

        return res_data

    
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return 

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data
