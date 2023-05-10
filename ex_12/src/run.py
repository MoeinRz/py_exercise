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

# url = input('Enter - ')
url = 'https://py4e-data.dr-chuck.net/known_by_Fikret.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')
count = 0
sum = 0
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    # print('URL:', tag.get('href', None))
    count += 1
    # sum += int(tag.contents[0])
    # print('Contents:', tag.contents[0])
    # print('Attrs:', tag.attrs)
# print(f"Count {count}")
# print(f"Sum {sum}")