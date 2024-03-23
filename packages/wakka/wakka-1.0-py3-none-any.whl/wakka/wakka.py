import webbrowser

def syntax(i):
    koubun = ["なんで寺院に機械があんだよ", "教えはどうなってんだ教えは", "お前ら禁じられた機械を平気で使ってんじゃねえか", "分かってんのか！？", "「シン」が生まれたのは人間が機械に甘えたせいだろうが", "金取んのかよ！？", "くそったれ！"]
    
    if(i == "all"):
        return koubun
    else:
        num = int(i)

    return koubun[num]

def isWakka(sin):
    if(sin == "シン" or sin == "アルベド"):
        return True
    else:
        return False

def openBrowser():
    webbrowser.open("https://google.com/search?q=ワッカ");

def isFellsGood(text):
    return "ティーダの" + text + "気持ち良すぎだろ！"

def ranking(rank, name):
    rank = str(rank)
    return "(" + rank + "位) " + name

def title():
    return "(合作)おとわっか"