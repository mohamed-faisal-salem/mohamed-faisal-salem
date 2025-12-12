import requests

# هنا حط اسم حسابك على GitHub
USERNAME = "Mohamed-Faisal-Salem"

# نجيب كل الريبو
url = f"https://api.github.com/users/{USERNAME}/repos?per_page=100"
repos = requests.get(url).json()

# نحسب كل لغة مستخدمة في الريبو
languages = {}
for repo in repos:
    lang = repo['language']
    if lang:
        languages[lang] = languages.get(lang, 0) + 1

# نحولها لنسبة مئوية
total = sum(languages.values())
top_languages = {k: round(v/total*100) for k,v in languages.items()}

print(top_languages)
