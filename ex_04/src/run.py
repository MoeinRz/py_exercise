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
avrage = 0.0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    pos = line.find(":")
    l = len(line)
    new = line[pos+1 : l]
    new = float(new.strip())
    avrage += new
    count = count + 1
avrage = avrage / count
print(f"Average spam confidence: {avrage}")
