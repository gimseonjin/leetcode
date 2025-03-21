/*
재택 근무와 함께 출근 희망 시각 - 유연 근무제
설정한 희망 시각에 늦지 않고 출근한 직원

출근 희망 시각 + 10분 전까지 출근해야함

ex) 9:58 분 -> 10:08분까지 출근

토 / 일 제외
매일 한번씩 / 시에 100분 곱하고 분을 더함

9:59 -> 959
10:00 -> 1000

schedules -> 출근 희망 시각을 담음
-> 7시 부터 11시 사이 -> 700 ~ 1100
일주일 동안 출근한 시각 timelogs
시작 요일 startday
*/
class Solution {
    fun solution(
        schedules: IntArray,
        timelogs: Array<IntArray>,
        startday: Int
    ): Int = schedules.indices.count { employeeIndex ->
        val arrivalDeadline = calculateArrivalDeadline(schedules[employeeIndex])
        val weeklyLog = timelogs[employeeIndex]

        (0..6).any { dayOffset ->
            if (isWeekendByOffset(startday, dayOffset)) return@any false
            
            isLate(weeklyLog[dayOffset], arrivalDeadline)
        }.not()
    }


    private fun isWeekendByOffset(startDay: Int, offset: Int): Boolean {
        val dayOfWeek = (startDay + offset - 1) % 7
        return dayOfWeek == 5 || dayOfWeek == 6
    }

    private fun calculateArrivalDeadline(scheduledTime: Int): Int {
        val deadline = scheduledTime + 10
        return if (deadline % 100 >= 60) deadline + 40 else deadline
    }

    private fun isLate(arrival: Int, deadline: Int) = arrival > deadline
}
