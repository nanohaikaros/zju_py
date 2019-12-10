seg1 = '''
<!DOCTYPE html>\n<html>\n<body>\n<meta charset="gb1312">
<h2 align="center">2016年7月部分大中城市新建住宅价格指数</h2>
<tr bgcolor="orange">
'''

seg2 = "</tr>\n"
seg3 = "</table>\n</body>\n</html>"
def fill_data(locls):
    seg = '<tr><td align="center">{}</td><td align="center">\
          {}</td><td align="center">{}</td><td align+"center">\
          {}</td></tr>\n'.format(*locls)
fr = open("price2016.csv", "r")
ls = []
for line in fr:
    line = line.replace("\n", "")
    ls.append(line.split(","))
fr.close()
fw = open("price2016.html", "w")
fw.write(seg1)
fw.write('<th width="25%">{}</th>\n<th width="25%">{}</th>\n<th width="25%">{}</th>\n<th width="25%">{}</th>\n'.format(*ls[0]))
fw.write(seg2)
for i in range(len(ls)-1):
    fw.write(fill_data(ls[i+1]))
fw.write(seg3)
fw.close()