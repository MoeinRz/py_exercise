# *************************************************************************** */
#                                                                             */
#                                                                             */
#    run.py                                                                   */
#                                                                             */
#    By: moeinrz <moeinrezaei330@gmail.com>                                   */
#                                                                             */
#    Created: 2023/03/05 11:04:59 by moeinrz                                  */
#    Updated: 2023/03/05 17:05:12 by moeinrz                                  */
#                                                                             */
# *************************************************************************** */

text = "X-DSPAM-Confidence:    0.8475"
pos = text.find(":")
l = len(text)
new = text[pos+1 : l]
new = float(new.strip())
print(new)
