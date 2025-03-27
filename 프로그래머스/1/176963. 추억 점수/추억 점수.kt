/*
사진별로 추억 점수를 매기려고 한다
사진 속 나오는 인물의 그리움 점수를 합산 한게 추억점수

["may", "kein", "kain"]이고 [5, 10, 1] -> 16점
yearning는 그리움 점수,
name의 길이는 yearning와 같다? 그치 중복도 없다

우선 name이랑 yearning을 맵으로 묶고,
photo를 순회하면서 확인한다.
*/
class Solution {
    fun solution(
        name: Array<String>, 
        yearning: IntArray, 
        photo: Array<Array<String>>
    ): IntArray {
        var answer: IntArray = intArrayOf()
        
        val nameYearningMap = mutableMapOf<String, Int>()
        for (i in 0 until name.size) {
            nameYearningMap[name[i]] = yearning[i]
        }
        
        return photo.map { group ->
            group.sumOf { name -> 
                nameYearningMap[name] ?: 0
            }
        }.toIntArray()
    }
}