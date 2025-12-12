import requests

USERNAME = "mohamed-faisal-salem"

# نجيب قائمة الريبو
repos_url = f"https://api.github.com/users/{USERNAME}/repos?per_page=100"
repos = requests.get(repos_url).json()

languages = {}

# نجيب كل لغة بشكل دقيق من endpoint خاص بكل repo
for repo in repos:
    repo_name = repo["name"]
    lang_url = f"https://api.github.com/repos/{USERNAME}/{repo_name}/languages"
    lang_data = requests.get(lang_url).json()

    for lang, size in lang_data.items():
        languages[lang] = languages.get(lang, 0) + size

# حساب النسب
total = sum(languages.values())
top_languages = {k: round(v / total * 100) for k, v in languages.items()}

print("📊 نسب اللغات بدقة:")
print(top_languages)

# اقرأ الـ SVG Template
with open("stats-card.svg", "r", encoding="utf-8") as f:
    svg_template = f.read()

# نحدث القيم داخل الـ SVG
for lang, percent in top_languages.items():

    # استبدال {Python} → 25%
    svg_template = svg_template.replace(f"{{{lang}}}", f"{percent}%")

    # تعديل bars width dynamically
    max_bar_width = 250  # نفس اللي في الكود بتاعك
    bar_width = int((percent / 100) * max_bar_width)
    svg_template = svg_template.replace(f"WIDTH[{lang}]", str(bar_width))

# حفظ الناتج النهائي
with open("stats.svg", "w", encoding="utf-8") as f:
    f.write(svg_template)

print("✅ SVG تم تحديثه بنجاح!")
