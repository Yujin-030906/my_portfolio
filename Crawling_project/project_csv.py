import pandas as pd

df1 = pd.read_csv("hyundai_jobs.csv", engine = 'python', quotechar = '"', on_bad_lines = 'skip')
df2 = pd.read_csv("hyundai_jobs1.csv", engine = 'python', quotechar = '"', on_bad_lines = 'skip')
df3 = pd.read_csv("hyundai_jobs2.csv", engine = 'python', quotechar = '"', on_bad_lines = 'skip')
df4 = pd.read_csv("saramin_1.csv", engine = 'python', quotechar = '"', on_bad_lines = 'skip')
df5 = pd.read_csv("saramin_2.csv", engine = 'python', quotechar = '"', on_bad_lines = 'skip')
df6 = pd.read_csv("saramin_3.csv", engine = 'python', quotechar = '"', on_bad_lines = 'skip')
df7 = pd.read_csv("saramin_4.csv", engine = 'python', quotechar = '"', on_bad_lines = 'skip')
df8 = pd.read_csv("saramin_5.csv", engine = 'python', quotechar = '"', on_bad_lines = 'skip')
df9 = pd.read_csv("saramin_6.csv", engine = 'python', quotechar = '"', on_bad_lines = 'skip')
df10 = pd.read_csv("saramin_7.csv", engine = 'python', quotechar = '"', on_bad_lines = 'skip')

combined_df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10], ignore_index=True)

combined_df.to_csv("all_jobs_combined.csv",
                   index=False,
                   encoding="utf-8-sig")

print("완료")