def main():
  with open("./books/frankenstein.txt") as f:
    file_contents = f.read()

    print_report(file_contents, condition=lambda c: c.isalpha())

def count_words(str):
  if len(str) > 0:
    return len(str.split())
  else:
    return 0

def count_chars(char, str):
  count = 0

  for c in str:
    if c == char:
      count += 1

  return count

def make_char_dictionary(str):
  formatted_str = str.lower()
  if len(formatted_str) <= 0:
    return 0

  dict_list = []

  char_list = set(formatted_str)

  for char in char_list:
    dict_list.append({"name": char, "count": count_chars(char, formatted_str)})

  dict_list.sort(key=lambda d : d['count'], reverse=True)

  return dict_list

def print_report(text, condition):
  print(f"{count_words(text)} words found in the document")
  print("\n")

  dict_list = make_char_dictionary(text)

  for item in dict_list:
    if condition and not(condition(item['name'])):
      continue
    print(f"The '{item['name']}' character was found {item['count']}")


main()