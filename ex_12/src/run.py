# *************************************************************************** */
#                                                                             */
#                                                                             */
#    run.py                                                                   */
#                                                                             */
#    By: moeinrz <moeinrezaei330@gmail.com>                                   */
#                                                                             */
#    Created: 2023/05/07 20:04:23 by moeinrz                                  */
#    Updated: 2023/05/07 21:25:20 by moeinrz                                  */
#                                                                             */
# *************************************************************************** */

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL:')
# url = 'https://py4e-data.dr-chuck.net/known_by_Fikret.html'
repeat = int(input('Enter count:'))
pos = int(input ('Enter position:'))
pos = pos - 1
for i in range(repeat):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    # print('TAG:', tag)
    url = tags[pos].get('href')
    name = tags[pos].contents[0]
    # print('URL:', tag.get('href', None))
    # print('TAG:', tag)
print(name)

