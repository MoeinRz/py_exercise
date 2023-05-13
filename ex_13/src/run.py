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

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location:')
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
tree = ET.fromstring(data)
results = tree.findall('.//count')

sum = 0
for item in results:
    sum += int(item.text)
print(f'Sum: {sum}')

