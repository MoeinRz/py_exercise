# *************************************************************************** */
#                                                                             */
#                                                                             */
#    run.py                                                                   */
#                                                                             */
#    By: moeinrz <moeinrezaei330@gmail.com>                                   */
#                                                                             */
#    Created: 2023/03/26 11:04:59 by moeinrz                                  */
#    Updated: 2023/03/26 17:05:12 by moeinrz                                  */
#                                                                             */
# *************************************************************************** */

fh = open("mbox-short.txt")
new_list = []
final = []
count = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    print(words[1])
    count += 1
print("There were", count, "lines in the file with From as the first word")
