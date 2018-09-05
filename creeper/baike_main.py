# 爬取 百度百科 python相关词条
from baike_spider import url_manager, html_downloader, html_parser, html_parser, html_outputer

class SpiderMain(object):

    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, rout_url):
        count = 1
        self.urls.add_new_url(rout_url)

        while self.urls.has_new_url() and count < 2:
            try:
                new_url = self.urls.get_new_url()
                print('craw url count ', count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

            except:
                print('craw failed!')
            
            count = count + 1

        self.outputer.output_html()


if __name__ == '__main__':
    rout_url = 'https://baike.baidu.com/item/Python/407313?fr=aladdin'
    obj_spider = SpiderMain()
    obj_spider.craw(rout_url)
