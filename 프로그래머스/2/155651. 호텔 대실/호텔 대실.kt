/*
호텔을 운영 중인 코니는 최소한의 객실만을 사용하여 예약 손님을 받으려고 한다
-> bfs dfs 문제

한 번 사용한 객실은 퇴실 시간을 기준으로 10분 간 청소 => 퇴실 시간 + 10 -> 사용 가능

예약 시간이 문자열로 담인 book_time 존재, 최소 객실 수 

우선 기본 아이디어는 book_time을 시작 시간으로 정렬해서, 가장 빠른 시간 순으로 넣어본다

조합을 하는거지 

맨 처음에 가장 빠른 거 pop으로 가져옴, 그 다음으로 종료 시간을 보고,

종료 시간 + 10을 한 다음, 그거 랑 같거나 늦은 가장 빠른 객실, 이걸 계속 탐색
*/
import java.util.PriorityQueue

class Solution {
    fun solution(book_time: Array<Array<String>>): Int {
        
        // 1. 시작 시간 기준 정렬
        val reservations = book_time
            .map { parseTimeToInt(it[0]) to parseTimeToInt(it[1]) }
            .sortedBy { it.first }

        // 2. 끝나는 시간(퇴실 + 청소 10분)을 담는 우선순위 큐 (가장 빨리 비는 방이 맨 위)
        val roomQueue = PriorityQueue<Int>() // Int는 방 사용 끝나는 시간 (분 단위)

        for ((start, end) in reservations) {
            // 가장 빨리 비는 방보다 예약 시작 시간이 같거나 늦으면 재사용
            if (roomQueue.isNotEmpty() && roomQueue.peek() <= start) {
                roomQueue.poll()
            }

            // 새 방 배정 (퇴실 + 청소 시간)
            roomQueue.add(end + 10)
        }

        return roomQueue.size
    }
    
    fun parseTimeToInt(time: String): Int {
        val (hour, minute) = time.split(":").map { it.toInt() }
        return hour * 60 + minute
    }
}
