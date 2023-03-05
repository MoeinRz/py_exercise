# *************************************************************************** */
#                                                                             */
#                                                                             */
#    run.py                                                                   */
#                                                                             */
#    By: moeinrz <moeinrezaei330@gmail.com>                                   */
#                                                                             */
#    Created: 2023/02/06 20:04:59 by moeinrz                                  */
#    Updated: 2022/02/07 14:05:12 by moeinrz                                  */
#                                                                             */
# *************************************************************************** */

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        fnum = int(num)
    except:
        print('Invalid input')
        continue
    if (largest == None) or (smallest == None):
        largest = fnum
        smallest = fnum
    if largest < fnum:
        largest = fnum
    if smallest > fnum:
        smallest = fnum

print("Maximum is", largest)
print("Minimum is", smallest)
