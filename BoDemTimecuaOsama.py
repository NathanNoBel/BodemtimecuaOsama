def solve():
        global folder1
        global folder2
        folder1 = r"\allmusic" #Nên tải về rồi đặt theo hoặc đổi vị trí folder thành nơi bạn lưu để có thể sử dụng nha
        folder2 = r"\all"
        import os
        import msvcrt
        import time
        from dateutil.relativedelta import relativedelta
        from datetime import datetime
        import webbrowser
        os.system("cls")
        def baothuc():
                def sosanh(y, m, d, h, M, s):
                        try:
                                goodday = datetime(y, m, d, h, M, s)
                                played = False
                                while True:
                                        today = datetime.now()
                                        remaining = goodday - today
                                        remaining2 = relativedelta(goodday, today)
                                        os.system("cls" if os.name == "nt" else "clear")        
                                        if remaining.total_seconds() >= 8640000:
                                                print("Còn xa lắm...")
                                        elif 259200 < remaining.total_seconds() <= 8640000:
                                                print("Cố lên, sắp đến rồi...")
                                        elif 86400 < remaining.total_seconds() <= 259200:
                                                print(f"Còn {int(remaining.total_seconds() // 86400)} ngày")
                                        elif 11 < remaining.total_seconds() <= 86400:
                                                print('Less than 1 day remaining...')
                                        elif 10 < remaining.total_seconds() <= 11:
                                                print(f"Cùng đếm ngược nào! ({remaining.total_seconds()})")
                                        elif 0 < remaining.total_seconds() <= 10:
                                                print(int(remaining.total_seconds()), "!")
                                        elif -259200 < remaining.total_seconds() <= 0:
                                                print("ChangeUrMinesetNow", today.strftime("%Y"), "!")
                                        elif -432000 < remaining.total_seconds() <= -259200:
                                                print("Được vài hôm th, chắc kh sao đâu")
                                        else:
                                                print("Error 404: Not Found")
                                        print("Discord: @NathanNoBel / @Vanixtium")
                                        print("-" * 40)
                                        print("Bộ đếm thời gian")
                                        print(
                                        remaining2.years, "năm",
                                        remaining2.months, "tháng",
                                        remaining2.days, "ngày",
                                        remaining2.hours, "giờ",
                                        remaining2.minutes, "phút",
                                        remaining2.seconds, "giây"
                                                )
                                        print("Thời gian hiện tại:", today.strftime("%d/%m/%Y %H:%M:%S"))
                                        print("-" * 40)
                                        print(f"Thời gian bạn đã cài: {d}/{m}/{y} {h}:{M}:{s}")        
                                        print("-" * 40)
                                        print('[Q]: Thoát             [C]: Chỉnh sửa')
                                        time.sleep(1)
                                        if not played and remaining.total_seconds() <= 0:
                                                os.startfile(os.path.join(folder1, 'Thuoc dam vao ng a lag.mov'))
                                                played = True
                                        if msvcrt.kbhit():
                                                key = msvcrt.getch().decode().lower()
                                                if key == 'q':
                                                        os.system('cls')
                                                        mode()
                                                elif key == 'c':
                                                        change()  
                        except (ValueError, IndexError):
                                settime()

                def settime():
                        var = input('Có vẻ bạn chưa cài đặt đúng thời gian hoặc chưa đặt, đặt lại chứ? (Y/N): ').strip().lower()
                        if var == 'y':
                                change()
                        with open('Nani2.INP') as none:
                                inputtime = none.read().split()
                        sosanh(int(inputtime[2]), 
                        int(inputtime[1]), 
                        int(inputtime[0]), 
                        int(inputtime[3]), 
                        int(inputtime[4]), 
                        int(inputtime[5])
                        )           
                        
                def check():
                        try:
                                with open('Nani2.INP') as none:
                                        inputtime = none.read().split()
                                if not inputtime:
                                        settime()
                                else:
                                        sosanh(int(inputtime[2]), 
                                        int(inputtime[1]), 
                                        int(inputtime[0]),
                                        int(inputtime[3]),
                                        int(inputtime[4]),
                                        int(inputtime[5]),
                                        )  
                        except (FileNotFoundError, IndexError):
                                settime() 

                def sure():
                        os.system("cls")
                        print('--Lưu ý: r là reset, và sau reset sẽ không thể phục hồi lại--')
                        var = input('Xem lại thời gian gần đây hay reset? (r/n): ').strip().lower()
                        if var == 'r':
                                os.system("cls")
                                change()
                        elif var == 'n':
                                check()
                def change():
                        os.system("cls")
                        goods = input("Nhập ngày (dd/mm/yyyy): ")
                        times = input("Nhập thời gian (hh:MM:ss): ")
                        with open('Nani2.INP', 'w') as niga:
                                g = goods.split("/")
                                t = times.split(":")
                                niga.write(" ".join(g + t))
                        check()
                sure()
        def xemgio():
                played = False
                if not played:
                        os.startfile(os.path.join(folder1, "Hosilo by SArisu.mp4"))
                        played = True
                while True:
                        os.system("cls" if os.name == "nt" else "clear") 
                        today = datetime.now()
                        print("Discord: @NathanNoBel / @Vanixtium")
                        print('-' * 40)
                        print("Thời gian hiện tại là:")
                        print(today.strftime("%d/%m/%Y %H:%M:%S"))
                        print('-' * 40)
                        print('[Q]: Thoát')
                        time.sleep(1)
                        if msvcrt.kbhit():
                                key = msvcrt.getch().decode().lower()
                                if key == 'q':
                                        os.system('cls')
                                        mode()
        def playmusic():
                while True:
                        os.system('cls')
                        folder1 = r"D:\SD\allmusic"
                        print('Trình phát nhạc của Osama')
                        print('-' * 40)
                        print('Bạn có thể lựa chọn các bản nhạc/vid sau:')
                        musica = os.listdir(folder1)
                        for z in range(len(musica)):
                                print(f"[{z + 1}].{musica[z][:-4]}", end = '\n')
                        print('-Những bản nhạc mới sẽ được update sau cho các cậu nha-')
                        print('-' * 40)
                        print('[Q]: Thoát')
                        print('Lựa chọn nhạc bạn muốn: ')
                        check = msvcrt.getch().lower().decode()
                        gin = check
                        try:
                                gin = int(gin)
                                os.startfile(os.path.join(folder1, musica[gin - 1]))
                        except (ValueError, IndexError):
                                if gin == 'q':
                                        mode()
                                else:
                                        os.system('cls')
                                        print('Vui lòng nhập lại')
                                        print('-' * 40)
                                        time.sleep(2)
                                        playmusic()
        
        def plswait():
                os.system("cls" if os.name == "nt" else "clear")
                print("Đang trong giai đoạn phát triển, xin lỗi mọi người nhiều ạ")
                print("-" * 40)
                print('[Q]: Thoát')
                while True:
                        if msvcrt.kbhit():
                                key = msvcrt.getch().decode().lower()
                                if key == 'q':
                                        os.system('cls')
                                        mode()
        def kcthoigian():
                def checktime(y, m, d):
                        played = False
                        while True:
                                today = datetime.now()
                                goodday = datetime(y, m, d)
                                remaining2 = relativedelta(goodday, today)
                                os.system("cls" if os.name == "nt" else "clear")
                                print('Đồng hồ tính ngày của Osama')
                                print('Discord: @NathanNoBel/@Vanixtium')
                                print("-" * 40)
                                print(f'Ngày {d}/{m}/{y} cách đây:', '\n' ,
                                        int(remaining2.years) * -1, "năm",
                                        int(remaining2.months) * -1, "tháng",
                                        int(remaining2.days) * -1, "ngày",
                                        int(remaining2.hours) * -1, "giờ",
                                        int(remaining2.minutes) * -1, "phút",
                                        int(remaining2.seconds) * -1, "giây"
                                        )
                                print("-" * 40)
                                print('[Q]: Thoát             [C]: Chỉnh sửa')
                                time.sleep(1)
                                if msvcrt.kbhit():
                                        key = msvcrt.getch().decode().lower()
                                        if key == 'q':
                                                os.system('cls')
                                                mode()
                                        elif key == 'c':
                                                normaltime() 
                                if not played:
                                        os.startfile(os.path.join(folder1, "Two Different Worlds by -KoruSe and mzmff- (beginning looped by Hasen Yeung).mp3"))
                                        played = True
                def normaltime():
                        try:
                                os.system('cls')
                                print('Đồng hồ tính ngày của Osama')
                                print("-" * 40)
                                daylight = input('Nhập thời gian (Nhập "Q" nếu muôn thoát):  ').lower().split('/')
                                if len(daylight) == 1 and daylight[0] == 'q':
                                        mode()
                                y = int(daylight[2])
                                m = int(daylight[1])
                                d = int(daylight[0])
                                if not daylight:
                                        notvalue()
                                checktime(y, m, d)
                        except (ValueError, IndexError):
                                notvalue()
                def notvalue():
                        z = input('Có vẻ bạn nhập sai dữ liệu rồi, muốn nhập lại?(Y/N): ').lower().strip()
                        if z == 'y':    
                                normaltime()    
                        else:    
                                mode()
                normaltime()
        def Osama():
                a = ["Tên đầy đủ: Osama bin Muhammad bin 'Awad bin Laden",
                "Năm sinh: 10 tháng 3 năm 1957 tại Riyadh, Ả Rập Xê Út",
                "Tôn giáo/Tư tưởng: Hồi giáo dòng Sunni, theo đường lối chiến binh thánh chiến Salafi",
                "Xuất thân: Sinh ra trong một gia đình vô cùng giàu có và thế lực tại Ả Rập Xê Út (gia tộc sở hữu Tập đoàn xây dựng Saudi Binladin)",
                "Học vấn: Hắn được giáo dục bài bản và học đại học chuyên ngành quản trị kinh doanh và kỹ thuật dân dụng",
                "Về Quá trình hình thành tư tưởng và al-Qaeda: ",
                "Chiến tranh Afghanistan (thập niên 1980): Bin Laden rời Ả Rập Xê Út đến Afghanistan để tham gia vào cuộc kháng chiến chống Liên Xô, nơi hắn bắt đầu tài trợ và tổ chức các chiến binh Hồi giáo",
                "Thành lập Al-Qaeda: Vào năm 1988, hắn thành lập mạng lưới khủng bố toàn cầu al-Qaeda với mục đích thiết lập một đế chế Hồi giáo toàn cầu bằng bạo lực",
                "Chủ mưu các cuộc thảm sát: Bin Laden đã chỉ đạo hoặc liên đới tới hàng loạt vụ tấn công, đặc biệt là vụ đánh bom đại sứ quán Mỹ tại châu Phi (1998) và đỉnh điểm là vụ tấn công khủng bố ngày 11 tháng 9 năm 2001 nhằm vào Trung tâm Thương mại Thế giới và Lầu Năm Góc",
                "Bị truy nã: Sự kiện này khiến hắn trở thành đối tượng bị truy nã gắt gao nhất thế giới bởi FBI",
                "Chui lủi: Sau khi Mỹ đưa quân vào Afghanistan để lật đổ chế độ Taliban và truy quét al-Qaeda, bin Laden đã phải lẩn trốn trong suốt gần một thập kỷ tại nhiều địa điểm ở vùng biên giới Afghanistan - Pakistan.",
                "Về Cái chết và Di sản: ",
                "Bị tiêu diệt: Vào rạng sáng ngày 2 tháng 5 năm 2011, Osama bin Laden đã bị đặc nhiệm Hải quân Mỹ (SEAL) tiêu diệt trong một cuộc đột kích táo bạo tại thành phố Abbottabad, Pakistan (Chiến dịch mang tên Neptune Spear).",
                "Xác nhận: Thi thể của hắn được nhận dạng bằng phương pháp ADN và sau đó được thủy táng trên biển.",
                "Nguồn: AI của Google tóm lược từ Wikipedia"
                ]
                def mod():
                        global negaaa
                        negaaa = 0
                        try:
                                os.startfile(os.path.join(folder1, "Osama PARODY by itsRucka.mp4"))
                                while True:
                                        os.system("cls" if os.name == "nt" else "clear") 
                                        print("Tiểu sử về Osama in a clock (có thể xem thêm tại Wikipedia)")
                                        print("Discord: @NathanNoBel / @Vanixtium")
                                        print('-' * 40)
                                        print(a[negaaa])
                                        print('-' * 40)
                                        print('[Q]: Thoát         [N]: Quay lại     [M]: Tiếp tục   [W]: Tìm hiểu thêm tại Wikipedia')
                                        time.sleep(0.25)
                                        if msvcrt.kbhit() and negaaa <= len(a):
                                                dayum = msvcrt.getch().decode().lower()
                                                if dayum == 'm':
                                                        negaaa += 1
                                                elif dayum == 'n':
                                                        negaaa -= 1
                                                elif dayum == 'q':
                                                        mode()
                                                elif dayum == 'w':
                                                        webbrowser.open('https://vi.wikipedia.org/wiki/Osama_bin_Laden')
                        except IndexError:
                                much(negaaa)
                def much(negaaa):
                        while True:
                                os.system("cls" if os.name == "nt" else "clear") 
                                print("Tiểu sử về Osama in a clock (có thể xem thêm tại Wikipedia)")
                                print("Discord: @NathanNoBel / @Vanixtium")
                                print('-' * 40)
                                print('Bạn có thể xem thêm tại Wikipedia nếu bấm [W] hoặc quay lại bằng [N]')
                                print('-' * 40)
                                print('[Q]: Thoát         [N]: Quay lại          [W]: Tìm hiểu thêm tại Wikipedia')
                                time.sleep(0.25)
                                if msvcrt.kbhit() and negaaa >= len(a):
                                        dayum = msvcrt.getch().decode().lower()
                                        if dayum == 'n':
                                                os.system('cls')
                                                negaaa -= 1
                                                mod()
                                        elif dayum == 'q':
                                                mode()
                                        elif dayum == 'w':
                                                webbrowser.open('https://vi.wikipedia.org/wiki/Osama_bin_Laden')
                mod()
        def myprofile():
                mine = ["Xin chào các bạn, mình là Nathan aka Vanix Kaisnivok",
                        "Bản thân tớ là một coder không quá nghiện ngập vô phát triển chương trình mình tạo (mặc dù khi viết dòng này là cày 9 tiếng rồi XD )",
                        "Nói về ý tưởng đầu tiên để phát triển lên nó thì không quá lớn",
                        "Mở đầu cho ứng dụng này thực chất chỉ là đồng hồ đếm ngày đến Tết sau khi thi cuối kỳ I đầy căng thẳng thôi:))",
                        "Có ai ngờ được sắp nghỉ hè này mình lại làm được quả ứng dụng dài hơn 350 dòng này đâu chứ (cười)",
                        "Nếu nói không ngoa thì tớ đúng là người rảnh háng chính hiệu luôn:>",
                        "Để tạo nên được ứng dụng này trước hết phải cảm ơn những người đã đồng hành cùng trong suốt 1 tuần qua",
                        "Đầu tiên phải nói lời cảm ơn các mem của 'Quán Coffee của SArisu' đã tiếp thêm động lực để cố gắng hoàn thành",
                        "Tiếp theo phải kể đến FuHo, người anh hài hước nhưng rất đáng quý với tớ",
                        "Thêm nữa là nội tâm của bản thân, phải nói là giằng xé dữ dội để không bỏ dở giữa chừng luôn đó:)))",
                        "Cuối cùng, cảm ơn các bạn đã đọc đoạn văn viết từ tận đáy lòng này của tớ",
                        "Mong rằng sẽ có ngày gặp lại các bạn trong một dự án khác",
                        "*End*"
                        ]
                for z in range(len(mine)):
                        os.system('cls')
                        print(mine[z])
                        print('-' * 40)
                        time.sleep(3)
                while True:
                        os.system("cls" if os.name == "nt" else "clear") 
                        print('À mà, nếu bạn muốn liên hệ với tớ qua mạng xã hội về code hay tâm lý có thể tìm qua đây nha')
                        print('-' * 40)
                        print('[Q]:Thoát     [F]: Facebook        [D]:Discord')
                        print("Nếu sử dụng Discord đăng nhập acc thì tìm ID 'NathanNoBel' trên phần 'Thêm bạn' nha")
                        print('-' * 40)
                        print('Buy me a coffee in: [B]')
                        social = msvcrt.getch().decode().lower()
                        if social == 'f':
                                webbrowser.open("https://www.facebook.com/Vanixtium/")
                        elif social == 'd':
                                webbrowser.open("https://discord.com/channels/@me")
                        elif social == 'q':
                                os.system('cls')
                                mode()
                        elif social == 'b':
                                os.startfile(os.path.join(folder2, "buymeacoffee.jfif"))
                        else:
                                none()
        def none():
                                os.system('cls')
                                print("Bấm nhầm rồi:)))")
                                print('-' * 40)
                                os.startfile(os.path.join(folder1, "Điệu cười duyên dáng của Anh Công Nhân.mp4"))
                                time.sleep(5)
                                mode()
        def mode():
                try:
                        os.system('cls')
                        print("Đồng hồ của Osama:)))")
                        print("Discord: @NathanNoBel / @Vanixtium")
                        print('-' * 40)
                        print("[1].Xem thời gian và ngày tháng")
                        print("[2].Báo thức:)))")
                        print("[3].Phát nhạc")
                        print("[4].Khoảng cách thời gian")
                        print("[5].Tiểu sử về Osama Bin Laden")
                        print('[6].Thông tin về tác giả')
                        print('[B].Buy me a coffee')
                        print('-' * 40)
                        mama = input("Chọn phần muốn đến (Nhập 'Q' nếu muốn thoát): ")
                        if mama == '1':
                                os.system("cls")
                                xemgio()
                        elif mama == '2':
                                os.system("cls")
                                baothuc()
                        elif mama == '3':
                                playmusic()
                        elif mama == '4':
                                kcthoigian()
                        elif mama == '5':
                                Osama()
                        elif mama == '6':
                                myprofile()
                        elif mama == 'b':
                                os.startfile(os.path.join(folder2, 'buymeacoffee.jfif'))
                                mode()
                        elif mama == 'q':
                                os.system('cls')
                                return()
                        else:
                                none()
                except ValueError:
                        os.system('cls')
                        none()
        mode()
solve()
