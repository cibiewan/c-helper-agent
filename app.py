import os
from openai import OpenAI

# 避免本地代理环境干扰网络请求
os.environ.pop("http_proxy", None)
os.environ.pop("https_proxy", None)
os.environ.pop("all_proxy", None)

client = OpenAI(
    api_key="sk-ws-H.PERHDDD.ekXW.MEUCIGLKOzyuHo1DxvsmkZED6kA-8xjtdJpnLeNFNBR1XqXhAiEA8cTVLn02Lhl68rT9D1va9tB7xekz55yLf0NbrNb2dSA",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

print("=" * 45)
print("     欢迎使用 C 语言报错诊断小助手")
print("=" * 45)

user_code = input("\n请粘贴或输入你想诊断的 C 语言错误代码，按回车确认：\n")

system_rule = (
    "你是一名耐心的大一C语言助教。请指出学生代码里的具体错因、修改方案，"
    "并用通俗易懂的口诀帮助新手记忆，不要使用过于深奥的计算机专业术语。"
)

print("\n助教正在看你的代码，请稍等几秒...\n")

response = client.chat.completions.create(
    model="qwen-plus",
    messages=[
        {"role": "system", "content": system_rule},
        {"role": "user", "content": f"帮我看看这段C代码哪里错了：\n{user_code}"}
    ]
)

print("=" * 20 + " 诊断报告 " + "=" * 20)
print(response.choices[0].message.content)
print("=" * 48)