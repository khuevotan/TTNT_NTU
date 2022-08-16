from abc import ABC, abstractmethod
import copy

class val:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __eq__(self, other):
        try:
            if self.name == other.name:
                return True
        except:
            return False
        return False

    def isval(self):
        return True

    def istuyen(self):
        return False

    def ishoi(self):
        return False

    def isphu(self):
        return False


class menhde:
    def __init__(self, val1, val2):
        pass

    def __str__(self):
        pass

    def istuyen(self):
        return False

    def ishoi(self):
        return False

    def isphu(self):
        return False

    @abstractmethod
    def __eq__(self, other):
        # Phải cùng kiểu hội hoặc tuyển
        condition1 = self.istuyen() and other.istuyen()
        if not condition1:
            return False
        # 2 vế bằng nhau
        condition2 = self.val1 == other.val1 and self.val2 == other.val2
        condition3 = self.val1 == other.val2 and self.val2 == other.val1
        if (condition2 or condition3):
            return True
        return False


class hoi(menhde):
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def __str__(self):
        return "("+str(self.val1)+"^"+str(self.val2)+")"

    def ishoi(self):
        return True

    def phanra(self):  # a^b chuyển thành a,b
        return [self.val1, self.val2]


class tuyen(menhde):
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def __str__(self):
        return "("+str(self.val1)+"v"+str(self.val2)+")"

    def istuyen(self):
        return True

    def phanra(self):  # avb chuyển thành a,b
        return [self.val1, self.val2]


class phu(menhde):
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return "!"+str(self.val)

    def isphu(self):
        return True

    def __eq__(self, other):
        try:
            if self.val == other.val:
                return True
        except:
            return False
        return False

    def isval(self):
        return True


class bieuthuc:
    # Bước 1: Khởi tạo với dạng chuẩn
    def __init__(self, vetrai, vephai, prev=None):
        self.prev = prev  # Node biểu thức trước đó
        # Nhận vào các mệnh đề vế trái và vế phải theo dạng list
        self.vetrai = vetrai  # Vế trái là 1 list chứa các mệnh đề
        self.vephai = vephai  # Vế phải là 1 list chứa các mệnh đề
    # Bước 2: Chuyển vế đổi dấu

    def chuyenve(self):
        flag = 0
        temp = copy.deepcopy(self)
        for menhde in self.vetrai:
            if menhde.isphu():
                self.vephai.append(menhde.val)  # Đưa qua vế phải, bỏ phủ
                self.vetrai.remove(menhde)  # Xóa khỏi vế trái
                flag = 1
        for menhde in self.vephai:
            if menhde.isphu():
                self.vetrai.append(menhde.val)  # Đưa qua vế trái, bỏ phủ
                self.vephai.remove(menhde)  # Xóa khỏi vế phải
                flag = 1

    # Bước 3: Phân rã hội của giả thiết và tuyển của kết luận thành dấu phẩy
    def phanra(self):
        flag = 0
        for menhde in self.vetrai:  # Các phép tính ở vế trái
            if menhde.ishoi():  # Nếu là hội
                self.vetrai += menhde.phanra()  # Phân rã thành 2 mệnh đề con
                self.vetrai.remove(menhde)  # Xóa mệnh đề cũ
                flag = 1
        for menhde in self.vephai:  # Các phép tính ở vế phải
            if menhde.istuyen():  # Nếu là tuyển
                self.vephai += menhde.phanra()  # Phân rã thành 2 mệnh đề con
                self.vephai.remove(menhde)  # Xóa mệnh đề cũ
                flag = 1
        if flag == 1:
            print('Phân rã: ', self)
        else:
            print('Không phân rã được:', self)
        if(self.checkcm() == 1):
            print(' (ĐCM)')
        elif(self.checkcm() == -1):
            print(' (Ko ĐCM)')
        else:
            print('\n')
    # Hàm kiểm tra trạng thái "Được chứng minh", "Ko được chứng minh", "Còn chứng minh"

    def checkcm(self):
        self.chuyenve()
        # 1 là được chứng minh, 0 là còn chứng minh, -1 là không được chứng minh
        for menhdevt in self.vetrai:
            for menhdevp in self.vephai:
                if menhdevt == menhdevp:  # Nếu có 2 phần tử giống nhau -> dc chứng minh
                    return 1
        donvi = True  # Check xem tất cả đã trở thành dạng
        try:
            for menhdevt in self.vetrai:
                if not menhdevt.isval():  # (Nếu không phải đơn vị) -> Xuất hiện exception
                    pass
        except:
            donvi = False
        if donvi:
            return -1
        return 0

    # Hàm chuyển thành 2 trạng thái
    def chuyentrangthai(self):
        tt1 = None
        tt2 = None
        temp = copy.deepcopy(self)
        temp.prev = self
        # Bước 1: phân rã
        temp.phanra()
        # Bước 2: Chuyển về
        temp.chuyenve()
        # Bước 3: Chuyển trạng thái
        for menhde in self.vetrai:  # Nếu vế trái
            if menhde.istuyen():  # Có mệnh đề tuyển
                temp.vetrai.remove(menhde)
                tt1 = copy.deepcopy(temp)
                tt1.vetrai.append(menhde.phanra()[0])  # Chuyển trạng thái 1
                tt2 = copy.deepcopy(temp)
                tt2.vetrai.append(menhde.phanra()[1])  # Chuyển trạng thái 2
                return [tt1, tt2]
       # Bước 3: Chuyển trạng thái
        for menhde in self.vephai:  # Nếu vế phải
            if menhde.ishoi():  # Có mệnh đề hội
                temp.vephai.remove(menhde)
                tt1 = copy.deepcopy(temp)
                tt1.phai.append(menhde.phanra()[0])  # Chuyển trạng thái 1
                tt2 = copy.deepcopy(self)
                tt2.phai.append(menhde.phanra()[1])  # Chuyển trạng thái 2
                return [tt1, tt2]
        return [tt1, tt2]  # [None,None]

    def __str__(self):
        vetraistr = ','.join([str(menhde) for menhde in self.vetrai])
        vephaistr = ','.join([str(menhde) for menhde in self.vephai])
        return vetraistr + " => " + vephaistr


class VuongHao:
    def __init__(self, bieuthuc):
        self.Nodes = [bieuthuc]

    def checktt(self):  # Kiểm tra thử bài toán của mình đã được giải chưa
        if -1 in [bieuthuc.checkcm() for bieuthuc in self.Nodes]:
            return -1
        if 0 in [bieuthuc.checkcm() for bieuthuc in self.Nodes]:
            return 0
        return 1

    def run(self):
        print('Biểu thức của chúng ta là: ', self.Nodes[0])
        while(self.checktt() == 0):
            for bieuthuc in self.Nodes:
                self.Nodes.remove(bieuthuc)
                tt1, tt2 = bieuthuc.chuyentrangthai()
                if (tt1 == None):
                    continue
                else:
                    self.Nodes.append(tt1)
                    self.Nodes.append(tt2)
                    print('Tách', str(bieuthuc), 'thành', tt1, ' và ', tt2)
                if(self.checktt() == -1):
                    break
        print('KẾT QUẢ:', end='')
        if(self.checktt() == -1):
            print(' Không được chứng minh')
        if(self.checktt() == 1):
            print(' Được chứng minh')
        for bieuthuc in self.Nodes:
            print(bieuthuc)


menhde1 = tuyen(phu(val('p')), val('q'))
menhde2 = tuyen(phu(val('q')), val('r'))
menhde3 = tuyen(phu(val('p')), val('r'))

mybieuthuc = bieuthuc([menhde1, menhde2], [menhde3])
VuongHao(mybieuthuc).run()
