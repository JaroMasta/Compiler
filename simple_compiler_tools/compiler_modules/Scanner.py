# -*- coding: utf-8 -*-
"""

NUMBER	"NUMBER"	Liczba całkowita lub zmiennoprzecinkowa ze znakiem

IDENTIFIER	"IDENTIFIER"	Identyfikator (np. zmienne, nazwy funkcji)

KEYWORD	"KEYWORD"	Słowo kluczowe (np. wyrażenia sterujące)

OPERATOR	"OPERATOR"	Operator arytmetyczny + - * / %

COMPARISON	"COMPARISON"	Operator porównania == != < > <= >=

ASSIGNMENT	"ASSIGNMENT"	Operator przypisania =

LOGICAL	"LOGICAL"	Operator logiczny &&, !, ||

LPAREN	"LPAREN"	Lewy nawias (

RPAREN	"RPAREN"	Prawy nawias )

LBRACE	"LBRACE"	Lewa klamra {

RBRACE	"RBRACE"	Prawa klamra }

SEMICOLON	"SEMICOLON"	Średnik ;

COMMA	"COMMA"	Przecinek ,

"""

class Scanner:

  # właściwa metoda skanera: Skanuje pojedynczy token i zwraca listę: [kod, wartość, indeks_za_tokenem]
  def scanner(self, line : str, p : int) -> list["token_key": str, "token_value" : str, "index_after_token" : int]:
    token_builder = ""
    token = False
    for letter_ind in range(p, len(line)):
      # jeżeli pod dodaniu znaku obecne wyrażenie nie będzie tokenem, a było nim bez modyfikacji (nie jest to więc pusty ciąg)
      if self.is_token(line, p, letter_ind, letter_ind) is None and len(token_builder) > 0:
        # jeżeli jest tokenem (bez dodawania kolejnego znaku)
        if self.is_token(line, p, letter_ind - 1, letter_ind) is not None:
          return self.is_token(line, p, letter_ind - 1, letter_ind)
        else:
          # nie jest poprawnym ciągiem
          return [f"ERROR in column {p}", token_builder, letter_ind]
      
      # jeżeli są jeszcze znaki na wejściu, to zobacz kolejny
      elif letter_ind < len(line):
        token_builder += line[letter_ind]
        # jeżeli jest to ostatni znak, to obsłuż koniec skanowania
        if letter_ind == len(line) - 1:
          if (self.is_token(line, p, letter_ind, letter_ind) in (None, False)):
            # nie jest poprawnym ciągiem
            if not token:
              return [f"ERROR in column {p}:", token_builder, letter_ind + 1]
            else:
              return self.is_token(line, p, letter_ind - 1, letter_ind)
          else:
            return self.is_token(line, p, letter_ind, letter_ind + 1)
      else:
        # nie jest poprawnym ciągiem
        return [f"ERROR in column {p}:", token_builder, letter_ind]


  # metoda do sprawdzenia czy ciąg jest tokenem danego rodzaju
  def is_token(self, line : str, start : int, end : int, letter_ind : int) -> bool | None:
    if line[start : end + 1] in self.value:
      (t1, t2) = self.value[line[start : end + 1]]
      return [t1, t2, letter_ind]
    else:
      if self.is_integer(line, start, end):
        return ["NUMBER", line[start : end + 1], letter_ind]
      if self.is_keyword(line[start : end + 1]):
        return ["KEYWORD", line[start : end + 1], letter_ind]
      if self.is_identifier(line[start : end + 1]):
        return ["IDENTIFIER", line[start : end + 1], letter_ind]
  

  # metoda do sprawdzania czy token jest liczbą
  def is_integer(self, line : str, start : int, end : int) -> bool:
      if not self.is_digit(line[start]):
        if line[start] in ('+', '-'):
          if start > 0:
            if line[start - 1] not in ('(', '/'):
              return False
        else:
          return False
      for l in line[start + 1 : end + 1]:
        if not self.is_digit(l):
            return False
      return True
  

  # metoda do sprawdzania czy ciąg należy do słów kluczowych
  def is_keyword(self, token) -> bool:
      return token in ["def", "return", "if", "else"]
  

  # metoda do sprawdzania czy ciąg spełnia warunki identyfikatora
  def is_identifier(self, lexeme : str) -> bool:
    if self.is_digit(lexeme[0]) or self.is_keyword(lexeme):
      return False
    for letter in lexeme:
      if not (self.is_letter(letter) or self.is_digit(letter) or letter in ('_')):
        return False
    return True
  

  # metoda do sprawdzania czy znak jest cyfrą
  def is_digit(self, char : str) -> bool:
      return '0' <= char <= '9'

  # metoda do sprawdzania czy znak jest literą
  def is_letter(self, char : str) -> bool:
      return 'a' <= char <= 'z'
  
  # metoda do pomijania spacji
  def clean_spaces(self, input : str) -> str:
    clean_input : str = ""
    for letter in input:
      if letter not in (' ', '\n'):
        clean_input += letter
    return clean_input

  # słownik operatorów
  value = {"+": ("Operator", "+"),
          "-": ("Operator", "-"),
          "*" : ("Operator", "*"),
          "/" : ("Operator", "/"),
          "(" : ("LPAREN", "("),
          ")" : ("RPAREN", ")"),
          "{" : ("LBRACE", "{"),
          "}" : ("RBRACE", "}"),
          "=" : ("ASSIGNMENT", "="),
          "==" : ("COMPARISON", "=="),
          "!=" : ("COMPARISON", "!="),
          "<" : ("COMPARISON", "<"),
          ">" : ("COMPARISON", ">"),
          "<=" : ("COMPARISON", "<="),
          ">=" : ("COMPARISON", ">="),
          "&&" : ("LOGICAL", "&&"),
          "||" : ("LOGICAL", "||")}