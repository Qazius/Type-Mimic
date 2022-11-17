# pseudo code
# special = ""
# char = ""
# for char in text
# if " "
#    add to space
#    write special
# else #if not at space
#    if len(space) > 0: #if had space
#       while len(space) >= tabSize: #if have tab in space
#          write words
#          write tab
#          space = space.replace(" ", '', tabSize)
#       add space to word
#    if newline:
#       write word
#       write special
#       write newline #newline must be last
#    else if special
#       write word
#       add to special
#    else: #if letter (not newline or special or space)
#       write special
#       add to word

import pyautogui
import time

# put text here
text="""   }
   return group_info;

out_undo_partial_alloc:
   while (--a >= 0) {
      free_page((unsigned long)group_info->blocks[a]);
   }
   kfree(group_info);
   return NULL;
}

EXPORT_SYMBOL(groups_alloc);

void groups_free(struct group_info *group_info)
{
   if (group_info->blocks[0] != group_info->small_block) {
      int a;
      for (a = 0; a < group_info->nblocks; a++)
"""
# sample text from hacker typer

#list of delay characters, add to @delay_keys below
NEWLINE={"\n"}
SPECIAL_CHARS={'!','@','#','$','%','^','&','*','(',')','_','+','{','}','[',']','/',':',';','"','=','-'}

# add wait here for keys with unique delay
tabSize=3
typeInterval=0.08 #default 0.08
specialInterval=0.09 #default 0.09
waitTab=0.1 #default 0.1
waitWord=0.08 #changing to word #default 0.08
waitNewline=0.20 #default 0.2
waitSpecial=0.15 #changing to special #default 0.15

 #* write specials
def writeSpecials(specials):
   time.sleep(waitSpecial)
   pyautogui.write(specials, specialInterval)
   specials = ""
   return specials

#* write words
def writeWords(words):
   time.sleep(waitWord)
   pyautogui.write(words, typeInterval)
   words = ""
   return words

spaces = ""
specials = ""
words = ""
for char in text:
   if char == " ":
      spaces += char
      if len(specials) > 0:
         specials = writeSpecials(specials) #* write specials
   else:
      while len(spaces) >= tabSize:
         if len(words) > 0:
            words = writeWords(words) #* write words
         time.sleep(waitTab)
         pyautogui.press("tab") #* enter tab
         spaces = spaces.replace(" ", '', tabSize)
      if len(spaces) > 0:
         words += spaces
         spaces = ""
      if char in NEWLINE:
         if len(words) > 0:
            words = writeWords(words) #* write words
         if len(specials) > 0:
            specials = writeSpecials(specials) #* write specials
         time.sleep(waitNewline)
         pyautogui.write(char) #* enter newline
      elif char in SPECIAL_CHARS:
         if len(words) > 0:
            words = writeWords(words) #* write words
         specials += char
      else:
         if len(specials) > 0:
            specials = writeSpecials(specials) #* write specials
         words += char

# write the left over (last)
if len(words) > 0: #* write words
   words = writeWords(words)
elif len(specials) > 0: #* write specials
   specials = writeSpecials(specials)
elif len(spaces) > 0:
   while len(spaces) >= tabSize:
      time.sleep(waitTab)
      pyautogui.press("tab") #* enter tab
      spaces = spaces.replace(" ", '', tabSize)
   if len(spaces) > 0:
      words += spaces
      spaces = ""