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

fh = open("mbox-short.txt")
new_list = []
final = []
counts = {}
for line in fh:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    final.append(words[5])
for hour in final:
    new_list.append(hour[:2])
for name in new_list:
    counts[name] = counts.get(name, 0) + 1
sorted_dict = dict(sorted(counts.items()))
for key, value in sorted_dict.items():
    print(f"{key} {value}")
