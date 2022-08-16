import time


class GRAPH:
    def __init__(self, yeuto):
        self.yeuto = yeuto
        temp = []
        self.parent = temp
    yeuto = "still not defined"
    congthuctinh = "still not defined"
    parent = []  # define: GRAPH()
    children = []

    def addChild(self, node):
        self.children.append(node)
        node.children = []
        node.parent = self

    def getAllParents_andMyself(self, list):
        list.append(self.yeuto)
        if self.parent:
            if self.parent.parent:
                self.parent.getAllParents_andMyself(list)
            else:
                list.append(self.parent.yeuto)

    def getChildrenF1(self):
        node = []
        for child in self.children:
            node.append(child)
        return node

    def getDirections(self, startnode):
        buocgiai = []
        node = self
        while node != startnode:
            buocgiai.insert(0, (node.yeuto, node.congthuctinh.name))
            node = node.parent
        return buocgiai


''' CÔNG THỨC '''


class CONGTHUC:
    yeutos = []  # yếu tố bao gồm trong công thức
    name = "undefined"  # tên công thức

    def __init__(self, name, *yeutos):
        self.name = name
        temp = []
        for yeuto in yeutos:
            temp.append(yeuto)
        self.yeutos = temp

    def display(self):
        print("List: ", self.yeutos)

    def getTongSo_YeuTo(self):
        return len(self.yeutos)


class Queue:
    "A container with a first-in-first-out (FIFO) queuing policy."

    def __init__(self):
        self.list = []

    def push(self, item):
        "Enqueue the 'item' into the queue"
        self.list.insert(0, item)

    def pop(self):
        """
          Dequeue the earliest enqueued item still in the queue. This
          operation removes the item from the queue.
        """
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the queue is empty"
        return len(self.list) == 0


class Search:
    def breadthFirstSearch(self, problem):
        """Search the shallowest nodes in the search tree first."""
        "*** YOUR CODE HERE ***"
        fringe = Queue()
        #visitedList = []
        fringe.push(problem.getStartState())
        state = fringe.pop()
        # visitedList.append(state)
        while not problem.isGoalState(state):
            successors = problem.getSuccessors(state)
            for son in successors:
                fringe.push(son)
            if(not fringe.isEmpty()):
                state = fringe.pop()
            else:
                return False
        return state


class SearchProblem:

    startnode = "still not defined"
    destinationnode = "still not defined"

    def __init__(self, start, des):
        self.startnode = start
        self.destinationnode = des

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        return self.startnode

    def isGoalState(self, node):
        """
          state: Search state
        Returns True if and only if the state is a valid goal state.
        """
        return (node.yeuto == self.destinationnode)

    def getSuccessors(self, node):
        """
          trả về children của node []child nodes
        """
        return node.getChildrenF1()  # []


''' MAIN: BÀI TOÁN TAM GIÁC'''


class BAITOAN_TAMGIAC:
    Startnode = "still not defined"
    root = "still not define"
    fringe = Queue()
    yeutocanthiets = []  # (thành phần phụ) sử dụng cho chuẩn hóa bước giải
    congthucs = []  # lưu các tri thức (các công thức)
    yeutodabiets = []  # lưu các yếu tố đã biết
    yeutocantim = -1  # chỉ định yếu tố cần tìm
    buocgiais = []  # lưu các bước giải bài toán

    def clear(self):  # vẫn giữ nguyên tri thức
        self.yeutocanthiets.clear()
        self.yeutodabiets.clear()
        self.yeutocantim = -1
        self.buocgiais.clear()
        fringe = Queue()
        Startnode = "still not defined"
        root = "still not define"

    def setYeuToDaBiets(self, *yeutos):
        self.Startnode = GRAPH(yeutos[0])
        self.root = self.Startnode
        for i in range(1, len(yeutos)):
            node = GRAPH(yeutos[i])
            self.Startnode.addChild(node)
            self.Startnode = node
        self.fringe.push(self.Startnode)

    def setYeuToCanTim(self, yeuto):
        self.yeutocantim = yeuto

    def getYeuToDaBiets(self, node):
        list = []
        node.getAllParents_andMyself(list)
        return list

    '''themCongThuc(*congthucs): thêm tri thức <*congthucs> vào Bài Toán Tam Giác. '''

    def themCongThuc(self, *congthucs):
        for congthuc in congthucs:
            self.congthucs.append(congthuc)
    ''' getSoYeuToDaBiet_congthuc(congthuc): return số lượng yếu tố đã biết trong <congthuc>. '''

    def getSoYeuToDaBiet_congthuc(self, congthuc, node):
        count = 0
        for yeuto in congthuc.yeutos:
            if(yeuto in self.getYeuToDaBiets(node)):
                count += 1
        return count
    ''' getYeuToChuaBiet_congthuc(congthuc): trả về yếu tố chưa biết trong <congthuc>'''

    def getYeuToChuaBiet_congthuc(self, congthuc, node):
        for yeuto in congthuc.yeutos:
            if (yeuto not in self.getYeuToDaBiets(node)):
                return yeuto
        raise ValueError('you got error!')

    ''' getYeuTo_cothetinh(self, congthuc):
            trả về yếu tố có thể kích hoạt
                trả về -1 nếu không tìm được'''

    def getYeuTo_cothetinh(self, node, actived_yeuto):
        for congthuc in self.congthucs:
            if(self.getSoYeuToDaBiet_congthuc(congthuc, node)+1 == congthuc.getTongSo_YeuTo()):
                yeuto = self.getYeuToChuaBiet_congthuc(congthuc, node)
                if(yeuto not in actived_yeuto):
                    #print("[log] từ node ",node.yeuto, " kích hoạt được ", yeuto, "." )
                    return (yeuto, congthuc)
        return (-1, "")
    ''' KichHoat_YeuTo(yeutoCoTheTinh): kích hoạt yếu tố được truyền vào '''

    def KichHoat_YeuTo(self, yeutoCoTheTinh):
        self.yeutodabiets.append(yeutoCoTheTinh)
    ''' themBuocGiai(yeuto, congthuc): thêm một bước giải vào <buocgiai>
            tham số: 
                yeuto: yếu tố cần tính
                congthuc: công thức để tính yeuto '''

    def themBuocGiai(self, yeuto, congthuc):
        buocgiai = (yeuto, congthuc)
        self.buocgiais.append(buocgiai)
    ''' is_Success(): kiểm tra trạng thái đích của bài toán.
            nếu yếu tố cần tìm đã được kích hoạt -> return True
                else: return Flase'''

    def is_Success(self):
        if(self.yeutocantim in self.yeutodabiets):
            return True
        return False
    ''' chuanhoaBuocGiai(congthucdich): loại bỏ các bước giải không cần thiết trong viễa (hàm bổ sung) '''

    def chuanhoaBuocGiai(self, congthucdich):
        # thêm các yếu tố có trong công thức đích vào @yeutocanthiets
        for yeuto in congthucdich.yeutos:
            self.yeutocanthiets.append(yeuto)
        # loại bỏ các bước dư thừa
        for i in range(len(self.buocgiais)-1, -1, -1):
            if(self.buocgiais[i].yeutogiai not in self.yeutocanthiets):
                del self.buocgiais[i]
            else:
                for yeuto in self.buocgiais[i].congthuc.yeutos:
                    self.yeutocanthiets.append(yeuto)

    def BuildGraph_bySemantic(self):

        while(not self.fringe.isEmpty()):
            node = self.fringe.pop()
            #print("\n[BuildGraph] GET a node [",node.yeuto,"] from fringe.")
            # input()
            actived_yeutos = []  # yeutos đã kích hoạt ở node hiện tại. khởi tạo bằng rỗng
            while True:
                (yeutoCoTheTinh, congthuctinh) = self.getYeuTo_cothetinh(
                    node, actived_yeutos)  # trả về yếu tố chưa có trong actived
                if(yeutoCoTheTinh != -1):
                    newnode = GRAPH(yeutoCoTheTinh)
                    newnode.congthuctinh = congthuctinh
                    node.addChild(newnode)
                    if(yeutoCoTheTinh != self.yeutocantim):
                        self.fringe.push(newnode)
                    else:
                        break
                    actived_yeutos.append(yeutoCoTheTinh)
                    #print("[log] danh sách actived list", actived_yeutos )
                else:
                    break

    def PrintGraph_DeepFirst(self, node, level):
        print("     "*level, node.yeuto)
        if(node.children):
            for child in node.children:
                self.getGraph_DFS(child, level+1)

    def PrintGraph_breadthFirst(self, node, level):
        print("     "*level, node.yeuto)
        if(node.children):
            for child in node.children:
                print("     "*(level+1), child.yeuto)
            for child in node.children:
                self.getGraph_DFS(child, level+2)
    ''' def getshallowestDestination(self)
        return: shallowest Destination node'''

    def getshallowestDestination(self):
        searchproblem = SearchProblem(
            self.Startnode, self.yeutocantim)  # Startnode = start_node
        search = Search()  # import from unit.py (pacman project)
        return search.breadthFirstSearch(searchproblem)
    '''  GiaiBaiToan(): 
        bước 1: xây dựng đồ thị (đồ thị rút gọn)
        bước 2: áp dụng BFS 
    '''

    def GiaiBaiToan(self):
        # bước 1: xây dựng đồ thị
        self.BuildGraph_bySemantic()
        #print("log: builded graph")
        # bước 2: áp dụng BFS tìm node đích gần nhất (các bước đi ngắn nhất)
        # desnode = node đích với bước đi là ngắn nhất
        desnode = self.getshallowestDestination()
        # sau khi tìm được node đích, lấy cách đi (getDirection)
        if(desnode):
            loigiai = []
            buocgiais = desnode.getDirections(self.Startnode)
            for buocgiai in buocgiais:
                loigiai.append(
                    "tính " + buocgiai[0] + " thông qua " + buocgiai[1])
            return loigiai
        return ["bài toán không thể giải, hãy bổ sung thêm thông tin hoặc tri thức"]


def CongThuc(n):
    cong_thuc = {
        1: "p = (a + b + c) / 2",
        2: "s = 1/2 * a * b * sin(c)",

    }
    return cong_thuc.get(n, "sai cong thuc")


# define names
canh_a = "cạnh a"
canh_b = "cạnh b"
canh_c = "cạnh c"
goc_A = "góc A"
goc_B = "góc B"
goc_C = "góc C"
nuaChuVi_p = "nửa chu vi"
dienTich_S = "diện tích"
trungTuyen_Ma = "trung truyến Ma"
trungTuyen_Mb = "trung truyến Mb"
trungTuyen_Mc = "trung truyến Mc"
duongCao_Ha = "đường cao Ha"
duongCao_Hb = "đường cao Hb"
duongCao_Hc = "đường cao Ha"
bk_NoiTiep_r = "bán kính đường tròn nội tiếp TG r"
bk_NgoaiTiep_R = "bán kính đường tròn ngoại tiếp TG R"

if __name__ == "__main__":
    # 1:init - thêm tri thức
    congthuc1 = CONGTHUC("công thức 1", canh_a, canh_b, canh_c, nuaChuVi_p)
    congthuc2 = CONGTHUC("công thức 2", canh_a, canh_b, goc_C, dienTich_S)
    congthuc3 = CONGTHUC("công thức 3", canh_a, canh_b, goc_A, goc_B)
    congthuc4 = CONGTHUC("công thức 4", canh_a, canh_b, canh_c, goc_C)
    congthuc5 = CONGTHUC("công thức 5", goc_A, goc_B, goc_C)
    congthuc6 = CONGTHUC("công thức 6", nuaChuVi_p, dienTich_S, bk_NoiTiep_r)
    congthuc7 = CONGTHUC("công thức 7", canh_a, canh_c, goc_A, goc_C)
    congthuc8 = CONGTHUC("công thức 8", canh_a, canh_b,
                         canh_c, nuaChuVi_p, dienTich_S)
    congthuc9 = CONGTHUC("công thức 9", canh_a, canh_b, canh_c, trungTuyen_Ma)
    congthuc10 = CONGTHUC("công thức 10", canh_a,
                          canh_b, canh_c, trungTuyen_Mb)
    congthuc11 = CONGTHUC("công thức 11", canh_a,
                          canh_b, canh_c, trungTuyen_Mc)
    congthuc12 = CONGTHUC("công thức 12", canh_a, dienTich_S, duongCao_Ha)
    congthuc13 = CONGTHUC("công thức 13", canh_b, dienTich_S, duongCao_Hb)
    congthuc14 = CONGTHUC("công thức 14", canh_c, dienTich_S, duongCao_Hc)
    congthuc15 = CONGTHUC("công thức 15", canh_a, canh_b,
                          canh_c, dienTich_S, bk_NgoaiTiep_R)
    baitoan = BAITOAN_TAMGIAC()
    baitoan.themCongThuc(congthuc1, congthuc2, congthuc3, congthuc4, congthuc5, congthuc6, congthuc7,
                         congthuc8, congthuc9, congthuc10, congthuc11, congthuc12, congthuc13, congthuc14, congthuc15)
    start_time = time.time()
    # 2 input here
    # bài toán 1
    baitoan.setYeuToDaBiets(canh_a, canh_b, canh_c)
    baitoan.setYeuToCanTim(nuaChuVi_p)
    loigiais = baitoan.GiaiBaiToan()
    print("Lời Giải")
    for loigiai in loigiais:
        print(loigiai)
    print(CongThuc(int(loigiais[0][-1])))
    baitoan.clear()
    # bài toán 2
    # baitoan.setYeuToDaBiets(canh_a, canh_b, canh_c)
    # baitoan.setYeuToCanTim(dienTich_S)
    # loigiais = baitoan.GiaiBaiToan()
    # print("Lời Giải")
    # for loigiai in loigiais:
    #     print(loigiai)
    # baitoan.clear()
    # bài toán 3
    # baitoan.setYeuToDaBiets(canh_a, canh_b, goc_C)
    # baitoan.setYeuToCanTim(duongCao_Ha)
    # loigiais = baitoan.GiaiBaiToan()
    # print("Lời Giải")
    # for loigiai in loigiais:
    #     print(loigiai)
    # # print("đồ thị:")
    # #baitoan.getGraph_DFS(baitoan.Startnode,0)
    # baitoan.clear()
    print("\nTime of execution: ", float(time.time() - start_time))
##  ##   ## THE END ##   ## ##
