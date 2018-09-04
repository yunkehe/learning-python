# 
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
    
    def collect_data(self, new_data):
        if new_data is None:
            return
        self.datas.append(new_data)

    def output_html(self):
        fout = open('output.html', 'w')

        fout.write('<b>')
        fout.write('<t>')
        fout.write('<td>')
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title'].encode('utf-8'))
            fout.write('<td>%s</td>' % data['summary'].encode('utf-8'))
            fout.write('</td>')

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')

        fout.close()
