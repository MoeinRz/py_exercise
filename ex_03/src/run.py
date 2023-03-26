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

fname = input("Enter the file name: ")
try:
    fh = open(fname)
except:
    print("your input file does not found.")
    quit()
for line in fh:
    line = line.rstrip()
    print(line.upper())

