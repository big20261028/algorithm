from typing import List

from collections import defaultdict


class Result:
    def __init__(self) -> None:
        self.ID: int = 0
        self.height: int = 0
        self.used: int = 0

class FenwickTree:
    def __init__(self, max_val):
        # 높이는 0부터 max_val까지 가능하므로, 1-based 인덱스를 위해 크기를 여유있게 잡습니다.
        self.tree = [0] * (max_val + 2)

    def add(self, val, delta):
        i = val + 1  # 0 높이도 처리할 수 있도록 +1 시프트
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)

    def query(self, val):
        i = val + 1
        if i >= len(self.tree):
            i = len(self.tree) - 1
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

class FishTank:
    def __init__(self, Mid, width, height, lengths, shapes):
        self.Mid = Mid
        self.width = width
        self.height = height
        self.lengths = list(lengths)
        self.shapes = list(shapes)
        self.shapes_subset = defaultdict(list)
        self.water_need = [0] * (height + 1)

        # 최적화: 물 계산 배열 대신 펜윅 트리 2개 생성
        self.count_tree = FenwickTree(height)  # 특정 높이의 기둥 '개수'
        self.sum_tree = FenwickTree(height)  # 특정 높이의 기둥 '높이 합'

        # 초기 높이 데이터 트리에 등록
        for h in self.lengths:
            if h <= self.height:
                self.count_tree.add(h, 1)  # 개수 1 증가
                self.sum_tree.add(h, h)  # 높이만큼 합 증가

        self.cal_shape_subset()
        # self.cal_need_water()  <-- 이 무거운 함수는 이제 영구 삭제합니다!

    # def cal_need_water(self):
    #     h_water = [0] * (self.height + 1)
    #     for h in self.lengths:
    #         if h <= self.height:
    #             h_water[h] += 1
    #
    #     can_fill_waters = 0
    #     total = 0
    #     for j in range(1, self.height + 1):
    #         can_fill_waters += h_water[j-1]
    #         total += can_fill_waters
    #         self.water_need[j] = total

    def cal_shape_subset(self):
        self.shapes_subset = defaultdict(list)

        for i in range(self.width - 2):
            sp_subset = (self.shapes[i], self.shapes[i+1], self.shapes[i+2])
            self.shapes_subset[sp_subset].append(i)

    # 이 어항 객체에 블록을 설치할 수 있는지 확인
    # shapes_subset에 없으면 리턴 -1
    # 있으면 해당 인덱스의 블록 높이 + 설치블록
    # 설치 조건 만족하는지 확인
    # 만족하는 col 인덱스 반환/
    def is_can_install(self, block_lengths, block_up_shapes, block_down_shapes):
        if tuple(block_down_shapes) not in self.shapes_subset:
            return -1

        for col in self.shapes_subset[tuple(block_down_shapes)]:
            if self.check_block_condition(col,block_lengths):
                return col

        return -1

    def check_block_condition(self, col_idx, block_lengths):
        l_1 = self.lengths[col_idx] + block_lengths[0]
        l_2 = self.lengths[col_idx + 1] + block_lengths[1]
        l_3 = self.lengths[col_idx + 2] + block_lengths[2]

        if l_1 > self.height or l_2 > self.height or l_3 > self.height:
            return False

        if l_1 <= self.lengths[col_idx + 1] or l_3 <= self.lengths[col_idx + 1]:
            return False
        if l_2 <= self.lengths[col_idx] or l_2 <= self.lengths[col_idx + 2]:
            return False

        return True

    def do_install(self, col, block_lengths, block_up_shapes, block_down_shapes):
        for i in range(3):
            old_h = self.lengths[col + i]
            new_h = old_h + block_lengths[i]

            # 1. 트리에서 기존 높이 데이터 빼기 (-)
            if old_h <= self.height:
                self.count_tree.add(old_h, -1)
                self.sum_tree.add(old_h, -old_h)

            # 2. 트리에 새로운 높이 데이터 더하기 (+)
            if new_h <= self.height:
                self.count_tree.add(new_h, 1)
                self.sum_tree.add(new_h, new_h)

            # 3. 실제 배열 업데이트
            self.lengths[col + i] = new_h
            self.shapes[col + i] = block_up_shapes[i]

        self.cal_shape_subset()
        # self.cal_need_water() <-- 삭제! 업데이트 끝.
        return True

    def get_water_need(self, Y):
        # Y가 0이면 물이 필요 없음
        if Y == 0:
            return 0

        # 목표 수위 Y보다 '낮은(Y-1 이하)' 기둥들의 정보를 가져옵니다.
        cnt = self.count_tree.query(Y - 1)
        total_sum = self.sum_tree.query(Y - 1)

        # 수학 공식: Y * (기둥 개수) - (기둥들의 원래 높이 합)
        return (Y * cnt) - total_sum

tank_list = []

def init(N: int, mWidth: int, mHeight: int, mIDs: List[int], mLengths: List[List[int]], mUpShapes: List[List[int]]) -> None:
    global tank_list
    tank_list = []
    for i in range(N):
        tank = FishTank(mIDs[i], mWidth, mHeight, mLengths[i], mUpShapes[i])
        tank_list.append(tank)
    tank_list.sort(key=lambda x : x.Mid)


def checkStructures(mLengths: List[int], mUpShapes: List[int], mDownShapes: List[int]) -> int:
    cnt = 0

    for tank in tank_list:
        if tuple(mDownShapes) in tank.shapes_subset:
            for col in tank.shapes_subset[tuple(mDownShapes)]:
                if tank.check_block_condition(col,mLengths):
                    cnt += 1

    return cnt

def addStructures(mLengths: List[int], mUpShapes: List[int], mDownShapes: List[int]) -> int:

    for tank in tank_list:
        if tuple(mDownShapes) in tank.shapes_subset:
            for col in tank.shapes_subset[tuple(mDownShapes)]:
                if tank.check_block_condition(col,mLengths):
                    tank.do_install(col,mLengths,mUpShapes,mDownShapes)
                    result = (tank.Mid * 1000) + (col+1)
                    return result
    return 0

def pourIn(mWater: int) -> Result:
    rs_Mid, rs_h, rs_wt = 0,0,0

    for tank in tank_list:
        top_idx = tank.height
        bottom_idx = 1 # 탱크 높이는 1부터 height까지

        max_water_need = 0
        max_height = 0
        while bottom_idx <= top_idx:
            middle_idx = (top_idx + bottom_idx) // 2
            need = tank.get_water_need(middle_idx)

            if 0 < need <= mWater:
                max_height = middle_idx
                max_water_need = need
                bottom_idx = middle_idx + 1
            else:
                if need == 0 and middle_idx < tank.height:
                    bottom_idx = middle_idx + 1
                else:
                    top_idx = middle_idx - 1

        if max_height > rs_h:
            rs_Mid, rs_h, rs_wt = tank.Mid, max_height, max_water_need

        elif max_height > 0 and max_height == rs_h and max_water_need > rs_wt:
            rs_Mid, rs_wt = tank.Mid, max_water_need

    ret = Result()
    ret.ID , ret.height , ret.used = rs_Mid, rs_h, rs_wt
    return ret
