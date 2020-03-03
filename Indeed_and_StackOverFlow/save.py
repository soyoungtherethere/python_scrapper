import csv

def save_to_file(jobs):
  file = open("jobs.csv", mode="w") #파일을 열어 변수 file에 저장
  writer = csv.writer(file) #방금 연 파일에 csv를 작성하겠다
  writer.writerow(["title", "company", "location", "link"])
  for job in jobs:
    writer.writerow(list(job.values()))
  return