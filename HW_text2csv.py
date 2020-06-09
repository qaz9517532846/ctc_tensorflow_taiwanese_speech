import csv

read_text = open('output_2769.txt')

with open('output_2769.csv', 'w', newline='') as csvfile:
  # 建立 CSV 檔寫入器
  writer = csv.writer(csvfile)

  # 寫入一列資料
  writer.writerow(['id', 'text'])

  for line in read_text:
      line_result = line.split(' ', 1)
      print('Processing ID:' + line_result[0])
      writer.writerow([line_result[0], line_result[1]])

print('Finish')