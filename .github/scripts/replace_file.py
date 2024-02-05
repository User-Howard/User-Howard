import requests

url = "https://raw.githubusercontent.com/User-Howard/Howard-OJ/master/%E5%81%9A%E9%A1%8C%E6%95%B8?token=GHSAT0AAAAAACNE3I4SRJD44UMSDJLZB6VMZOASSWQ"

response = requests.get(url)

if response.status_code == 200:
    number = int(response.text.strip())
    print("The number is:", number)
else:
    print("Failed to fetch data. Status code:", response.status_code)

content = f"""
### Hi there 👋
![Language](https://img.shields.io/badge/language-C/C++-brightgreen)
![Language](https://img.shields.io/badge/language-Python-brightgreen)
![Language](https://img.shields.io/badge/language-Swift-brightgreen)
![Language](https://img.shields.io/badge/做題數-{number}-brightgreen)
- 🌱 I’m currently learning C/C++, Python, Swift


<!--

<p>&nbsp;<img align="center" src="https://github-readme-stats.vercel.app/api?username=User-Howard&show_icons=true&locale=en" alt="User-Howard" /></p>
**User-Howard/User-Howard** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->"""
with open('README.md', 'w') as file:
    file.write(content)
