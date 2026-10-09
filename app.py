import streamlit as st
from openai import OpenAI

# 1. 页面设置
st.set_page_config(page_title="C语言助教", page_icon="💻", layout="centered")

st.title("💻 C语言初学者代码诊断助教")
st.caption("专门针对大一新生：输入有疑问或报错的 C 语言代码，助教为你分析诊断！")

# 2. 读取你在 Streamlit Secrets 中配置的 API_KEY（如果没配好则留空备用）
api_key = st.secrets.get("DASHSCOPE_API_KEY", "")

# 3. 初始化客户端
client = OpenAI(
    api_key=api_key,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 4. 网页端代码输入框
user_code = st.text_area(
    "请在此粘贴你想诊断的 C 语言代码：",
    height=200,
    placeholder='#include <stdio.h>\n\nint main() {\n    int a;\n    scanf("%d", a);\n    return 0;\n}'
)

# 5. 诊断按钮与触发逻辑
if st.button("🚀 开始诊断", type="primary"):
    if not user_code.strip():
        st.warning("⚠️ 请先在上方输入需要诊断的代码！")
    else:
        with st.spinner("助教正在逐行阅读你的代码，请稍候..."):
            system_rule = (
                "你是一名耐心的大一C语言助教。请指出学生代码里的具体错因、修改方案，"
                "并用通俗易懂的口诀帮助新手记忆，不要使用过于深奥的计算机专业术语。"
            )
            try:
                response = client.chat.completions.create(
                    model="qwen-plus",
                    messages=[
                        {"role": "system", "content": system_rule},
                        {"role": "user", "content": f"帮我看看这段C代码哪里错了：\n{user_code}"}
                    ]
                )
                st.markdown("### 📋 诊断报告")
                st.markdown(response.choices[0].message.content)
            except Exception as e:
                st.error(f"调用诊断接口失败：{e}")
