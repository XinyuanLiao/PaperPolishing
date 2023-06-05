import os
import openai

os.environ["HTTP_PROXY"] = "代理地址" # 前面记得加个“//”
os.environ["HTTPS_PROXY"] = "代理地址" # 前面记得加个“//”

openai.api_key = 'apikey'


def response(question):
    question = translate(question)
    q = "以下是一篇学术论文的一段话，打磨文字以符合学术风格，提高拼写，语法，清晰度，简洁性和整体可读性。必要时重写整个句子。此外，在后面直接列出修改后的中文翻译：" + question
    rsp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "一个计算机方向的论文专家"},
            {"role": "user", "content": q}
        ]
    )
    return rsp.get("choices")[0]["message"]["content"]


def translate(chinese):
    q = "如果下列语句是中文，将其翻译成英文输出，不需要其他多余语句；如果是英文则重复这句话即可，不需要其他多余语句：" + chinese
    rsp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "中文到英文的翻译学家"},
            {"role": "user", "content": q}
        ]
    )
    return rsp.get("choices")[0]["message"]["content"]


def only_translate(l):
    q = "如果下列语句是中文，则直接列出其英文翻译不需要其他多余语句；如果是英文，则直接列出其中文翻译不需要其他多余语句：" + l
    rsp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "中文到英文的翻译学家"},
            {"role": "user", "content": q}
        ]
    )
    return rsp.get("choices")[0]["message"]["content"]

def check_connection():
    try:
        r = openai.Completion.create(
            engine="text-davinci-003",
            prompt="Hello",
            max_tokens=10
        )
        return "连接成功！"
    except requests.exceptions.RequestException:
        return "网络连接失败，请重新设置代理地址！"
    except openai.error.AuthenticationError:
        return "API密钥无效，请重新设置API密钥！"
