private data class Board(
    private val building: MutableList<MutableList<Int>>
) {
    private val n = building.size
    private val m = building[0].size
    private val diff = Array(n + 1) { IntArray(m + 1) }

    fun applyArea(
        fromY: Int,
        fromX: Int,
        toY: Int,
        toX: Int,
        delta: Int
    ) {
        diff[fromY][fromX] += delta
        if (toX + 1 < m) diff[fromY][toX + 1] -= delta
        if (toY + 1 < n) diff[toY + 1][fromX] -= delta
        if (toY + 1 < n && toX + 1 < m) diff[toY + 1][toX + 1] += delta
    }

    fun survivedBuildings(): Int {
        // 누적합 계산
        for (y in 0 until n) {
            for (x in 1 until m) {
                diff[y][x] += diff[y][x - 1]
            }
        }
        for (x in 0 until m) {
            for (y in 1 until n) {
                diff[y][x] += diff[y - 1][x]
            }
        }

        var count = 0
        for (y in 0 until n) {
            for (x in 0 until m) {
                if (building[y][x] + diff[y][x] > 0) count++
            }
        }
        return count
    }
}

private enum class SkillType(val value: Int) {
    ATTACK(1),
    HILL(2);

    companion object {
        fun fromValue(value: Int): SkillType {
            return values().find { it.value == value }!!
        }
    }
}

private data class Skill(
    private val type: SkillType,
    private val fromY: Int,
    private val fromX: Int,
    private val toY: Int,
    private val toX: Int,
    private val damage: Int
) {
    companion object {
        fun from(input: IntArray): Skill {
            return Skill(
                type = SkillType.fromValue(input[0]),
                fromY = input[1],
                fromX = input[2],
                toY = input[3],
                toX = input[4],
                damage = input[5]
            )
        }
    }

    fun applyTo(board: Board) {
        val delta = when (type) {
            SkillType.ATTACK -> -damage
            SkillType.HILL -> damage
        }
        board.applyArea(fromY, fromX, toY, toX, delta)
    }
}

class Solution {
    fun solution(board: Array<IntArray>, skill: Array<IntArray>): Int {
        val boardData = board.map { it.toMutableList() }.toMutableList()
        val domainBoard = Board(boardData)

        skill.map { Skill.from(it) }
            .forEach { it.applyTo(domainBoard) }

        return domainBoard.survivedBuildings()
    }
}
