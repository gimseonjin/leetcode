import java.util.PriorityQueue
import kotlin.math.max

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

// 지점 간 경로
data class Trail(
    val target: TrailPoint,
    val cost: Int
)

// 등산 지점 노드
class TrailPoint(val id: Int) {
    private val connections = mutableListOf<Trail>()

    fun connectTo(target: TrailPoint, cost: Int) {
        connections.add(Trail(target, cost))
    }

    fun getConnections(): List<Trail> = connections
}

// 전체 산 구조 (그래프)
class Mountain(
    private val gates: Set<Int>,
    private val summits: Set<Int>
) {
    private val points: MutableMap<Int, TrailPoint> = mutableMapOf()

    fun addPath(from: Int, to: Int, cost: Int) {
        val fromPoint = points.getOrPut(from) { TrailPoint(from) }
        val toPoint = points.getOrPut(to) { TrailPoint(to) }
        fromPoint.connectTo(toPoint, cost)
        toPoint.connectTo(fromPoint, cost)
    }

    fun calculateFromAllGates(): Result {
        val pq = PriorityQueue<IntensityNode>()
        val intensities = mutableMapOf<Int, Int>().withDefault { Int.MAX_VALUE }

        for (gate in gates) {
            val point = points[gate] ?: continue
            intensities[gate] = 0
            pq.add(IntensityNode(point, 0))
        }

        while (pq.isNotEmpty()) {
            val current = pq.poll()
            val currentId = current.node.id
            val currentIntensity = current.intensity

            if (currentId in summits) continue  // summit 도착 시, 더 확장하지 않음
            if (currentIntensity > intensities.getValue(currentId)) continue

            for (trail in current.node.getConnections()) {
                val next = trail.target.id
                val nextIntensity = max(currentIntensity, trail.cost)

                if (nextIntensity < intensities.getValue(next)) {
                    intensities[next] = nextIntensity
                    pq.add(IntensityNode(trail.target, nextIntensity))
                }
            }
        }

        // 모든 summit 중 최소 intensity 선택
        return summits
            .map { Result(0, it, intensities.getValue(it)) }
            .filter { it.intensity < Int.MAX_VALUE }
            .minWithOrNull(compareBy<Result> { it.intensity }.thenBy { it.summit })!!
    }
}

class Solution {
    fun solution(n: Int, paths: Array<IntArray>, gates: IntArray, summits: IntArray): IntArray {
        // 1. 그래프 구성
        val mountain = Mountain(
            gates = gates.toSet(),
            summits = summits.toSet()
        )
        for (path in paths) {
            val (from, to, cost) = path
            mountain.addPath(from, to, cost)
        }

        // 2. 최적 경로 계산
        val result = mountain.calculateFromAllGates()

        // 4. 결과 반환
        return if (result == null) intArrayOf() else intArrayOf(result.summit, result.intensity)
    }
}