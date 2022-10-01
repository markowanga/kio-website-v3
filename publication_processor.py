import unidecode

Line = 'title={Parallel processing of large graphs},'
AUT = 'author={Tuligłowicz, Włodzimierz J. and Augustyniak, Łukasz M. and Szymański, Piotr and Kajdanowicz, Tomasz},'
year_line = 'year={2017},'


def get_first_surname_from_line(text: str) -> str:
  return unidecode.unidecode(text.replace('author={', '').strip().split(',')[0]).lower()


def extract_title_from_line(text: str) -> str:
  base_name = unidecode.unidecode(text.replace('title={', '').strip().split(',')[0]).lower()
  return [it for it in base_name.split(' ') if len(it) >= 5][0]


def extract_year_from_line(text: str) -> str:
  return text.replace('year={', '').strip()[:-2]


if __name__ == '__main__':
  print(extract_year_from_line(year_line))
  print(get_first_surname_from_line(AUT))
  print(extract_title_from_line(Line))
