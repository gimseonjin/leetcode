/*
지나다니느길 O, 장애물 X
방향 / 거리
방향(EWNS) / 거리
공원을 벗어나는지, 장애물을 만나는지 -> 실패
해피케이스 -> 안나간다, 장애물 안만난다

3칸 전진 -> 2칸 뒤에 나간다 x 있다/ 1칸만 이동
3칸 전진 -> 1칸 뒤에 나간다 x 있다 / 무시
3칸 전진 -> 0칸 뒤에(라인) 나간다. / 무시

라인 나간다 기준 -> x | y + 이동 거리
라인 (H, W) == 이거면 끝 / 안나간다 -> 내 위치 + 거리 < x 즉 같으면 나간다.
x 충돌도 -> 같으면 나간다.
*/

function find(park, target) {
  for (const y in park) {
    for (const x in park[y]) {
      if (park[y][x] === target) {
        return [Number(x), Number(y)];
      }
    }
  }
}

function parseDirection(command) {
    const [dir, amountStr] = command.split(" ")
    const amount = parseInt(amountStr)
    switch (dir) {
        case 'E': return [amount, 0];
        case 'W': return [-amount, 0];
        case 'N': return [0, -amount];
        case 'S': return [0, amount];
    }
}

function move(park, [x, y], [to_x, to_y]) {
    let next_x = x;
    let next_y = y;

    const steps = Math.abs(to_x) + Math.abs(to_y);
    const dx = Math.sign(to_x);
    const dy = Math.sign(to_y);

    for (let i = 0; i < steps; i++) {
        const tx = next_x + dx;
        const ty = next_y + dy;

        const isOutOfBounds =
            tx < 0 || tx >= park[0].length ||
            ty < 0 || ty >= park.length;

        if (isOutOfBounds) {
            return [x, y];
        }

        if (park[ty][tx] === "X") {
            return [x, y];
        }

        next_x = tx;
        next_y = ty;
    }

    return [next_x, next_y];
}

function solution(park, routes) {
    let [x, y] = find(park, "S");

    for (const route of routes) {
        const [to_x, to_y] = parseDirection(route);
        [x, y] = move(park, [x, y], [to_x, to_y]);
    }
    return [y, x]
}