package com.nkia

import java.util.PriorityQueue
import kotlin.math.max

// 지점 간 경로
data class Trail(
    val target: TrailPoint,
    val cost: Int
)

// 등산 지점 노드
data class TrailPoint(val id: Int) {
    private val connections = mutableListOf<Trail>()

    fun connectTo(target: TrailPoint, cost: Int) {
        connections.add(Trail(target, cost))
    }

    fun getConnections(): List<Trail> = connections
}

// 전체 산 구조 (그래프)
data class Mountain(
    val gates: Set<Int>,
    val summits: Set<Int>
) {
    private val points: MutableMap<Int, TrailPoint> = mutableMapOf()

    fun addPath(from: Int, to: Int, cost: Int) {
        val fromPoint = points.getOrPut(from) { TrailPoint(from) }
        val toPoint = points.getOrPut(to) { TrailPoint(to) }
        fromPoint.connectTo(toPoint, cost)
        toPoint.connectTo(fromPoint, cost)
    }

    fun getPoint(id: Int): TrailPoint? = points[id]
}

// -------------알고리즘 구현 용-------------

// 결과 표현용 data class
data class Result(val gate: Int, val summit: Int, val intensity: Int)

// 우선순위 큐 노드
data class IntensityNode(
    val node: TrailPoint,
    val intensity: Int
) : Comparable<IntensityNode> {
    override fun compareTo(other: IntensityNode): Int {
        return this.intensity - other.intensity
    }
}

// Intensity 계산
object IntensityCalculator {

    fun calculateFromAllGates(mountain: Mountain): Result {
        val pq = PriorityQueue<IntensityNode>()
        val intensities = mutableMapOf<Int, Int>().withDefault { Int.MAX_VALUE }

        // 모든 시작점 한번에 주입
        for (gate in mountain.gates) {
            val point = mountain.getPoint(gate) ?: continue
            intensities[gate] = 0
            pq.add(IntensityNode(point, 0))
        }

        while (pq.isNotEmpty()) {
            val current = pq.poll()
            val currentId = current.node.id
            val currentIntensity = current.intensity

            // 산봉우리에 도달했으면 더 이상 확장하지 않음 (하나만 방문 가능하므로)
            if (currentId in mountain.summits) continue

            // 이미 더 낮은 intensity로 방문한 적이 있다면 skip
            if (currentIntensity > intensities.getValue(currentId)) continue

            // 연결된 모든 지점을 확인하며 intensity 업데이트
            for (trail in current.node.getConnections()) {
                val next = trail.target.id
                val nextIntensity = max(currentIntensity, trail.cost)

                if (nextIntensity < intensities.getValue(next)) {
                    intensities[next] = nextIntensity
                    pq.add(IntensityNode(trail.target, nextIntensity))
                }
            }
        }

        // 도달 가능한 산봉우리 중 intensity가 가장 낮은 경로 선택
        return mountain.summits
            .map { Result(0, it, intensities.getValue(it)) }
            .filter { it.intensity < Int.MAX_VALUE }
            .minWithOrNull(compareBy<Result> { it.intensity }.thenBy { it.summit })!!
    }
}

fun main() {
    data class TestCase(
        val paths: List<List<Int>>,
        val gates: List<Int>,
        val summits: List<Int>,
        val expected: List<Int>
    )

    val testCases = listOf(
        TestCase(
            paths = listOf(
                listOf(1, 2, 3), listOf(2, 3, 5), listOf(2, 4, 2), listOf(2, 5, 4),
                listOf(3, 4, 4), listOf(4, 5, 3), listOf(4, 6, 1), listOf(5, 6, 1)
            ),
            gates = listOf(1, 3),
            summits = listOf(5),
            expected = listOf(5, 3)
        ),
        TestCase(
            paths = listOf(
                listOf(1, 4, 4), listOf(1, 6, 1), listOf(1, 7, 3),
                listOf(2, 5, 2), listOf(3, 7, 4), listOf(5, 6, 6)
            ),
            gates = listOf(1),
            summits = listOf(2, 3, 4),
            expected = listOf(3, 4)
        ),
        TestCase(
            paths = listOf(
                listOf(1, 2, 5), listOf(1, 4, 1), listOf(2, 3, 1),
                listOf(2, 6, 7), listOf(4, 5, 1), listOf(5, 6, 1), listOf(6, 7, 1)
            ),
            gates = listOf(3, 7),
            summits = listOf(1, 5),
            expected = listOf(5, 1)
        ),
        TestCase(
            paths = listOf(
                listOf(1, 3, 10), listOf(1, 4, 20),
                listOf(2, 3, 4), listOf(2, 4, 6),
                listOf(3, 5, 20), listOf(4, 5, 6)
            ),
            gates = listOf(1, 2),
            summits = listOf(5),
            expected = listOf(5, 6)
        )
    )

    testCases.forEachIndexed { index, (paths, gates, summits, expected) ->
        val mountain = Mountain(
            gates = gates.toSet(),
            summits = summits.toSet()
        ).apply {
            paths.forEach {
                addPath(
                    from = it[0],
                    to = it[1],
                    cost = it[2]
                )
            }
        }

        val result = IntensityCalculator
            .calculateFromAllGates(mountain)

        println("Test #$index result: $result, expected: ${expected}")
    }
}
