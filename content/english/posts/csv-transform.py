import csv

with open('catalog2.csv') as csv_file:
   csv_reader=csv.DictReader(csv_file)
   line_count = 0
   for row in csv_reader:
     with open(f'{row["Инвентаризационный номер"]}.md', 'w') as tgt:
       title = row["Название модели, книги"]
       title = title.strip()
       title = title.replace("\n"," ")
       tgt.write('+++\n')
       if '\'' in title:
          tgt.write(f'title = "{title}"\n')
       else:
          tgt.write(f'title = \'{title}\'\n')
       data = row["Год производства, начало выпуска модели"]
       if data and data.strip().isdigit():
          tgt.write(f'date = {data}-01-01\n')
       if "Примечание" in row:
         descr = row["Примечание"].strip()
         if descr:
            descr = descr.strip()
            descr = descr.replace("\n", " ")
            tgt.write(f'description = \'{descr}\'\n')
       tgt.write(f'categories = ["{row["Категория"].strip()}"]\n')
       tgt.write(f'tags = ["{row["Страна производитель"].strip()}"]\n')
       tgt.write('+++\n\n')
       for key, value in row.items():
         if value:
           value = value.strip()
           tgt.write(f'{key}: {value}\n\n')
