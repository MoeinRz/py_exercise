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
    final.append(words[1])
for name in final:
    counts[name] = counts.get(name, 0) + 1
max_key = max(counts, key=counts.get)
max_value = counts[max_key]
print(f"{max_key} {max_value}")
