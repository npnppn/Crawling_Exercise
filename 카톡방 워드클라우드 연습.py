from wordcloud import WordCloud

text = ''
with open("kakaotalk.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines[5:]:
        if '] [' in line:
            text += line.split('] ')[2].replace('ㅋ','')

print(text)


wc = WordCloud(font_path="C:/Windows/Fonts/malgunsl.ttf", background_color="white", width=600, height=400)
wc.generate(text)
wc.to_file("result.png")


# 글씨체 다운로드 하는 코드
# import matplotlib.font_manager as fm
#
# # 이용 가능한 폰트 중 '고딕'만 선별
# for font in fm.fontManager.ttflist:
#     if 'Gothic' in font.name:
#         print(font.name, font.fname)

