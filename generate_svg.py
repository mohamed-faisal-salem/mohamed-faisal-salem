import requests

# حط اسم حسابك هنا
USERNAME = "Mohamed-Faisal-Salem"

# جلب الريبو من GitHub
url = f"https://api.github.com/users/mohamed-faisal-salem/repos?per_page=100"
repos = requests.get(url).json()

# نحسب كل لغة ونسبتها
languages = {}
for repo in repos:
    lang = repo['language']
    if lang:
        languages[lang] = languages.get(lang, 0) + 1

total = sum(languages.values())
top_languages = {k: round(v/total*100) for k,v in languages.items()}

# اقرأ الـ SVG Template
with open("stats-card.svg", "r") as f:
    svg_template = f.read()

# استبدل placeholders بالقيم الحقيقية
for lang, percent in top_languages.items():
    svg_template = svg_template.replace(f"{{{lang}}}", f"{percent}%")

# احفظ الملف النهائي
with open("stats.svg", "w") as f:
    f.write(svg_template)

print("✅ SVG تم تحديثه بنجاح!")
