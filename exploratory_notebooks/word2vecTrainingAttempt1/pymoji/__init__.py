#!/usr/bin/env python3

import re

from .codes import codes

class Emoji:
  def __init__(self, const):
    if len(const) == 1:
      self.__fromUnicode(const)
    elif const[0] == ":":
      self.__fromAlias(const)
    else:
      self.__fromEscape(const)
    self.aliases = codes[self.escape]
    self.alt_alias = self.aliases[0].replace(":", "__")
    self.alias = self.aliases[0]
    self.char = bytes("\\u"+self.escape, "ascii").decode("unicode-escape")[0]
    self.is_supported = hex(ord(self.char))[2:] == self.escape

  def __fromUnicode(self, char):
    escape = hex(ord(char))[2:]
    if escape in codes:
      self.escape = escape
    else:
      raise ValueError

  def __fromAlias(self, alias):
    for k, v in codes.items():
      if alias in v:
        self.escape = k
        break
    else:
      raise ValueError

  def __fromEscape(self, escape):
    if escape in codes.keys():
      self.escape = escape
    else:
      raise ValueError

def replaceAliases(text, trailingSpaces=0, force=False):
  """ Replaces all supported emoji-cheat-sheet aliases in a text with the corresponding emoji. """
  def replAlias(m):
    alias = ":"+m.group(1)+":"
    if not Emoji(alias).is_supported and not force:
      return alias
    try:
      return Emoji(alias).char + trailingSpaces * " "
    except ValueError:
      return alias
  return re.sub(":([^s:]?[\w-]+):", replAlias, text)

def replaceEmoji(text, trailingSpaces=0):
  """ Replaces all emojis with their primary emoji-cheat-sheet alias. """
  i = 0
  while i < len(text):
    escape = hex(ord(text[i]))[2:]
    if escape in codes.keys():
      text = text.replace(text[i] + trailingSpaces*" ", Emoji(escape).alias)
      i += len(Emoji(escape).alias)
    else:
      i += 1
  return text
def replaceEmojiAlt(text, trailingSpaces=0):
  """ Replaces all emojis with their primary emoji-cheat-sheet alias. """
  i = 0
  while i < len(text):
    escape = hex(ord(text[i]))[2:]
    if escape in codes.keys():
      text = text.replace(text[i], Emoji(escape).alt_alias + trailingSpaces*" ")
      i += len(Emoji(escape).alt_alias)
    else:
      i += 1
  return text
