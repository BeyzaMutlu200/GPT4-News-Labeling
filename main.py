import os
import openai
import pandas as pd
import time

# openai.api_key = 'YOUR_API_KEY_HERE'  # API key artık buraya yazılmayacak, GitHub’a pushlanabilir

news_directory = r'C:\Users\Beyza\Desktop\magazin'

def label_news_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    while True:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a sentiment analysis assistant."},
                    {"role": "user", "content": f"Bu haber metnini 'olumlu' veya 'olumsuz' olarak etiketler misin: {content}"}
                ]
            )

            label = response['choices'][0]['message']['content'].strip().lower()
            if 'olumlu' in label:
                return 'olumlu'
            elif 'olumsuz' in label:
                return 'olumsuz'
            else:
                return 'belirsiz'
        except openai.error.RateLimitError as e:
            print(f"Rate limit error: {e}. Sleeping for 10 seconds.")
            time.sleep(10)

results = []
for root, dirs, files in os.walk(news_directory):
    for file in files:
        if file.endswith('.txt'):
            file_path = os.path.join(root, file)
            label = label_news_file(file_path)
            results.append((file_path, label))
            print(f"File: {file_path} - Label: {label}")
            time.sleep(2)  # Her istekten sonra 2 saniye bekle

df = pd.DataFrame(results, columns=['File Path', 'Label'])
output_excel = 'news_labels.xlsx'
df.to_excel(output_excel, index=False)
