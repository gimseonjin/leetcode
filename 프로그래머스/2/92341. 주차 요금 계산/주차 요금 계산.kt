import kotlin.math.ceil

data class FeeTable(
    val defaultTime: Int,
    val defaultPrice: Int,
    val unitTime: Int,
    val unitPrice: Int
) {
    companion object {
        fun from(input: List<Int>) = FeeTable(
                defaultTime = input[0],
                defaultPrice = input[1],
                unitTime = input[2],
                unitPrice = input[3]
            )
    }

    fun calculatePrice(usedTime: Int): Int {
        if(usedTime < defaultTime)
            return defaultPrice

        val moreUsedTime =
            ceil((usedTime- defaultTime).toDouble() / unitTime).toInt()

        val priceToPayMore = moreUsedTime * unitPrice

        return defaultPrice + priceToPayMore
    }
}

data class Car(
    val plate: String,
    val logs: List<Log>
) {
    private val processedLogs: List<Log> = if (logs.last().type == ParkingType.IN) {
        logs + Log("23:59".toMinute(), plate, ParkingType.OUT)
    } else {
        logs
    }

    fun calculateTotalTimes() = processedLogs
        .windowed(2, 2)
        .sumOf { (inLog, outLog) -> outLog.time - inLog.time }
}

data class Log(
    val time: Int,
    val plate: String,
    val type: ParkingType
) {
    companion object {
        fun from(input: String) = Log(
            time = input.split(" ")[0].toMinute(),
            plate = input.split(" ")[1],
            type = ParkingType.valueOf(input.split(" ")[2])
        )
    }
}

enum class ParkingType {
    IN, OUT
}

fun String.toMinute(): Int {
    val (hour, minute) = this.split(":")

    return hour.toInt() * 60 + minute.toInt()
}

class Solution {
    fun solution(fees: IntArray, records: Array<String>): IntArray {
        val feeTable = FeeTable.from(
            input = fees.toList()
        )

        val logs = records.toList()
            .map { Log.from(it) }

        return logs
            .groupBy { it.plate }
            .map { (plate, logs) ->  Car(plate, logs)}
            .sortedBy { it.plate }
            .map { it.calculateTotalTimes() }
            .map { feeTable.calculatePrice(it) }
            .toIntArray()
    }
}