from tokhelper.dao.tiktok_main import solve_captcha_auto


class TokHelper():
    def __init__(self):
        print("init")
    def solve_auto(self,id,room):
        solve_captcha_auto(id,room)
