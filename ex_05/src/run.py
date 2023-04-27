# *************************************************************************** */
#                                                                             */
#                                                                             */
#    run.py                                                                   */
#                                                                             */
#    By: moeinrz <moeinrezaei330@gmail.com>                                   */
#                                                                             */
#    Created: 2023/04/26 11:04:59 by moeinrz                                  */
#    Updated: 2023/04/26 17:05:12 by moeinrz                                  */
#                                                                             */
# *************************************************************************** */

fh = open("romeo.txt")
new_list = []
final = []
for line in fh:
    line = line.rstrip()
    new_list = line.split()
    for w in new_list:
        if w not in final:
            final.append(w)
final.sort()
print(final)
