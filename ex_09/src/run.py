# *************************************************************************** */
#                                                                             */
#                                                                             */
#    run.py                                                                   */
#                                                                             */
#    By: moeinrz <moeinrezaei330@gmail.com>                                   */
#                                                                             */
#    Created: 2023/04/27 20:04:23 by moeinrz                                  */
#    Updated: 2023/04/27 21:25:20 by moeinrz                                  */
#                                                                             */
# *************************************************************************** */

import re

fh = open("regex_sum_42.txt")
new_list = []
final = []
for line in fh:
    line = line.rstrip()
    if re.findall('[0-9]+', line):
        new_list.append(line)
count = 0
for i in new_list:
    final.append(re.findall('[0-9]+', i))
int_list = []
for sublist in final:
    for element in sublist:
        int_list.append(int(element))

print(f"There are {len(int_list)} values with a sum={sum(int_list)}")
