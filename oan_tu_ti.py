from time import sleep
from random import randint

cach1 = "\n"+"-"*50
cach2 = "-"*50
display_game = "main"
so_lan_choi = 0

def choi_lai():
    sleep(0.5)
    while True:
        global so_lan_choi
        try:
            chon = int(input("Bạn có muốn chơi lại không:\n1.Có\n2.Không\nBạn chọn (1,2): "))
            if chon == 1:
                so_lan_choi += 1
                return "ok"
            
            elif chon == 2:
                so_lan_choi += 1
                return "no"
            
            else:
                print("vui lòng nhập (1,2)")
        except:
            sleep(0.5)
            print(cach1)
            print("Lỗi x_x")
            print("vui lòng chọn (1,2)")
            print(cach2)
            sleep(0.5)

def choi_mot_nguoi():
    global so_lan_choi
    diem_player = 0
    diem_computer = 0
    chon1 = ""
    print("\n-- Trò chơi bắt đầu --")
    sleep(0.5)
    while True:
        try:
            kp = ""
            print(cach1)
            player = input("Chọn (keo, bua, bao): ")

            computer = randint(1,3)
            computer_chon = ""
            
            if computer == 1:
                computer_chon = "keo"
            elif computer == 2:
                computer_chon = "bua"
            elif computer == 3:
                computer_chon = "bao"
            
            if player == computer_chon:
                sleep(0.5)
                kp = "Hòa"
            else:
                if player == "keo":
                    if computer_chon == "bao":
                        kp = "Bạn được cộng 1 điểm"
                        diem_player += 1
                    else:
                        kp = "Máy được cộng 1 điểm"
                        diem_computer += 1

                elif player == "bua":
                    if computer_chon == "keo":
                        kp = "Bạn được cộng 1 điểm"
                        diem_player += 1
                    else:
                        kp = "Máy được cộng 1 điểm"
                        computer_chon += 1
                
                elif player == "bao":
                    if computer_chon == "bua":
                        kp = "Bạn được cộng 1 điểm"
                        diem_player += 1
                    else:
                        kp = "Máy được cộng 1 điểm"
                        computer_chon += 1
                
                else:
                    kp = "Máy được cộng 1 điểm"
                    computer_chon += 1
            
            sleep(0.5)
            print(cach1)
            print(f"Bạn chọn: {player}")
            sleep(0.25)
            print(f"Máy chọn: {computer_chon}")
            sleep(0.25)
            print(f"Kết quả: {kp}")
            sleep(0.25)
            print(f"Điểm của bạn: {diem_player}")
            sleep(0.25)
            print(f"Điểm của máy {diem_computer}")
            sleep(0.25)
            player = ""
            print(cach2)
            
            if diem_player == diem_thang:
                sleep(0.5)
                print(cach1)
                print(f"xin chúc mừng bạn đã thắng với số điểm là {diem_player}")
                chon1 = choi_lai()

            elif diem_computer == diem_thang:
                sleep(0.5)
                print(cach1)
                print(f"Bạn đã thất bại với số điểm là {diem_player}")
                chon1 = choi_lai()
            
            if chon1 == "ok":
                diem_computer = 0
                diem_player = 0
                chon1 = ""
                sleep(0.5)
            
            elif chon1 == "no":
                sleep(0.5)
                print(cach1)
                return "menu"
        
        except:
            print(cach1)
            print("Vui lòng nhập lại")
            print(cach2)

def choi_hai_nguoi():
    sleep(0.5)
    print("Trò chơi bắt đầu")
    global diem_thang
    running = True
    print(cach1)
    diem_player1 = 0
    diem_player2 = 0
    cho = ""
    while running:
        player1 = input("Player 1 chọn (keo,bua,bao): ")
        print("\n"*1000)
        player2 = input("player 2 chọn (keo,bua,bao): ")
        print("\n"*1000)
        if player1 == player2:
            kp = "Hòa nhau"
        elif player1 == "keo":
            if player2 == "bao":
                kp = "Player 1 được cộng 1 điểm"
                diem_player1 += 1
            else:
                kp = "Player 2 được cộng 1 điểm"
                diem_player2 += 1
        elif diem_player1 == "bua":
            if diem_player2 == "keo":
                kp = "Player 1 được cộng 1 điểm"
                diem_player1 += 1
            else:
                kp = "Player 2 được cộng 1 điểm"
        elif diem_player1 == "bao":
            if diem_player2 == "keo":
                kp = "Player 1 được cộng 1 điểm"
                diem_player1 += 1
            else:
                kp = "Player 2 được cộng 1 điểm"
                diem_player2 += 1
        else:
            kp = "Không hợp lệ"
        
        print(cach1)
        sleep(0.5)
        print(f"Player 1 chọn: {player1}")
        sleep(0.5)
        print(f"Player 2 chọn: {player2}")
        sleep(0.5)
        print(f"Kết quả: {kp}")
        sleep(0.5)
        print(f"Điểm Player 1: {diem_player1}")
        sleep(0.5)
        print(f"Điểm Player 2: {diem_player2}")
        print(cach2)

        if diem_player1 == diem_thang:
            sleep(0.5)
            print("Xin chúc mừng Player 1 thắng")
            cho = choi_lai()
        
        elif diem_player2 == diem_thang:
            sleep(0.5)
            print("Xin chúc mừng Player 2 thắng")
            cho = choi_lai()
            print(cach2)
            sleep(0.5)
        
        if cho == "ok":
            diem_player1 = 0
            diem_player2 = 0
            cho = ""
        
        elif cho == "no":
            running = False
            return "menu"

def cai_dat():
    sleep(0.5)
    global diem_thang
    running = True
    while running:
        print("Màn hình menu")
        print(cach1)
        chon = int(input("1.Số điểm thắng\n2.Mặc định\n3.Thoát\nBạn chọn (1,2,3): "))

        if chon == 1:
            sleep(0.5)
            print(cach1)
            diem_thang = int(input("chọn số điểm thắng: "))
            print(f"{diem_thang} điểm là thắng")
            print(cach2)
            sleep(0.5)

        elif chon == 2:
            sleep(0.5)
            print(cach1)
            diem_thang = 5
            print("đã quay về mặc định")
            sleep(0.5)
            print(cach2)

        elif chon == 3:
            sleep(0.5)
            running = False
            return "main"


def menu():
    running = True
    while running:
        chon = int(input("1.Chơi cùng máy\n2.Chơi cùng bạn\n3.Thoát\nbạn chọn(1,2,3): "))

        if chon == 1:
            sleep(0.5)
            return "choi_mot_nguoi"

        elif chon == 2:
            sleep(0.5)
            return "choi_hai_nguoi"

        elif chon == 3:
            sleep(2)
            running = False
            return "main"


def main():
    global so_lan_choi
    running = True
    while running:
        try:
            print(cach1)
            print("Game oẳn tù tì")
            choose = int(input("1.Chơi\n2.Cài đặt\n3.Thoát\nBạn chọn (1,2,3): "))
            print(cach2)

            if choose == 1:
                sleep(0.5)
                return "menu"

            elif choose == 2:
                sleep(0.5)
                return "setting"


            elif choose == 3:
                sleep(0.5)
                print("Tạm biệt bạn")
                running = False
                return "bye"
            
            elif choose == 3 and so_lan_choi >= 1:
                sleep(0.5)
                print("Cảm ơn bạn đã chơi và tạm biệt bạn")
                running = False
                return "bye"
        
        except:
            sleep(0.5)
            print(cach1)
            print("         Nhập sai\n-- yêu cầu nhập 1 hoặc 2 --")
            print(cach2)
            sleep(5)

if __name__ == "__main__":
        try:
            diem_thang = open("file.txt",mode = "r")
            diem_thang = diem_thang.readline()
            diem_thang = diem_thang.replace(":","")
            diem_thang = diem_thang.replace("=","")
            diem_thang = diem_thang.replace(" ","")
            diem_thang = diem_thang.replace("diem_thang","")
            diem_thang = int(diem_thang)

            while True:
                if display_game == "main":
                    display_game = main()
                elif display_game == "setting":
                    display_game = cai_dat()
                elif display_game == "menu":
                    display_game = menu()
                elif display_game == "choi_mot_nguoi":
                    display_game = choi_mot_nguoi()
                elif display_game == "choi_hai_nguoi":
                    display_game = choi_hai_nguoi()
                else:
                    break
            file_phuc_hoi = open("file.txt",mode = "w")
            file_phuc_hoi.write(f"diem_thang = {diem_thang}")
        except:
            sleep(0.5)
            file_phuc_hoi = open("file.txt",mode = "w")
            file_phuc_hoi.write("diem_thang = 5")
            print(cach1)
            print("không tìm thấy file")
            print("file sẽ phục hồi sau vài giây")
            sleep(5)
            print("vui lòng khởi động lại")
            print(cach2)