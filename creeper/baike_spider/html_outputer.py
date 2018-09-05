#-*- coding:utf-8 -*-
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
    
    def collect_data(self, new_data):
        if new_data is None:
            return
        self.datas.append(new_data)

    def output_html(self):
        fout = open('./creeper/baike_spider/output.html', 'w', encoding='utf-8')

        fout.write('<html>')
        fout.write(
            '<head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"></head>')
        fout.write('<body>')
        fout.write('<table>')
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' %
                       data['title'].encode('utf-8').decode("utf-8"))
            fout.write('<td>%s</td>' %
                       data['summary'].encode('utf-8').decode("utf-8"))
            fout.write('</td>')

        fout.write('</table>')
        fout.write('</table>')
        fout.write('</html>')

        fout.close()
