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

from urllib.request import urlopen
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location:')
# url = 'http://py4e-data.dr-chuck.net/comments_42.json'
data = urlopen(url, context=ctx).read()
num_characters = len(data)
info = json.loads(data)
# print(info)
sum = 0
co = 0
for item in info['comments']:
    count = item['count']
    sum += int(item['count'])
    co += 1
    # name = item['name']
print(f"Retrieving {url}")
print(f"Retrieved {num_characters} characters")
print(f"Count: {co}")
print(f"Sum: {sum}")